from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

datafile = "data.csv"

@app.route('/')
def index():
    df = pd.read_csv(datafile)

    types = []
    materials = []
    bottom_bars = []

    if 'Type' in df.columns:
        types = df['Type'].unique().tolist()

    if 'Material' in df.columns:
        materials = df['Material'].unique().tolist()

    if 'Bottom Bar' in df.columns:
        bottom_bars = df['Bottom Bar'].unique().tolist()

    return render_template('index.html', data=df.to_dict('records'), columns=df.columns.tolist(), types=types, materials=materials, bottom_bars=bottom_bars)

@app.route('/update', methods=['POST'])
def update():
    data = request.form.to_dict()
    df = pd.read_csv(datafile)
    df.loc[df['Invoice'] == data['Invoice'], 'Dealer Name'] = data['Dealer Name']
    df.to_csv(datafile, index=False)
    return '', 200

@app.route('/delete', methods=['POST'])
def delete():
    data = request.form.to_dict()
    df = pd.read_csv(datafile)
    df = df[df['Invoice'] != data['Invoice']]
    df.to_csv(datafile, index=False)
    return '', 200

@app.route('/add', methods=['POST'])
def add():
    print("Add route was hit!")
    data = request.form.to_dict()
    df = pd.read_csv(datafile)
    df = df.append(pd.DataFrame([data]), ignore_index=True)
    df.to_csv(datafile, index=False)
    return '', 200

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        print("Add_record route was hit!")
        data = request.form.to_dict()
        df = pd.read_csv(datafile)
        new_record = pd.DataFrame([data])  # Convert dict to DataFrame
        df = pd.concat([df, new_record], ignore_index=True)  # Here, we use concat instead of append
        df.to_csv(datafile, index=False)
        return redirect('/')
    else:
        return render_template('add_record.html', columns=pd.read_csv(datafile).columns)

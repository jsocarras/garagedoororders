from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<hostname>/<database>'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/{os.getenv('DB_NAME')}"

db = SQLAlchemy(app)
# define Marshmallow without the app object
ma = Marshmallow()

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<hostname>/<database>'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/{os.getenv('DB_NAME')}"

db = SQLAlchemy(app)
# bind Marshmallow to the app object
ma.init_app(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), unique=False)
    order_date = db.Column(db.String(120), unique=False)
    order_amount = db.Column(db.String(120), unique=False)
    order_details = db.Column(db.String(120), unique=False)

    def __init__(self, customer_name, order_date, order_amount, order_details):
        self.customer_name = customer_name
        self.order_date = order_date
        self.order_amount = order_amount
        self.order_details = order_details

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_name', 'order_date', 'order_amount', 'order_details')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# endpoint to create new order
@app.route("/order", methods=["POST"])
def add_order():
    customer_name = request.json['customer_name']
    order_date = request.json['order_date']
    order_amount = request.json['order_amount']
    order_details = request.json['order_details']

    new_order = Order(customer_name, order_date, order_amount, order_details)

    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)

# endpoint to show all orders
@app.route("/order", methods=["GET"])
def get_order():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)

# endpoint to get order detail by id
@app.route("/order/<id>", methods=["GET"])
def order_detail(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)

# endpoint to update order
@app.route("/order/<id>", methods=["PUT"])
def order_update(id):
    order = Order.query.get(id)
    customer_name = request.json['customer_name']
    order_date = request.json['order_date']
    order_amount = request.json['order_amount']
    order_details = request.json['order_details']

    order.customer_name = customer_name
    order.order_date = order_date
    order.order_amount = order_amount
    order.order_details = order_details

    db.session.commit()
    return order_schema.jsonify(order)

# endpoint to delete order
@app.route("/order/<id>", methods=["DELETE"])
def order_delete(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)

if __name__ == '__main__':
    app.run(debug=True)

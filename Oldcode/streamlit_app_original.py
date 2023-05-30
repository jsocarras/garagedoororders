import streamlit as st
import requests
import pandas as pd

# Use the form feature to create forms quickly
with st.form(key='Create Order Form'):
    st.write('Create a new order')
    customer_name = st.text_input('Customer Name')
    order_date = st.date_input('Order Date')
    order_amount = st.number_input('Order Amount', value=0.00)
    order_details = st.text_input('Order Details')

    # Every form must have a submit button.
    submitted = st.form_submit_button('Submit')
    if submitted:
        # make a POST request to the Flask API
        response = requests.post('http://localhost:5000/order', json={
            'customer_name': customer_name,
            'order_date': order_date.strftime('%Y-%m-%d'),
            'order_amount': str(order_amount),
            'order_details': order_details
        })
        if response.status_code == 200:
            st.write('Order created successfully')
        else:
            st.write('Failed to create order')

# make a GET request to the Flask API to get all orders
response = requests.get('http://localhost:5000/order')
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)

    selected = st.multiselect('Select orders to delete', df['id'].values)
    if st.button('Delete'):
        for id in selected:
            # make a DELETE request to the Flask API
            response = requests.delete(f'http://localhost:5000/order/{id}')
            if response.status_code == 200:
                st.write(f'Deleted order {id}')
            else:
                st.write(f'Failed to delete order {id}')

        # refresh the table after deleting orders
        response = requests.get('http://localhost:5000/order')
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            st.write(df)

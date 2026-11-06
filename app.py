import os
import streamlit as st
import mysql.connector
import pandas as pd

def fetch_data(period_number):

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.environ.get('DB_PASSWORD', 'your_password'),
        database='mrp_database'
    )
    
    cursor = connection.cursor()

    query = f"SELECT * FROM item_period WHERE period_number = {period_number};"
    
    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

st.title("Streamlit Period Data Viewer")

period = st.number_input("Enter the period number (0 to 12)", min_value=0, max_value=12, value=0)

data = fetch_data(period)

if data:
    columns = ['item_id', 'period_number', 'gross_requirement', 'projected_inventory', 'planned_order_receipt', 'planned_order_release']
    df = pd.DataFrame(data, columns=columns)

    st.write(f"Data for period {period}:")
    st.write(df)
else:
    st.write(f"No data found for period {period}.")

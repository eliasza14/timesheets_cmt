import streamlit as st
import pandas as pd
import mysql.connector

st.write("CMT Timesheets Extended")

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

cursor=conn.cursor()
cursor.execute("USE mproj_db")
cursor.close()

df1=pd.read_sql("SELECT * FROM kimai2_users", conn)
st.write(df1)

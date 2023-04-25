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
st.write(conn)



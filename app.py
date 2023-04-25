import streamlit as st
import pandas as pd
import mysql.connector

st.write("CMT Timesheets Extended")

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     return mysql.connector.connect(**st.secrets["mysql"])

# conn = init_connection()




cnx=mysql.connector.connect(host='5.77.39.26',port=3306,user='mproj_user2',password='xVHHCNU1UR}v')

if cnx.is_connected():
    print('Successfully connected')
    st.write("connect to db")
    
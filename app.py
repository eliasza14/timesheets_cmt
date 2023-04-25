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

st.write("VERSION 1")
# cursor=conn.cursor()
# cursor.execute("USE mproj_db")
# cursor.close()

sql = """SELECT kimai2_timesheet.*,kimai2_users.alias,kimai2_projects.name as project_name,kimai2_activities.name as activity_name,kimai2_timesheet_tags.name as tag_name FROM kimai2_timesheet 
INNER JOIN kimai2_users ON kimai2_timesheet.user=kimai2_users.id
INNER JOIN kimai2_projects ON kimai2_timesheet.project_id=kimai2_projects.id
INNER JOIN kimai2_activities ON kimai2_timesheet.activity_id=kimai2_activities.id
INNER JOIN (SELECT * FROM kimai2_tags INNER JOIN kimai2_timesheet_tags ON kimai2_tags.id=kimai2_timesheet_tags.tag_id ) AS kimai2_timesheet_tags ON kimai2_timesheet.id=kimai2_timesheet_tags.timesheet_id
"""
# df1=pd.read_sql(sql, conn)
# st.write(df1)


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query(sql)

st.write(rows)
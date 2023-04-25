import streamlit as st
import pandas as pd
import mysql.connector

st.write("CMT Timesheets Extended")

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
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


# @st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        columnsnames=cur.column_names
        return cur.fetchall(),columnsnames

rows,columnames = run_query(sql)

st.write(columnames)
df1=pd.DataFrame(rows,columns=columnames)



# df1=pd.read_sql(sql, conn)
st.write(df1)

df2=df1[['start_time', 'end_time','duration', 'description', 'rate', 'fixed_rate', 'hourly_rate' , 'internal_rate', 'alias', 'project_name', 'activity_name','tag_name']]
st.write(df2)
# st.write(rows)
# for row in rows:
#     st.write(f"{row[18]} is :{row[18]}:")

st.write("TESTTTTTTTT")
names=df2['alias'].unique().tolist()


name_choice = st.sidebar.selectbox('Select  name:',('',names))
dfbyname=df2[df2['alias']==name_choice]
st.write(dfbyname)

projects=dfbyname['project_name'].unique().tolist()


project_choice = st.sidebar.selectbox('Select  project:', projects)
dfbyproject=dfbyname[dfbyname['project_name']==project_choice]
st.write(dfbyproject)
# year_choice = st.sidebar.selectbox('', years)
# model_choice = st.sidebar.selectbox('', models)
# engine_choice = st.sidebar.selectbox('', engines)






# option = st.selectbox(
#     'How would you like to be contacted?',
#     (df2['alias'].unique().tolist()))

# st.write('You selected:', option)

# st.write(df2[df2['alias']==option])
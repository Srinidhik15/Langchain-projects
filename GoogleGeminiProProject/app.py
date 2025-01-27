# This file is responsible for creating our LLM application

import os
from dotenv import load_dotenv
load_dotenv()  # load all the env variables

import streamlit as st
import sqlite3
import google.generativeai as genai

# configure GenAI key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a function to load Google Gemini model and provide quesries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

# Create function to retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    for row in rows:
        print(row)
    return rows

# Define your prompt
prompt=[
    """
    You are an expert in converting english question to sql query.
    The sql database has the name STUDENT and has the following columns - NAME, CLASS
    SECTION \n\nFor example, \nExample 1 - How many entries of record are present?,
    the sql command will be something like this SELECT COUNT(*) from STUDENT;
    \nExample 2 - Tell me all the  students study in Data Science class?,
    the sql command will be something like this SELECT * from STUDENT where CLASS="Data Science";
    also the sql code should not have ''' in the beginning or end and sql word in output
    """

]

# streamlite app set up
st.set_page_config(page_title="I can retrieve any SQL Query")
st.header("Gemini App to retrieve SQL Data")
question=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

# if submit is cliked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)

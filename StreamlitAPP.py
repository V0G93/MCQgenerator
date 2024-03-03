import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.MCQgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.MCQgenerator.MCQgenerator import generate_evaluate_chain
from src.MCQgenerator.logger import logging

with open('C:\Users\victo\MCQgenerator\Response.json','r') as file:
    RESPONSE_JSON=json.load(file)

st.title("MCQ Creator App with LangChain")

with st.form("user_inputs"):
    uploaded_file=st.file_uploader("Upload PDF or txt")

    mcq_count=st.number_input("No of MCQs",min_value=3,max_value=50)
    subject=st.text_input("Insert Subject",max_chars=20)
    tone=st.text_input("Complexity level of questions",max_chars=20,placeholder="Simple")
    button=st.form_submit_button("Create MCQs")

    

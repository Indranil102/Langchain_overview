from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st



load_dotenv()

st.header("research Tool")

user_input=st.text_input("Enter your prompt")

if st.button:
    st.text("some random text")
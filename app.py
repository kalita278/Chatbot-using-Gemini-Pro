import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))



def get_response(question):
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(question)

    return response.text


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_response(input)
    st.subheader("The Response is")
    st.write(response)
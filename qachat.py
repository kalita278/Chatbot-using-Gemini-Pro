import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-1.0-pro')
chat = model.start_chat(history=[])

def get_response(question):
   
    response = chat.send_message(question,stream=True)

    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []



input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit and input:
    
    response=get_response(input)

    st.session_state['chat_history'].append(('you',input))

    st.subheader("The Response is")


    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))

st.subheader("The Chat History is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from PIL import Image


load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-pro')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text



st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_response(input,image)
    st.subheader("The Response is")
    st.write(response)
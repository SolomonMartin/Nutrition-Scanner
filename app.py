from dotenv import load_dotenv
import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_response(prompt,image):
    response = model.generate_content([prompt,image[0]])
    return response.text

prompt = """
You are a nutritionist and are well versed with the nutritional aspects of various food types
given an image below tell me what all food items are in the image , along with the calories per item. 
also give me the percentage of protein, carbohydrates, fibers, sugar and other.
Let me know if the food is health or not and given reason for the same .

image :

"""

def get_img_bytes(image):
    img_bytes = image.getvalue()
    img_content = [
        {
            "mime_type": image.type,
            "data": img_bytes
        }
    ]
    return img_content

st.set_page_config("Calorie and Nutrition")
st.header("Gemini Calories from Image")
uploaded_file = st.file_uploader("Upload image of food", type=["jpg","jpeg","png"])
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        #uploaded_file = Image.open(uploaded_file)
        res = get_img_bytes(uploaded_file)
        response = get_response(prompt,res)
        st.write(response)
    else:
        raise FileNotFoundError
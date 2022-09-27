import streamlit as st
import pandas as pd
import numpy as np
import cv2

def canny_filter(image):
     bytes_data = picture.getvalue()
     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
     gray = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
     gauss = cv2.GaussianBlur(gray, (3,3), 0)
     thresh = 20
     canny_output = cv2.Canny(gauss, thresh, thresh * 5)

     return canny_output

st.set_page_config(layout="wide")

st.title("Mi primera App en Streamlit")

st.subheader("Convolución y filtro Canny de imagenes")
c1, c2, c3, c4 = st.columns(4)
picture = c1.camera_input("Take a picture")
with c2:
     if picture:
          st.image(picture)
          c2 = st.image(canny_filter(picture), "Your picture's edges")



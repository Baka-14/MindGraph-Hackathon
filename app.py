import streamlit as st  
from PIL import Image

st.set_page_config(page_title = "Mind Graph Hackathon", page_icon = ":globe_with_meridians:", layout = "wide",)

with st.container():
     new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px; text-align: center">Mind Graph Hackathon</p>'
     st.markdown(new_title, unsafe_allow_html=True)
     st.header("Target Market")
     st.header("Market Size")
     st.write("")

with st.container():
     st.header("Market Size")
     st.write("")
     
with st.container():
     st.header("Market Segmentation")
     st.write("")
     
     col1, col2, col3 = st.columns([1,1,1])

with col1:
     img = Image.open("fest1.png")
     st.image(img,width=500)

with col2:
     img = Image.open("fes.png")
     st.image(img,width=390)

with col3:
     img = Image.open("c3.png")
     st.image(img,width=390)
     

with st.container():
     st.header("Demo Graphics")
     st.write("")

with st.container():
     st.header("Psycho Graphics")
     st.write("")

with st.container():
     st.header("Strengths and Weakness")
     st.write("")

with st.container():
     st.header("Market Trends")
     st.write("")
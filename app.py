import streamlit as st  
from PIL import Image

st.set_page_config(page_title = "Mind Graph Hackathon", page_icon = ":globe_with_meridians:", layout = "wide",)

with st.container():
     new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px; text-align: center">Mind Graph Hackathon</p>'
     st.markdown(new_title, unsafe_allow_html=True)
    

with st.container():
     st.header("Target Market")
     st.write("As you can see the target market for our product would be all the Participants for the various events that take place the exact number comes down to ")
     
     
with st.container():
     st.header("Market Size")
     st.write("As you can see from the pie chart our market size is  %")
     


with st.container():
     st.header("Demo & Psycho Graphics")
     st.write("")

with st.container():
     st.header("Strengths and weaknesses")
     st.write("Our Weaknesses are we dont have much data regarding the what exactly happens in each club event ") 
     st.write("We dont have data from the past few years which would have given out better market trends") 
     st.write("However our Strengths are that we are able to deduplicate data pretty quickly and thereby give us more time to hypertune our product")

with st.container():
     st.header("Market Trends")
     col1, col2= st.columns([1,1])

with col1:
     img = Image.open("fest1.png")
     st.image(img,width=500) 
     st.write("")

with col2:
     img = Image.open("fest2.png")
     st.image(img,width=500)   

with st.container(): 
     st.write("[For More information click here](https://github.com/Baka-14/MindGraph-Hackathon)")




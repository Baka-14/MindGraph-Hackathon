
import streamlit as st  
from PIL import Image

st.set_page_config(page_title = "Mind Graph Hackathon", page_icon = ":globe_with_meridians:", layout = "wide",)

with st.container():
     new_title = '<p style="font-family:sans-serif; color:White; font-size: 80px; text-align: center">Mind Graph Hackathon</p>'
     st.markdown(new_title, unsafe_allow_html=True)
    

with st.container():
     st.header("Target Market")
     percent = 96
     st.write("As you can see the target market for our product would be all the Participants for the various events that take place the exact-: ")
     st.write(f"The number comes down to {percent}% of the meta data")
     st.write("The business model would be to bridge the gap between clubs and participants by being a analytics platform(SaaS product)") 
     
     
with st.container():
     st.header("Market Size")
     img = Image.open("Images/roles.png")
     st.image(img,width=500) 
     st.write("As you can see from the pie chart our market size is about 96%") 

with st.container():
     st.header("Market Segmentation")
     st.write("The market can be divided in 2 ways-:")
     st.write("The First being with respect to different year Students and Later being with respect to Clubs")
     col1, col2= st.columns([1,1]) 
with col1:
     img = Image.open("Images/students.png")
     st.image(img,width=500) 
     st.write("We can infer from the given data that from clubs we can see that they are more 17XJ than 18XJ in terms of participatents thereby giving us a clear indication on whom to target")

with col2:
     img = Image.open("Images/clubs.png")
     st.image(img,width=500) 
     st.write("As we can see the CLubs Bar Graph they are almost quite evenly distributed thereby tell us that each club has equal amount of potential") 


with st.container():
     st.header("DemoGraphics")
     img=Image.open("Images/students.png")
     st.image(img,width=500)
     st.write("As we can see our demographic is college students and they would comprise of seniors and juniors who actively partcipate in various fests and club events")

with st.container():
     st.header("Strengths and weaknesses")
     st.write("Our Weaknesses are we dont have much data regarding the what exactly happens in each club event ") 
     st.write("We dont have data from the past few years which would have given out better market trends") 
     st.write("However our Strengths are that we are able to deduplicate data pretty quickly and thereby give us more time to hypertune our product")
     st.write("Our event deciding forum would be community driven which means its a strong sign onto to figure out what is working and what is not with zero bias")

with st.container():
     st.header("Market Trends")
     col1, col2= st.columns([1,1])

with col1:
     img = Image.open("Images/fest1.png")
     st.image(img,width=500) 
     st.write("As we can see in the fest1 pie chart fests 1,2,3,4,5 seem to be getting the most participation hence they should be promoted more and events similar to them should be conducted")

with col2:
     img = Image.open("Images/fest2.png")
     st.image(img,width=500) 
     st.write("As we can see in the fest2 pie chart fests 1,2,3,4,5 seem to be getting the most participation hence they should be promoted more and events similar to them should be conducted") 

with st.container(): 
          col1, col2,col3= st.columns([1,1,1])

with col1:
     img = Image.open("Images/Club1.png")
     st.image(img,width=500) 
     st.write("In the Piechart of Club1 its clearly visible that Its event 1 and 2 seem to be big hits therefore they should work around and figure out what is causing them to have such huge participation unlike event 3 ")

with col2:
     img = Image.open("Images/Club2.png")
     st.image(img,width=500) 
     st.write("In the Piechart of Club2 its clearly visible that Its event 1 and 2 seem to be big hits therefore they should work around and figure out what is causing them to have such huge participation unlike event 3 ") 


with col3:
     img = Image.open("Images/Club3.png")
     st.image(img,width=500) 
     st.write("In the Piechart of Club3 its clearly visible that Its event 1 and 2 seem to be big hits therefore they should work around and figure out what is causing them to have such huge participation unlike event 3 ") 



with st.container(): 
     st.write("[For More information click here](https://github.com/Baka-14/MindGraph-Hackathon)")





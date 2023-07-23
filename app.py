import streamlit as st
import pandas as pd
import time
from matplotlib import pyplot as plt
import numpy as np
st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="😂",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title("Welcome to Market basket data Miner")
#st.title used to set title which is tile of page

st.subheader("Please make sure you have transaction file in CSV format")
#subheader used to show subheading
st.header("upload here")
#header is just geading to particular thing bigger than subheader
st.text("Once uploades please click on submit to proceed")
# text work exactly like paragraph in html

st.markdown("My first webapp :joy: " )#emoji for :happy:
st.markdown("[Click here to go sanjaydh.com ](https://www.sanjaydh.com)")
# We can use this type of html things to explore more go to  https://www.markdownguide.org/cheat-sheet/
st.caption("Caption here")
st.latex("hi")#to print maths equation like matrix and other check https://katex.org/docs/supported.html
json ={"a":"1,2,3", "b":"4,5,6"}# used to write key value pairs
st.json(json)#used to print in screen
st.write("## H2")# used wite anyleements inside 
# st.metric()used to write equation like windspeed 120ms-1(in superscriot)
table = pd.DataFrame({"column1":[1,2,3,4,5],"column2":[5,6,7,8,9]})
st.table(table)#table used to print table
st.dataframe(table)# used to print dataframe with some asc, desc selection

# to import images, audio, and video
# st.image(" "), st.audio(" "), st.video(" ")

#To remove hamburger(3lines) and footer that says made by streamlit
# inspect 3lines locate class name copy and do this

# st.markdown("""
    
#     <style>
# .css-1a1tcp.e1ewe7hr3
# {
#     visibility: hidden;
# }
# .css-h5rgaw.e1g8pov61
# {
#     visibility: hidden;
# }
# </style>
# """,unsafe_allow_html=True)


#In Streamlit, checkboxes are interactive elements that allow users
# to make binary choices. A checkbox is represented by a boolean 
# variable, which can be either checked (True) or unchecked 
# (False). Users can toggle the checkbox by clicking on it, 
# and the app can respond to the user's choice based on the
# state of the checkbox.

# Create a checkbox
checked = st.checkbox("Check me!")

# Respond to the user's choice
if checked:
    st.write("Checkbox is checked!")
else:
    st.write("Checkbox is unchecked!")

show_data = st.checkbox("Show Data")

# Display data only when the checkbox is checked
if show_data:
    data = [1, 2, 3, 4, 5]
    st.write("Here's the data:")
    st.write(data)
    
    
# def move():
# #   print("Its dynamic")
#     print(st.session.uniqueid)
    
# test = st.checkbox("che ck function", value=True, on_change=move, key="uniqueid")        

# rad = st.radio("Are you noob", options=("Yes", "No"))
# #radio button can use properties like checkbutton above
# def btnfun():
#     print("you clicked me")
# btn = st.button("Click me!", on_click=btnfun)

# #button search your self

# slct = st.selectbox("whats your game",options=("coc","pubg","cod"))

# mulslct = st.multiselect("whats your game",options=("coc","pubg","cod"))

# st.write(mulslct)

#slider widgets
st.slider("Slider", min_value=1,max_value=10)

# text input widget used to take few line of text
st.text_input("Fill me", max_chars=10)

#text area widget to take large text
st.text_area("Enter most text", max_chars=100)

# data and time widget to take ip of format time and date
st.date_input("Select data")
st.time_input("Slect time")


st.markdown("---")
# file uploader option
#we can upload, image,video, files even multiple files

upl = st.file_uploader("Upload your file", type=("jpg","png","mp4","csv"),accept_multiple_files=False)

if upl is not None:
    df = pd.read_csv(upl)

        # Display the contents of the CSV file
    st.subheader("Uploaded CSV File is:")
    st.dataframe(df)
    
#creating forms in streamlit with "with" keyword
#you can also use object to create form
# with st.form("My form"):
#      st.text_input("Name")
#      st.form_submit_button("Submit")   
     
     
#we can divide anyscreen in columns, lets divide form for eg
# with st.form("My form"):
#      c1,c2=st.columns(2)
#      c1.text_input("Name")
#      c2.text_input("Lname")
#      st.text_input("email")
#      st.text_input("password")
#      st.form_submit_button("Submit")      

#more custumization with forms
# st.markdown("<h1 style='text-align:center;'>Form</h1>",unsafe_allow_html=True )
# with st.form("My form", clear_on_submit=True):
#      c1,c2=st.columns(2)
#      fn =c1.text_input("Name")
#      ln = c2.text_input("Lname")
#      st.text_input("email")
#      pas =st.text_input("password")
#      day,mon,year = st.columns(3)
#      day.text_input("day")
#      mon.text_input("month")
#      year.text_input("year")
#      sub = st.form_submit_button("Submit")   
#      if sub:
#        if fn == "" and ln == "" and pas == "":
#          st.warning("Please fill")
#        else:
#            st.success("Submitted!")

#progress bar track progress of the task, can use while data is analyzing
# bar = st.progress(100)#(value 0 represent bar is in 0, 50 is half , 75 is 1/4 100 is full)
# # pro_stat = st.empty()
# for i in range(100):
#     bar.progress((i+1)*10)
#     # pro_stat.write(str(i+1)+"%") we can show percentage with progress
#     time.sleep(0.4) # to use time.sleep import time
n = np.linspace(0,10,100)
x = np.array([10,20,30,40,50])
opt = st.sidebar.radio("Selct type of graph", options=("line","bar","h-bar"))
if opt == "line":
    st.markdown("<h1 style='text-align:center;'>line Graph</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(n,np.sin(n))
    plt.plot(n,np.cos(n),'--')
    st.write(fig)
    
elif opt == "bar":
    st.markdown("<h1 style='text-align:center;'>Bar Graph</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(x,x*10)
    plt.plot(x,x+10)
    st.write(fig)
elif opt == "h-bar":
    st.markdown("<h1 style='text-align:center;'>H-bar Graph</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(x*10,x)
    plt.plot(x+10,x)
    st.write(fig)
    
    #Notes: We can create user input from form eg webscarpper
    #pil library used to build image editor
    # st.number_input() used to take number as input
    st.file_uploader("Upload", type="CSV",accept_multi_file=True)

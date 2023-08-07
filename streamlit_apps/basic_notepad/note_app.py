import streamlit as st
import os
from PIL import Image

im = Image.open('note_icon.png')
st.set_page_config(
    page_title="Taking Notes",
    page_icon=im,
    layout="centered",
)

title = '<h3 style="color: cyan; text-align: center;">Quick-Notes 📖 🖊️</h3>'
title2 = '<p style="color: white; text-align: center;">A Streamlit Powered note taking Web Application </p>'


def clear():
    st.session_state['text'] = ""
    
def main():

    #title
   
    st.markdown(title,   unsafe_allow_html=True)
    st.markdown(title2,  unsafe_allow_html=True)
    #type area
    text = st.text_area(label = ":blue[Write Your Notes Here:]", key = "text", height = 400, placeholder ="Type Here..")
    col1, col2 = st.columns(2)
    with col2:
        st.button("Clear", on_click=clear)
    
    
    with col1:
        notes = st.session_state['text']
        st.download_button("Save", data = notes, file_name ="MyNotes.txt" )
    
    
if __name__ == "__main__":
    main()

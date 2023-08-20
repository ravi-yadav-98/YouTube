#import

from rembg import remove
import streamlit as st 
from PIL import Image


st.title("Image Background Removal Tool: :white_check_mark:")
st.markdown(":green[A Remgb Powered Image Background Removal Tool.] :red[ Try this !!!]")
st.markdown('<hr>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(":red[Choose and Upload Image file here]", type=['.png', '.jpg', '.jpeg'])

if uploaded_file is not None:
    # img_path = uploaded_file.name
    button = st.button("Remove Background")
    if button:

        image = uploaded_file.read()
        out_img = remove(image)
        col1, col2 = st.columns(2)
        with col1:
            img = st.image(image, caption='Original Image')
        
        with col2:
            img2 = st.image(out_img, caption='Original Image')
        
    





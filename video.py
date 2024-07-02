import base64
import streamlit as st


def show_video(name):
    file_ = open(name, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="landings gif">',
        unsafe_allow_html=True,
    )

def render_image(filepath: str):
   """
   filepath: path to the image. Must have a valid file extension.
   """
   mime_type = filepath.split('.')[-1:][0].lower()
   with open(filepath, "rb") as f:
      content_bytes = f.read()
      content_b64encoded = base64.b64encode(content_bytes).decode()
   image_string = f'data:image/{mime_type};base64,{content_b64encoded}'
   st.image(image_string)
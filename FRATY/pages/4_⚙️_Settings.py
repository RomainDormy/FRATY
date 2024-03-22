import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import re
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.customize_running import center_running
import time
from streamlit_extras.stoggle import stoggle 
import os
import resend
import numpy as np

st.title("Settings")

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.text_area("this is tab 1")
tab2.write("this is tab 2")

with st.spinner(text='In progress'):
    time.sleep(1)

# Show and update progress bar
#bar = st.progress(50,"ok")

uploaded_file = st.file_uploader("Select Image",type=["png","jpg","jpeg"],accept_multiple_files=False)
if uploaded_file is not None:
    st.image(uploaded_file)
    st.toast("Image added - "+uploaded_file.name,icon="✅")
    

st.toast('Mr Stay-Puft')

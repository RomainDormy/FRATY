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

st.set_page_config(
    page_title="Visualisation chaque produit",
    page_icon="🚀",
    layout="wide"
)






st.title("Page d'Accueil")


selector, test1, test2, test3, test4 = st.columns(5)
with selector:
    selected_option = st.selectbox('Selectionne le produit :', ["🍎🍐 Compote Multifruits", "🍕 Pizza", "🥪 Sandwich"])
st.text(" ")


# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

#print(selected_option)
# Fetch existing vendors data
if selected_option == "🍎🍐 Compote Multifruits":
    existing_data = conn.read(worksheet="1", usecols=list(range(8)), ttl=5)
elif selected_option == "🍕 Pizza":
    existing_data = conn.read(worksheet="2", usecols=list(range(8)), ttl=5)
elif selected_option == "🥪 Sandwich":
    existing_data = conn.read(worksheet="3", usecols=list(range(8)), ttl=5)


existing_data = existing_data.dropna(how="all")
num_lines = existing_data.shape[0]



tab1, tab2, tab3 = st.tabs(['Valeur Nutritive','Empreinte Carbone','Répartition des couts'])

for i in range(num_lines):
    nutri = str(existing_data.loc[i, 'Step'])+" - "+str(existing_data.loc[i, 'Product Name'])+" en "+str(existing_data.loc[i, 'Localisation'])+" --> "+str(existing_data.loc[i, 'Calories (Kj)'])+" Kcal"
    if (str(existing_data.loc[i, 'Step']) == "🛒 Mise en rayon"):
        tab1.write(f"➡️➡️ **{nutri}**")
    else: 
        tab1.write(nutri)
    carbone = str(existing_data.loc[i, 'Step'])+" - "+str(existing_data.loc[i, 'Product Name'])+" en "+str(existing_data.loc[i, 'Localisation'])+" --> "+str(existing_data.loc[i, 'Empreinte Carbone'])+" eq CO2"
    if (str(existing_data.loc[i, 'Step']) == "🛒 Mise en rayon"):
        tab2.write(f"➡️➡️ **{carbone}**")
    else: 
        tab2.write(carbone)
    couts = str(existing_data.loc[i, 'Step'])+" - "+str(existing_data.loc[i, 'Product Name'])+" en "+str(existing_data.loc[i, 'Localisation'])+" --> "+str(existing_data.loc[i, 'Cout (€/u)'])+" Kcal"
    if (str(existing_data.loc[i, 'Step']) == "🛒 Mise en rayon"):
        tab3.write(f"➡️➡️ **{couts}**")
    else: 
        tab3.write(couts)

#Display Data Table
#st.dataframe(existing_data)


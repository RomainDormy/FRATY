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
import streamlit_shadcn_ui as ui
import numpy as np

st.set_page_config(
    page_title="Dashboard Management Portal",
    page_icon="🚀",
    layout="wide"
)
# Display Title and Description
st.title("Dashboard Management Portal")

# Add logo
add_logo("https://scribate.com/wp-content/uploads/2024/02/small-logo.png",height=80)




# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
existing_data = conn.read(worksheet="Comp1", usecols=list(range(8)), ttl=5)
existing_data = existing_data.dropna(how="all")


testing_data = existing_data.copy()
testing_data = testing_data[['NewHire Name', 'Start Date']]
testing_data['Start Date'] = pd.to_datetime(testing_data['Start Date'], format='%d/%m/%y')

# Filter out past dates
today = datetime.now()
testing_data = testing_data[testing_data['Start Date'] >= today]
#Sort Starters by Start Date
testing_data.sort_values(by='Start Date', inplace = True) 


#Total lines in Sheet
total_launched = existing_data.shape[0]

#Total lines marked as completed
completed_rows = existing_data[existing_data.iloc[:, 0] == "🟢 Completed"]


# Count the number of rows that match the condition
num_completed_rows = completed_rows.shape[0]

# Metric Cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Total Launched", content=str(total_launched), description="+20% from last month", key="card1")
with cols[1]:
    ui.metric_card(title="Total Completed", content=str(num_completed_rows), description="+11% from last month", key="card2")
with cols[2]:
    ui.metric_card(title="Next Starting Hire", content=testing_data["NewHire Name"].iloc[0], description="Starting "+str(existing_data.iloc[testing_data.index[0]]["Start Date"]), key="card3")



#Data for Graph

# Convert 'Dates' column to datetime format to extract the month
existing_data['Start Date'] = pd.to_datetime(existing_data['Start Date'], format='%d/%m/%y')

# Extract the month into a new column
start_months = existing_data['Start Date'].dt.month.tolist()

# Group by month and year of the "Start Date" and count the number of users

month_counts = [start_months.count(month) for month in range(1,13)]

def generate_sales_data():
    month_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    hires = month_counts  # Ensure month_counts is defined and in the correct order
    # Create DataFrame with an explicit order for 'Month' using Categorical data type
    month_df = pd.DataFrame({
        'Month': pd.Categorical(month_ordered, categories=month_ordered, ordered=True),
        'Hires': hires
    })
    return month_df


month_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
chart_config = {
    'mark': {'type': 'bar', 'tooltip': True, 'fill': 'rgb(20, 20, 200)', 'cornerRadiusEnd': 4},
    'encoding': {
        'x': {'field': 'Month', 'type': 'ordinal', 'sort': month_ordered},  # Explicitly define sort order
        'y': {'field': 'Hires', 'type': 'quantitative', 'axis': {'grid': True}},
    },
}
st.markdown("Employees Starting:")
st.vega_lite_chart(generate_sales_data(), chart_config, use_container_width=True)



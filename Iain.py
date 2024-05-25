import streamlit as st
import folium 
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from streamlit_gsheets import GSheetsConnection


# Google Sheet URL
url = "https://docs.google.com/spreadsheets/d/1fC354qoKCC847OFmI9p32evXxcCCw_FPvzx9CkhGsVk/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols = [1,2,3,4,5,6])

st.dataframe(data)
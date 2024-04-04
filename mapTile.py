import streamlit as st
import requests as req
from streamlit_lottie import st_lottie as stl
import folium as fol
import pandas as pd
from streamlit_folium import folium_static

st.set_page_config(page_title="MapApp", page_icon=":compass:", layout="wide")

def load_anim(url):
    ref=req.get(url)
    if ref.status_code != 200:
        return None
    return ref.json()

#------- Animation Load Sector -----
stlLoader = load_anim("https://lottie.host/d54acd1d-6de7-4904-aa10-75a8fdcd616e/xGF6C3UQuS.json")


#------- Header Section ----------
with st.container():
    left_col, right_col = st.columns((1,1))
    with left_col:
        st.subheader("Welcome to Map Tile! :pushpin:")
        st.title("Your one stop destination for location app")
        st.write("Our project work upon the tech stack of  ")
        st.write("[Learn More]()")
    with right_col:
        stl(stlLoader, height=300, key="animation_load")

#----------- MAP GENERATION SECTION ------------
data = pd.read_csv('station.csv')
data2=pd.read_csv('loc.csv')
a=data['Longitude'].mean()
b=data['Latitudes'].mean()

def generate_map():
    # Generate the map first
    myObj = fol.Map(zoom_start=15, location=[23.856667, 81.878889])

    #Generate the markers present in the csv file
    for index, row in data.iterrows():
        popup_html = f"<b>Station Name:</b> {row['StationName']}<br><b>Station Code:</b> {row['StationCodes']}"

        h=row['Longitude']
        j=row['Latitudes']
        fol.Marker([h,j], popup=fol.Popup(popup_html, max_width=300),icon=fol.Icon(color='red')).add_to(myObj)
    
    for index, row in data2.iterrows():
        h1=row['lat']
        j1=row['loft']  
        fol.Marker([h1,j1], popup=fol.Popup(popup_html, max_width=300),icon=fol.Icon(color='green')).add_to(myObj)


    return myObj
#-------------------------------------------------


st.write("---")
st.write("##")
#-------- Dashboard ---------
st.title("Dashboard")
folium_map = generate_map()
folium_static(folium_map)

import folium as fol
import pandas as pd

data = pd.read_csv('station.csv')
a=data['Longitude'].mean()
b=data['Latitudes'].mean()
myObj = fol.Map(zoom_start=10, location=[a,b])

for index, row in data.iterrows():
    popup_html = f"<b>Station Name:</b> {row['StationName']}<br><b>Station Code:</b> {row['StationCodes']}"

    h=row['Longitude']
    j=row['Latitudes']
    fol.Marker([h,j], popup=fol.Popup(popup_html, max_width=300),icon=fol.Icon(color='red')).add_to(myObj)

myObj.save('map.html')
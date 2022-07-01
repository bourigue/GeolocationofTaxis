  
from numpy import integer
from plyer import notification
import openrouteservice
import requests

import folium
import requests
from .models import Measurement, client
import mysql.connector  as mcdb
conn=mcdb.connect(host="localhost",user="root",password="",database="geocalisation_taxi")
cur=conn.cursor()

def notofyMe(title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon='static/photo/ico.ico',
    timeout=10,
    )

def notofyMch(title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon='static/photo/taxi.ico',
    timeout=10,
    )
def tabnot():
   cur.execute("SELECT * FROM `pages_measurement`")
   data=cur.fetchall()
   con=None
   for i in data:
    b=Measurement.objects.all()
    msg=i[1]+"    vers     "+i[2]
    notofyMe('Demnader Taxi',msg)
def noticli():
   cur.execute("SELECT * FROM `pages_commande`")
   data=cur.fetchall()
   con=None
   for i in data:
    b=Measurement.objects.all()
    msg=i[1]+"    vers     "+i[2]+"  "+i[11]+"  "+"places"
    notofyMe('Demnader Taxi',msg)
def notich():
   cur.execute("SELECT * FROM `pages_orderchauffeur`")
   data=cur.fetchall()
   con=None
   for i in data:
    b=Measurement.objects.all()
    msg=i[1]+"    "+i[6]+"    "+i[2]
    notofyMch('Votre Taxi moi',msg)

def map():
       client=openrouteservice.Client(key='5b3ce3597851110001cf6248c2e292e64f8440369997bec0ee255a61')
       res=requests.get('https://ipinfo.io')
       data=res.json()
       location = data['loc'].split(',')
       lat = float(location[0])
       lng = float(location[1])
       print(lng, lat)
       tooltip ='clik for mor information'
       coordinates = [[lat, lng], [-84.191850,
       25.971645]]
       # folium.Marker([lat, lng],
       #    popup ='<strong>hee am kraza</strong>',
       #        tooltip=tooltip,
       #      ).add_to(m)
       # folium.Marker([, ],
       #   popup ='<strong>hee am kraza</strong>',
       #       tooltip=tooltip,
       #     ).add_to(m)
       #folium.Marker([26.345455, 39.5645677],
       #   popup ='<strong>hee am kraza</strong>',
       #       tooltip=tooltip,
       #     ).add_to(m)
       route = client.directions(coordinates=coordinates, profile='driving-car',format='geojson')
       m =folium.Map(width=1341,height=600,location=[lat, lng], zoom_start=14)
       
       folium.GeoJson(route, name='route').add_to(m)
       folium.LayerControl().add_to(m)
       m.save("compteclient.html")
      
       return m

   




   


from django import http
from django.http.request import HttpHeaders
from mysql.connector.errors import DatabaseError
from pages.forms import clientForm
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render
from .models import ChofoChoisir, chauffeur, client, file_upload, orderchauffeur
from .forms import clientForm,chauffeurForm,taxiForm,arderchofo,CmdForm,ChofoChoisirForm
from plyer import notification
from .models import client,chauffeur,Commande
from .NOTI import notofyMe,map,tabnot,noticli,notich
import folium,jupyter
import requests
from .forms import CreateUserForm
import mysql.connector  as mcdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

conn=mcdb.connect(host="localhost",user="root",password="",database="geocalisation_taxi")
cur=conn.cursor()




def notificlient(request):

   id_chof=request.session['chofo_id']
   cho=chauffeur.objects.get(id=id_chof)
   onj=Commande.objects.all()
   res=requests.get('https://ipinfo.io')
   data=res.json()
   location = data['loc'].split(',')
   data=cur.execute("SELECT lat FROM `pages_orderchauffeur`")
   data=cur.fetchall()
   lat = float(location[0])
   lng = float(location[1])
   
   cont = {'pro': onj,'cho':cho,'lat':lat,'lng':lng}
   if request.method=='POST' and 'accepter' in request.POST:
       form1=arderchofo(request.POST)
       if form1.is_valid():
          form1.save()
          return redirect('notificlient')
   else:

    return render(request,'pages/notificlient.html',cont)
# Create your views here.



def chofo(request):
         idchofor=request.session['chofo_id']
         b=chauffeur.objects.get(id=idchofor)   
         #  onj=Measurement.objects.get(id=1)
         
         countt=Commande.objects.all()
         counttt=countt.count()
         res=requests.get('https://ipinfo.io')
         data=res.json()
         location = data['loc'].split(',')
         lat = 32.3192#float(location[0])
         lng = -6.3498#float(location[1])
         pointA=[lat, lng]
         #  form=MeasurementModelForm(request.POST or None)
         re="SELECT ord.lat,ord.lng FROM `pages_chofochoisir` ch ,`pages_orderchauffeur` ord where ord.id=ch.id_orderch "
         cur.execute(re)
         data=cur.fetchall() 
    # initial folium map
         m = folium.Map(width=1495,height=660, location=[lat, lng], zoom_start=14)
         folium.Marker([lat, lng], tooltip='c est votre position',
           icon=folium.features.CustomIcon('static/photo/taxi.ico')).add_to(m)
    # location marker
         for i in data: 
           pointB=[i[0], i[1]]
           lin=folium.PolyLine(locations=[pointA,pointB],weight=2,color='blue') 
           m.add_child(lin) 
           folium.Marker([i[0], i[1]], tooltip='click here for more',
           icon=folium.features.CustomIcon('static/photo/homme.png')).add_to(m)
         
         m = m._repr_html_()
         rr=noticli()
         cont = {
       
         # 'destination': onj ,
          #'form':form,
          'map' :m,                                                                                             
          'counttt':counttt,
          'gg':b,
          'ff':rr
        }
         return render(request, 'pages/chofo.html',cont)
def index(request):
   #id_client=request.session['member_id']
      
      res=requests.get('https://ipinfo.io')
      data=res.json()
      location = data['loc'].split(',')
      lat = float(location[0])
      lng = float(location[1]) 
         #  form=MeasurementModelForm(request.POST or None)

      re="SELECT * FROM `pages_orderchauffeur` where id"
      cur.execute(re)
      data=cur.fetchall()             
    # initial folium map   
      m = folium.Map(width=1495,height=660, location=[lat, lng], zoom_start=14)
    # location marker       
      for i in data: 
          folium.Marker([i[8], i[9]], tooltip='click here for more', popup="hhhhh",
           icon=folium.features.CustomIcon('static/photo/taxi.ico')).add_to(m)
                               
    
  
       
      m=m._repr_html_()
      return  render(request, 'pages/index.html',{'m':m})

def interface1(request):

   return render(request, 'pages/interface1.html')

def fourmulaireChauffeur(request):
   
   if request.method=='POST' and 'btnf1' in request.POST:
      form1=chauffeurForm(request.POST,request.FILES)
      if form1.is_valid():
          form1.save()
          message="bonne enregistrement continue le taxi ...."
   else:
      form1=taxiForm()
   if request.method=='POST':
      form2=taxiForm(request.POST,request.FILES)
      if form2.is_valid():
        form2.save()
        
   else:
      form2=taxiForm()
      
     
   return render(request, 'pages/fourmulaireChauffeur.html',{'form':form1,})

def interfaceClient(request):
    if request.method=='POST':    
        user=request.POST['email']
        passw=request.POST['password']
        cur.execute("SELECT * FROM `pages_client`")
        data=cur.fetchall()
        
        con=None
        c=0
        b=0
        h=0
        for i in data:
         if i[3]==user and i[4]==passw :                  
           c=1
           h=i[0]
           b=client.objects.get(id=i[0])
           con={'m':b,
                            }
            
             

        if c==1:
             request.session['member_id'] =h
             return redirect('main')

        else:
         return render(request, 'pages/interfaceClient.html')

    else:
         return render(request, 'pages/interfaceClient.html')
          
def InterfaceChauffeur(request):

     if request.method=='POST' and 'btncnxch' in request.POST:
        user=request.POST['email']
        passw=request.POST['password']
        cur.execute("SELECT * FROM `pages_chauffeur`")
        data=cur.fetchall()
        
        con=None
        c=0
        b=0
        h=0
        for i in data:
         if i[4]==user and i[6]==passw :
           c=1
           h=i[0]
           b=chauffeur.objects.get(id=i[0])
           con={'m':b,
           }
            
             

        if c==1:
             request.session['chofo_id'] =h
             return redirect('chofo')

        else:
         return render(request, 'pages/InterfaceChauffeur.html',{'msg':"email or password incorrect"})

     else:
         return render(request, 'pages/InterfaceChauffeur.html')

def fourmulaireClient(request):
    if request.method=='POST':
      form=clientForm(request.POST,request.FILES)
      form1 = User(username=request.POST['email'],password=request.POST['password'])
      form1.save()
      if form.is_valid() :
         
         form.save()
      return HttpResponse('hello')
    else:
     form=clientForm()
     return render(request, 'pages/fourmulaireClient.html',{'form':form,})
 
def compteclient(request):
       destination = None
       m =map() 
       con={ 'map':m}
       return render(request, 'pages/compteclient.html',con)
def main(request):
         cont=None
         m=None
         nmb=None;
         gg=request.session['member_id']
         kk=request.session['chofo_id']
         noticho=orderchauffeur.objects.filter(id_client=gg)
         if  noticho is not None:
            noticho=orderchauffeur.objects.filter(id_client=gg)
            if  noticho is not None:
                 nmb=noticho.count()
         else:
                 nmb=0

         b=client.objects.get(id=gg)
       #  onj=Measurement.objects.get(id=1)
         res=requests.get('https://ipinfo.io')
         data=res.json()
         location = data['loc'].split(',')
         lat =32.3492# float(location[0])
         lng =-6.3458# float(location[1])
         re="SELECT * FROM `pages_orderchauffeur`"
         cur.execute(re)
         data=cur.fetchall()  
         nom=None
    # initial folium map
         m = folium.Map(width=1495,height=620, location=[lat, lng], zoom_start=14)
    # location marker
         folium.Marker([lat, lng], tooltip='C est votre position',
         icon=folium.features.CustomIcon('static/photo/homme.png')).add_to(m)
         la=None       
         ln=None 
         for i in data:  
            la=i[8]
            ln=i[9]
            nn=i[1]+" "+i[6]
            ttg="Tele:"+i[2]
            folium.Marker([la, ln], tooltip=nn, popup=ttg,
            icon=folium.features.CustomIcon('static/photo/taxi.ico')).add_to(m)
         
         
         
         m = m._repr_html_()

         if request.method=='POST' and 'btnsub' in request.POST:
               form=CmdForm(request.POST or None)
               if form.is_valid():
                 instance = form.save(commit=False)
                 instance.location =form.cleaned_data.get('location')
                 instance.destination=form.cleaned_data.get('destination')
                 instance.profilClient=form.cleaned_data.get('profilClient')
                 instance.nomcl=form.cleaned_data.get('nomcl')
                 instance.prenomcl=form.cleaned_data.get('prenomcl')
                 instance.nbrplace=form.cleaned_data.get('nbrplace')
                 instance.id_client=gg
                 instance.distance = 3455 
                 instance.lat=lat
                 instance.lng=lng
                 instance.save()
            

        
         vv=notich()
         cont = {
         # 'destination': onj ,
         #'form':form,
         'map':m,
         'g':vv,  
          'gg':b,
          'coun':nmb
         }
   
         return render(request, 'pages/main.html',cont)
def base(request):
    return render(request, 'base.html')
def notificationversclient(request):
   if request.method=='POST' and 'Confirmer' in request.POST:
      form2=ChofoChoisirForm(request.POST)
      if form2.is_valid():
          form2.save()

          
   count=None
   id_client=request.session['member_id']
   notifi=orderchauffeur.objects.filter(id_client=id_client)
   if notifi is not None:
      count={'pro':notifi}
   
   return render(request, 'pages/notificationversclient.html',count)
def dachborde(request):
    cur.execute("SELECT cmd.profilClient,cmd.nomcl,cmd.prenomcl,cmd.location,cmd.destination,cmd.nbrplace,ord.id,ch.id,cmd.id FROM `pages_chofochoisir` ch,`pages_orderchauffeur` ord,`pages_commande` cmd where ch.id_orderch=ord.id and ord.id_Commande=cmd.id")
    data=cur.fetchall()   
    idchofor=request.session['chofo_id']
    b=chauffeur.objects.get(id=idchofor) 
    count={'obj':data,'chofo':b} 
    if request.method=="POST" and "bbb" in request.POST:
        idch=request.POST['idch']    
        idord=request.POST['idord']   
        idcmd=request.POST['idcmd'] 
        c1="DELETE FROM `pages_chofochoisir` WHERE `pages_chofochoisir`.`id` ="+idch+""
        c2="DELETE FROM `pages_orderchauffeur` WHERE `pages_orderchauffeur`.`id` ="+idord+""
        c3="DELETE FROM `pages_commande` WHERE `pages_commande`.`id` ="+idcmd+""
        cur.execute(c1)
        conn.commit()
        cur.execute(c2) 
        conn.commit()
        cur.execute(c3) 
        conn.commit()
       
        
                   
      
        return render(request, 'pages/dachborde.html',count)


    else:
     return render(request, 'pages/dachborde.html',count)
def map_directions(request):

   return render(request, 'pages/map_directions.html')
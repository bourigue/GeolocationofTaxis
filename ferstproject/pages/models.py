from django.db import models
from plyer import notification

from django.db.models.deletion import CASCADE
class client(models.Model):
    profile=models.FileField(upload_to='profilClient')
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
                                                       
 
    

class chauffeur(models.Model):
    profile=models.FileField(upload_to='profilCheuffaur')
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    tele=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    mtrc=models.CharField(max_length=50)
    def __str__(self):
      return self.mtrc

class taxi(models.Model):
    cni=models.ImageField(upload_to='cni')
    taxi=models.ImageField(upload_to='taxi')
    permi=models.ImageField(upload_to='permi')
    mtrc=models.CharField(max_length=50)

   
class clientt():
    profile=models.FileField(upload_to='profilClient')
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)



class file_upload(models.Model):
    file_name=models.CharField(max_length=133)
    my_file=models.FileField(upload_to='profilClientt')

    def __str__(self):
            return self.name

class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    id_client=models.CharField(max_length=200)
    def notofyMe(location, destination):
     notification.notify(
    title = location,
    message = destination,
    app_icon=None,
    timeout=10,
    
    )   
    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"

class orderchauffeur(models.Model):
      nom=models.CharField(max_length=200)
      prenom=models.CharField(max_length=200)
      tele=models.CharField(max_length=200)
      id_client=models.CharField(max_length=200)
      id_chofo=models.CharField(max_length=200)
      id_Commande=models.CharField(max_length=200)
      profilCh=models.CharField(max_length=200)
      lat=models.CharField(max_length=200)
      lng=models.CharField(max_length=200)

class Commande(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    id_client=models.CharField(max_length=200)  
    profilClient= models.CharField(max_length=200)  
    nomcl=models.CharField(max_length=200)
    prenomcl=models.CharField(max_length=200)
    lat=models.CharField(max_length=200)
    lng=models.CharField(max_length=200)
    nbrplace=models.CharField(max_length=200)

class ChofoChoisir(models.Model):
      id_client=models.CharField(max_length=200)
      id_chofo=models.CharField(max_length=200)
      id_orderch=models.CharField(max_length=200)
      
        
class finalcmd(models.Model):
        profileclient=models.CharField(max_length=200)
        nomclient=models.CharField(max_length=200)
        prenomclient=models.CharField(max_length=200)
        location=models.CharField(max_length=200)
        destination=models.CharField(max_length=200)
        nbrplace=models.CharField(max_length=200)
        idcmd=models.CharField(max_length=200)
        idord=models.CharField(max_length=200)



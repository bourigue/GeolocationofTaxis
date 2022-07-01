from django.forms import ModelForm, fields
from pages.models import client,chauffeur,taxi,Measurement,orderchauffeur,Commande,ChofoChoisir,finalcmd
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class clientForm(ModelForm):
    class  Meta:
       model=client
       fields=['profile','nom','prenom','email','password']

class chauffeurForm(ModelForm):       
      class  Meta:
       model=chauffeur
       fields=['profile','nom','prenom','tele','email','password','mtrc']
       
class taxiForm(ModelForm):       
      class  Meta:
       model=taxi
       fields=['cni','taxi','permi','mtrc']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['email', 'password']

class arderchofo(ModelForm):       
      class  Meta:
       model=orderchauffeur
       fields=['nom','prenom','tele','id_client','id_chofo','id_Commande','profilCh','lat','lng']
     

class CmdForm(ModelForm):       
      class  Meta:
       model=Commande
       fields=['location','destination','profilClient','nomcl','prenomcl','nbrplace']

class ChofoChoisirForm(ModelForm):       
      class  Meta:
       model=ChofoChoisir
       fields=['id_client','id_chofo','id_orderch',]

class finalcmdForm(ModelForm):       
      class  Meta:
       model=finalcmd
       fields=['profileclient','nomclient','prenomclient','location','destination','nbrplace','idcmd','idord']
    
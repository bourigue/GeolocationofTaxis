from django.contrib import admin
from .models import client,chauffeur,finalcmd,taxi,file_upload,Measurement,orderchauffeur,Commande,ChofoChoisir
admin.site.register(client)
admin.site.register(chauffeur)
admin.site.register(taxi)
admin.site.register(file_upload)
admin.site.register(Measurement)
admin.site.register(orderchauffeur)
admin.site.register(Commande)
admin.site.register(ChofoChoisir)
admin.site.register(finalcmd)

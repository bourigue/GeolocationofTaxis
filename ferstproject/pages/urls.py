from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path,include
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('interface1',views.interface1,name='interface1'),
    path('fourmulaireChauffeur',views.fourmulaireChauffeur,name='fourmulaireChauffeur'),
    path('interfaceClient',views.interfaceClient,name='interfaceClient'),
    path('InterfaceChauffeur',views.InterfaceChauffeur,name='InterfaceChauffeur'),
    path('fourmulaireClient',views.fourmulaireClient,name='fourmulaireClient'),
    path('compteclient',views.compteclient,name='compteclient'),
    path('main',views.main,name='main'),
    path('base',views.base,name='base'),
    path('chofo',views.chofo,name='chofo'),
    path('notificlient',views.notificlient,name='notificlient'),
    path('notificationversclient',views.notificationversclient,name='notificationversclient'),
    path('dachborde',views.dachborde,name='dachborde'),
    path('map_directions',views.map_directions,name='map_directions'),

]
                  
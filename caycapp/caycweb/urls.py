from django.urls import path
from . import views
 

urlpatterns = [ path('', views.home, name='home'),
                path('missionandvision', views.missionandvision, name='missionandvision'),
                path('housefellow', views.housefellow, name='housefellow'),
                path('mediaresources', views.mediaresources, name='mediaresources'),
                path('youthdiary', views.youthdiary, name='youthdiary'),
                path('testimony', views.testimony, name='testimony'), 
                path('firsttimer', views.firsttimer, name='firsttimer'),
                path('altarcall', views.altarcall, name='altarcall'),
                path('onlinegiving', views.onlinegiving, name='onlinegiving'),
                path('contact', views.contact, name='contact'),
                path('success', views.success, name='success'),

] 

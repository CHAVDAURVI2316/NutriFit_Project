from django.urls import path

from . import views

urlpatterns = [
    path('', views.nindex, name='nindex'), 
    path('nlogin', views.nlogin, name='nlogin'),
    path('nlogout', views.nlogout, name='nlogout'),
    path('nprofile', views.nprofile, name='nprofile'),
    path('npending', views.npending, name='npending'),
    path('napproved', views.napproved, name='napproved'),
    path('ncancel', views.ncancel, name='ncancel'), 
    path('nconsult', views.nconsult, name='nconsult'),
    path('nconsultreport', views.nconsultreport, name='nconsultreport'),
    path('nappointmentreport', views.nappointmentreport, name='nappointmentreport'),
    path('naddconsult', views.naddconsult, name='naddconsult'),
    path('nuser', views.nuser, name='nuser'),
    path('nnutritionist', views.nnutritionist, name='nnutritionist'),
    path('npconsult', views.npconsult, name='npconsult'),
    path('npappointment', views.npappointment, name='npappointment'),
    path('nspecialization', views.nspecialization, name='nspecialization'),
    path('nfeedback', views.nfeedback, name='nfeedback'),


    ]


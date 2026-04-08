from django.urls import path

from . import views

urlpatterns = [
    path('', views.uindex, name='uindex'), 
    path('contactus', views.ucontactus, name='ucontactus'),    
    path('aboutus', views.uaboutus, name='uaboutus'),   
    path('appointment', views.uappointment, name='uappointment'),  
    path('umyappointment', views.umyappointment, name='umyappointment'),  
    path('ulogin', views.ulogin, name='ulogin'),      
    path('logout', views.logout, name='logout'),
    path('usignup', views.usignup, name='usignup'),      
    path('unsignup', views.unsignup, name='unsignup'),      
    path('uprofile', views.uprofile, name='uprofile'),  
    path('uforgotpassword', views.uforgotpassword, name='uforgotpassword'),         
    path('unforgotpassword', views.unforgotpassword, name='unforgotpassword'),   
    path('uconsult', views.uconsult, name='uconsult'),  
    path('uourteam', views.uourteam, name='uourteam'),
    path('resendotp', views.resendotp, name='resendotp'),
    path('nresendotp', views.nresendotp, name='nresendotp'),
    path('uprivacypolicy', views.uprivacypolicy, name='uprivacypolicy'),
    path('uteamdetails', views.uteamdetails, name='uteamdetails'),
    path('upayment', views.upayment, name='upayment'),
    path('uapayment', views.uapayment, name='uapayment'),
    path('umypayment', views.umypayment, name='umypayment'),
    ]






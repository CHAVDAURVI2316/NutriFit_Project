from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('specialization', views.specialization, name='specialization'), 
    path('specializationedit', views.specializationedit, name='specializationedit'),
    path('user', views.user, name='user'),
    path('feedback', views.feedback, name='feedback'),
    path('nutritionist', views.nutritionist, name='nutritionist'),
    path('consult', views.consult, name='consult'), 
    path('appointment', views.appointment, name='appointment'), 
    path('pappointment', views.pappointment, name='pappointment'),
    path('pconsult', views.pconsult, name='pconsult'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('userreport', views.userreport, name='userreport'),
    path('nutritionistreport', views.nutritionistreport, name='nutritionistreport'),
    path('consultreport', views.consultreport, name='consultreport'),
    path('appointmentreport', views.appointmentreport, name='appointmentreport'), 
    path('pending', views.pending, name='pending'),
    path('approved', views.approved, name='approved'),
    path('cancel', views.cancel, name='cancel'), 


    ]

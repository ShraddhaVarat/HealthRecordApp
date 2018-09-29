from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'HealthRecord'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login, name='login'),
	path('signup/', views.signup, name='signup'),
	path('hospital/', views.hospital, name='hospital'),
	path('hprofile/', views.hprofile, name='hospitalp'),
	path('patient/', views.patient, name='patient'),
	path('pprofile/', views.pprofile, name='patientp'),
	path('doctor/', views.doctor, name='doctor'),
	path('dprofile/', views.dprofile, name='doctorp'),
	path('pharmacist/', views.pharmacist, name='pharmacist'),
	path('phprofile/', views.phprofile, name='pharmacistp'),

]

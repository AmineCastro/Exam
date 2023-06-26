from django.urls import path
from . import views
urlpatterns = [

    path('', views.bienv, name= 'bienv'),
    path('acceuil.html', views.acceuil, name='acceuil'),
    path('infractions', views.infractions, name='infractions'),
    path('form1/<int:id_exploitant>/', views.form1, name='form1')


]








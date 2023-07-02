from django.urls import path
from . import views
urlpatterns = [

   
    path('', views.bienv, name= 'bienv'),
    path('bienv', views.bienv, name= 'bienv'),
    path('acceuil.html', views.acceuil, name='acceuil'),
    path('infractions', views.infractions, name='infractions'),

   path('liste_exploitants/', views.acceuil, name='liste_exploitants'),

    


     #exploitant
    
    path('create/', views.exploi_create, name='exploi_create'),
    path('exploi/delete/<int:id_exploitant>/', views.exploi_delete, name='exploi_delete'),
    path('exploitants/<int:id_exploitant>/edit/', views.exploi_edit, name='exploi_edit'),


    #infrac
  
  path('fract', views.infrac_create, name='infrac_create'),
  path('infracs/delete/<int:id_infraction>/', views.infrac_delete, name='infrac_delete'),

  path('infracs/edit/<int:id_infraction>/', views.infrac_edit, name='infrac_edit'),
   
   path('infractions/', views.infrac_list, name='infrac_list'),
   
   
]










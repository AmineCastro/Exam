from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Exploi(models.Model):

   Id_exploitant = models.AutoField(primary_key=True)
   Nom_complet = models.CharField(max_length=40)
   CIN = models.CharField(max_length=100)
   Adresse = models.CharField(max_length=100)
   Tele = models.CharField(max_length=100)
   
   def __str__(self):
      return self.Nom_complet

class Infrac(models.Model):

   
   Id_infraction = models.AutoField(primary_key=True)
   Nature = models.CharField(max_length=100)
   Resiliation = models.CharField(max_length=100)
   Inscription_date = models.DateTimeField(blank=True, null=True)
   Amende = models.CharField(max_length=100)
   Emprisonement = models.CharField(max_length=100)
   Id_exploitant = models.ForeignKey(Exploi, on_delete=models.CASCADE)

   def __str__(self):
        return str(self.Id_infraction)
   
  




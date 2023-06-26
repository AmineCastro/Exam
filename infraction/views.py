from django.shortcuts import render
from .models import Exploi, Infrac

# Create your views here.



def acceuil(request):
    explois = Exploi.objects.all()
    return render(request, 'infraction/acceuil.html', {'explois': explois})


#def form1(request, id_exploitant):
    #exploi = Exploi.objects.get(pk=id_exploitant)
    #infracs = Infrac.objects.all()
    #return render(request, 'form1.html', {'infracs': infracs})

def form1(request, id_exploitant):
    Exploi = Exploi.objects.get(Id_exploitant=id_exploitant)
    Infracs = Infrac.objects.filter(Id_exploitant=exploi)
    return render(request, 'form1.html', {'Exploi': Exploi, 'Infracs': Infracs})

def infractions(request):
    Infracs = Infrac.objects.all()
    return render(request, 'infraction/infr.html', {'Infracs': Infracs})




def bienv(request):
    explois = Exploi.objects.all()
    return render(request, 'infraction/bienv.html')








from .models import Exploi, Infrac

from django.shortcuts import render, redirect

from .forms import ExploiForm
from .forms import InfracForm

from .models import Infrac
from .models import Exploi

from django.shortcuts import get_object_or_404



# Create your views here.




def acceuil(request):
    explois = Exploi.objects.all()
    return render(request, 'infraction/acceuil.html', {'explois': explois})


#def form1(request, id_exploitant):
    #exploi = Exploi.objects.get(pk=id_exploitant)
    #infracs = Infrac.objects.all()
    #return render(request, 'form1.html', {'infracs': infracs})




def infractions(request):
    Infracs = Infrac.objects.all()
    return render(request, 'infraction/infrac_list.html', {'Infracs': Infracs})


def bienv(request):
    explois = Exploi.objects.all()
    return render(request, 'infraction/bienv.html')



def add_exploitant(request):
    if request.method == 'POST':
        nom_complet = request.POST['nom_complet']
        cin = request.POST['cin']
        adresse = request.POST['adresse']
        tele = request.POST['tele']
        
        exploitant = Exploi(Nom_complet=nom_complet, CIN=cin, Adresse=adresse, Tele=tele)
        exploitant.save()
        
        return redirect('liste_exploitants')  # Rediriger vers la liste des exploitants après l'ajout
        
    return render(request, 'ajouter.html')









### exploitants !



def exploi_delete(request, id_exploitant):
    exploi = get_object_or_404(Exploi, Id_exploitant=id_exploitant)

    if request.method == 'POST':
        # Effectuer l'action de suppression
        exploi.delete()
        return redirect('liste_exploitants')  # Rediriger vers la page de liste des exploitants après la suppression

    return render(request, 'exploi_delete.html', {'exploi': exploi})

def exploi_edit(request, id_exploitant):
    exploi = get_object_or_404(Exploi, Id_exploitant=id_exploitant)
    
    if request.method == 'POST':
        form = ExploiForm(request.POST, instance=exploi)
        if form.is_valid():
            form.save()
            return redirect('liste_exploitants')
    else:
        form = ExploiForm(instance=exploi)
    
    return render(request, 'exploi_edit.html', {'form': form})

def exploi_create(request):
    if request.method == 'POST':
        form = ExploiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acceuil')
    else:
        form = ExploiForm()
    return render(request, 'exploi_create.html', {'form': form})

## infra


def infrac_create(request):
    if request.method == 'POST':
        form = InfracForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infractions')
    else:
        form = InfracForm()
    return render(request, 'infrac_create.html', {'form': form})



def infrac_list(request):
    infracs = Infrac.objects.all()
    context = {'infracs': infracs}
    return render(request, 'infraction/infrac_list.html', context)


def infrac_delete(request, id_infraction):
    infrac = Infrac.objects.get(Id_infraction=id_infraction)
    infrac.delete()
    return redirect('infractions')


def infrac_edit(request, id_infraction):
    infrac = Infrac.objects.get(Id_infraction=id_infraction)

    if request.method == 'POST':
        form = InfracForm(request.POST, instance=infrac)
        if form.is_valid():
            form.save()
            return redirect('infractions')

    else:
        form = InfracForm(instance=infrac)

    return render(request, 'infrac_edit.html', {'form': form})

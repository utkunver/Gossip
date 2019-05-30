from django.shortcuts import render,Http404,redirect
from .models import Profil
from icerik.models import icerik
from django.contrib.auth.models import User
from django.shortcuts import render
from kullanici.forms import EditProfilFrom
from .forms import ProfilFrom

def profil_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        username_id = request.user.id
        iceriks = icerik.objects.filter(icerik_user_id=username_id)
        posts = User.objects.values().filter(username=username).get()
        duzen = Profil.objects.filter(profil_user_id=username_id)
        isteks = Profil.objects.values().filter(profil_user_id=username_id).get
        return render(request, 'profil/profil.html',{'posts':posts,'duzen':duzen,'isteks':isteks,'iceriks':iceriks})
    else:
        return Http404()

def duzenle_view(request):
    if request.user.is_authenticated:
        form = EditProfilFrom(request.POST, instance=request.user)
        profil_form = ProfilFrom(request.POST or None, request.FILES or None)
        username = request.user.username
        username_id = request.user.id
        posts = User.objects.values().filter(username=username).get()
        duzen = Profil.objects.filter(profil_user_id=username_id)
        isteks = Profil.objects.values().filter(profil_user_id=username_id).get
        profil_form.profil_user = username_id
        args = {'form': form, 'posts': posts, 'duzen': duzen, 'isteks': isteks,'profil_form':profil_form}
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('profil')
            elif profil_form.is_valid():
                profil_form.save()
                return redirect('profil')
            else:
                profil_form = ProfilFrom(request.POST or None, request.FILES or None)
                form = EditProfilFrom(instance=request.user)
                args = {'form':form,'duzen':duzen,'profil_form':profil_form}
            return render(request,'profil/düzenle.html',args)
        return render(request, 'profil/düzenle.html',args)
    else:
        return Http404()


def other_view(request):

    username = request.user.username
    username_id = request.user.id
    iceriks = icerik.objects.filter(icerik_user_id=username_id)
    posts = User.objects.values().filter(username=username).get()
    duzen = Profil.objects.filter(profil_user_id=username_id)
    isteks = Profil.objects.values().filter(profil_user_id=username_id).get
    return render(request, 'profil/profil.html',{'posts':posts,'duzen':duzen,'isteks':isteks,'iceriks':iceriks})

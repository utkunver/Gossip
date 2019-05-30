from django.shortcuts import render,get_list_or_404
from .models import AnaSayfa,hakkinda
from icerik.models import icerik
from django.contrib.auth.models import User

def home_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})

def edebiyat_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.filter(icerik_kategori='9')
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})

def gossipozel_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.filter(icerik_kategori='2') or icerik.objects.filter(icerik_kategori='4')
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})

def gundem_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})

def spor_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.filter(icerik_kategori='7')
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})

def sinema_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.filter(icerik_kategori='8')
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa.html',
                      {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa.html', {'categories': categories, 'posts': posts})
def hakkimizda_view(request):
    categories = AnaSayfa.objects.values()
    hakkimizda = hakkinda.objects.values()
    posts = icerik.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa/hakkimizda.html', {'categories': categories, 'select_tip': comment, 'posts': posts,'hakkimizda': hakkimizda})
    return render(request, 'anasayfa/hakkimizda.html', {'categories': categories, 'posts': posts,'hakkimizda': hakkimizda})
def iletisim_view(request):
    categories = AnaSayfa.objects.values()
    posts = icerik.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa/iletisim.html', {'categories': categories, 'select_tip': comment, 'posts': posts})
    return render(request, 'anasayfa/iletisim.html', {'categories': categories, 'posts': posts})
def detail_view(request,id):
    categories = AnaSayfa.objects.values()
    posts = get_list_or_404(icerik,id=id)
    comment = None
    context = {
        'form':posts
    }
    if request.user.is_authenticated:
        username = request.user.username
        try:
            comment = User.objects.get(is_superuser=True, username=username)
        except User.DoesNotExist:
            comment = None
        return render(request, 'anasayfa/detail.html',
                      {'categories': categories, 'posts': posts, 'select_tip': comment})

    return render(request, 'anasayfa/detail.html', {'categories': categories,'posts': posts, 'select_tip': comment})


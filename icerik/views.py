from django.shortcuts import render,Http404
from anasayfa.models import AnaSayfa
from .forms import icerikFrom
from django.contrib import messages

def icerikyaz_view(request):

    if not request.user.is_authenticated:
        return Http404() # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
    categories = AnaSayfa.objects.values()
    form = icerikFrom(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.icerik_user = request.user
        post.save()
        messages.success(request,'Başarılı Bir Şekilde Oluşturdunuz.')
    context = {
        'form' : form
    }
    return render(request, 'icerik/icerikyaz.html', context, {'categories': categories})

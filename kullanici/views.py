from django.shortcuts import render,redirect,reverse
from anasayfa.models import AnaSayfa
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def forgot_view(request):
    categories = AnaSayfa.objects.values()
    return render(request, 'kullanici/forgot.html', {'categories': categories})
def login_view(request):
    categories = AnaSayfa.objects.values()
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        try:
            comment = User.objects.get(is_superuser=True,username=username)
        except User.DoesNotExist:
            comment = None
        return redirect('anasayfa')
    return render(request, 'kullanici/login.html', {'categories': categories,'form':form})

def register_view(request):
    categories = AnaSayfa.objects.values()
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        user.save()
        new_user = authenticate(username=username, password=password,email=email,first_name=first_name)
        login(request, new_user)
        return redirect('anasayfa')

    return render(request, 'kullanici/register.html', {'categories': categories,'form':form})

def logout_view(request):

    logout(request)
    return redirect('anasayfa')
#
# def update_view(request):
#     categories = AnaSayfa.objects.values()
#     if request.user.is_authenticated:
#         username = request.user.username
#         users = User.objects.values().filter(username=username).get()
#         form = LoginForm(request.POST or None, instance=users)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             login(request, user,backend='django.contrib.auth.backends.ModelBackend')
#             try:
#                 comment = User.objects.get(is_superuser=True,username=username)
#             except User.DoesNotExist:
#                 comment = None
#             return redirect('profil')
#         return render(request, 'profil/profil.html', {'categories': categories,'form':form})
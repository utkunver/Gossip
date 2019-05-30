from django.urls import path

from .views import profil_view,duzenle_view
urlpatterns = [

    path('', profil_view, name='profil'),
    path('duzenle/', duzenle_view, name='düzenle'),

]
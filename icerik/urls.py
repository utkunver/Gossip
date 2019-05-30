from django.urls import path

from .views import icerikyaz_view
urlpatterns = [


    path('', icerikyaz_view, name='icerik'),

]
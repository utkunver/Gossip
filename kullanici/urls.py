from django.urls import path

from .views import forgot_view,login_view,register_view,logout_view
urlpatterns = [

    path('forgot/', forgot_view, name='forgot'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
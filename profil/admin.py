from django.contrib import admin

from .models import Profil

class ProfilAdmin(admin.ModelAdmin):

    list_display = ['profil_user']
    search_fields = ['profil_user']
    class Meta:
        model = Profil
admin.site.register(Profil,ProfilAdmin)

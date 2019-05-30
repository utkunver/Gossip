from django.contrib import admin
from .models import icerik

class IcerikAdmin(admin.ModelAdmin):

    list_display = ['icerik_user','icerik_kategori','icerik_bas','icerik_tarih']
    list_filter = ['icerik_tarih']
    class Meta:
        model = icerik

admin.site.register(icerik,IcerikAdmin)
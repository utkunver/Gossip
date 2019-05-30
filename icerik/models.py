from django.db import models
from ckeditor.fields import RichTextField
from anasayfa.models import AnaSayfa
from django.urls import reverse

class icerik(models.Model):
    icerik_user = models.ForeignKey('auth.User', related_name="icerik_user", on_delete=models.CASCADE)
    icerik_kategori = models.ForeignKey(AnaSayfa, related_name='icerik_kategori', on_delete=models.CASCADE)
    icerik = RichTextField(verbose_name='içerik')
    icerik_tarih = models.DateTimeField(verbose_name='yayımlama tarihi',auto_now_add=True)
    begeni_say = models.IntegerField(default=0,verbose_name='Begeni Sayisi')
    icerik_bas = models.CharField(max_length=50,verbose_name='icerik_bas')
    icerik_foto = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.icerik
    class Meta:
        db_table = "icerik"

    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})

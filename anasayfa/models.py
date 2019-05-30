from django.db import models
from django.urls import reverse

class AnaSayfa(models.Model):
    kategori_adi = models.CharField(max_length=25, verbose_name='kategori_adi')
    def __str__(self):
        return self.kategori_adi
    class Meta:
        db_table = "Anasayfa"

    def get_absolute_url(self):
        return reverse('kategori', kwargs={'id': self.id})

class iletisim(models.Model):
    adi = models.CharField(max_length=30, verbose_name='adi ve Soyadi')
    konu = models.CharField(max_length=50, verbose_name='konu')
    ileti = models.CharField(max_length=700, verbose_name='ileti')
    def __str__(self):
        return self.adi
    class Meta:
        db_table = "iletisim"
class hakkinda(models.Model):
    hakkinda = models.TextField(verbose_name='hakkinda')
    def __str__(self):
        return self.hakkinda
    class Meta:
        db_table = "hakkinda"

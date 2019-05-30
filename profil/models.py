from django.db import models


class Profil(models.Model):
    profil_user = models.ForeignKey('auth.User', related_name="profil_user", on_delete=models.CASCADE)
    profil_photo = models.ImageField(null=True)
    wall_photo = models.ImageField(null=True)
    slogan = models.CharField(max_length=50, verbose_name='slogan',null=True)
    hakkinda = models.CharField(max_length=200, verbose_name='hakkında',null=True)
    icerik_say = models.IntegerField(default=0,verbose_name='İçerik Sayisi')
    begeni_say = models.IntegerField(default=0,verbose_name='Begeni Sayisi')

    def __str__(self):
        return self.slogan
    class Meta:
        db_table = "Profil"
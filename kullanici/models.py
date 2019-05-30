from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# class Kullanici(models.Model):
#     kullanici_adi = models.CharField(max_length=15, verbose_name='kullanici adi')
#     adi = models.CharField(max_length=50, verbose_name='adi ve Soyadi')
#     sifre = models.CharField(max_length=20, verbose_name='sifre')
#     email = models.CharField(max_length=50, verbose_name='email')
#     tip = models.CharField(max_length=6,verbose_name='tip', null=True)
#     def __str__(self):
#         return self.adi
#     class Meta:
#         db_table = "kullanici"

# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255,unique=True)
#     full_name = models.CharField(max_length=255,blank=True,null=True)
#     active = models.BooleanField(default=True)#login için
#     staff = models.BooleanField(default=False)#editör için
#     admin = models.BooleanField(default=False)#admin için
#
#
#     USERNAME_FIELD = 'email'#username
#     REQUIRED_FIELDS = ['full_name1']
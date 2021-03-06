# Generated by Django 2.1.7 on 2019-05-28 17:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anasayfa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='icerik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icerik', ckeditor.fields.RichTextField(verbose_name='içerik')),
                ('icerik_tarih', models.DateTimeField(auto_now_add=True, verbose_name='yayımlama tarihi')),
                ('begeni_say', models.IntegerField(blank=True, null=True, verbose_name='Begeni Sayisi')),
                ('icerik_bas', models.CharField(max_length=50, verbose_name='icerik_bas')),
                ('icerik_foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('icerik_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icerik_kategori', to='anasayfa.AnaSayfa')),
                ('icerik_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icerik_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'icerik',
            },
        ),
    ]

from django import forms
from .models import Profil


class ProfilFrom(forms.ModelForm):

    class Meta:
        model = Profil
        fields = [
            'profil_user',
            'profil_photo',
            'wall_photo',
            'slogan',
            'hakkinda',
                  ]

    def __init__(self, *args, **kwargs):
        super(ProfilFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# class DuzenleFrom():
#     class Meta:
#         model = Profil
#         fields = [
#             'profil_photo',
#             'wall_photo',
#             'slogan',
#             'hakkinda',
#                   ]
#
#     def __init__(self, *args, **kwargs):
#         super(DuzenleFrom, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

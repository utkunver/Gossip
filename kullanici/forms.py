from django import forms
# from .models import Kullanici
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='Adı ve Soyadı')
    email = forms.EmailField(max_length=100,label='email')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password1',
            'email',
            'first_name',
        ]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        return password1

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EditProfilFrom(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
        ]

    def __init__(self, *args, **kwargs):
        super(EditProfilFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
    #     super(EditProfilFrom, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


# class LoginForm(forms.ModelForm):

#     class Meta:
#         model = Kullanici
#         fields = [
#             'kullanici_adi',
#             'sifre',
#         ]
#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
#
#
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Kullanici
#         fields = [
#             'kullanici_adi',
#             'sifre',
#             'adi',
#             'email',
#             # 'tip',
#                   ]
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'


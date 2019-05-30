from django import forms
from .models import icerik
from ckeditor.widgets import CKEditorWidget


class icerikFrom(forms.ModelForm):

    class Meta:
        model = icerik
        fields = [
            'icerik_bas',
            'icerik',
            'icerik_kategori',
            'icerik_foto',
                  ]

    def __init__(self, *args, **kwargs):
        super(icerikFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'




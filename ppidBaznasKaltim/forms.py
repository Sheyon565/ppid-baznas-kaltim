from django import forms 
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import ArtikelBaznas
        
class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBaznas
        fields = ['judul', 'konten', 'gambar', 'status']
        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'konten': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"},
                  config_name="extends"
              ),
        }
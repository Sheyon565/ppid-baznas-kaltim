from django import forms 
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import ArtikelBaznas, Pimpinan
    
class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBaznas
        fields = ['judul', 'konten', 'gambar', 'status']
        # Perhatikan urutan fields, harus sesuai dengan yang ingin ditampilkan di form

        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan judul artikel', # Opsional: Tambahkan placeholder
                    'required': True # Ini sudah ada, tapi penting untuk diketahui
                }
            ),
            'konten': CKEditor5Widget(config_name='extends'),
            # Opsional: Menambahkan widget untuk 'gambar' dan 'status'
            # Jika 'gambar' adalah ImageField atau FileField
            'gambar': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file', # Bootstrap 5 class for file inputs
                    'accept': 'image/*', # Opsional: Batasi hanya file gambar
                }
            ),
            # Jika 'status' adalah CharField dengan choices atau BooleanField
            'status': forms.Select( # Contoh jika status adalah CharField dengan choices
                attrs={
                    'class': 'form-control',
                }
            )
            # Atau jika 'status' adalah BooleanField
            # 'status': forms.CheckboxInput(
            #     attrs={
            #         'class': 'form-check-input',
            #     }
            # )
        }

class PimpinanForm(forms.ModelForm):
    class Meta:
        model = Pimpinan
        fields = ['nama', 'foto', 'deskripsi']
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Nama Pimpinan'
                }
            ),
            'deskripsi': CKEditor5Widget(config_name='extends'),
        }
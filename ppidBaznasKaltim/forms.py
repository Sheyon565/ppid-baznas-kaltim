from django import forms 
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import ArtikelBaznas, Pimpinan, User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()
    
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
        
            'gambar': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file', # Bootstrap 5 class for file inputs
                    'accept': 'image/*', # Opsional: Batasi hanya file gambar
                }
            ),
            'status': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                    }
                ),

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

class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(
        required=False,
        label="Password Baru",
        widget=forms.PasswordInput,
        help_text="Kosongkan jika tidak ingin mengganti password."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']
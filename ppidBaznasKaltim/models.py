from django.db import models

from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field

class ArtikelBaznas(models.Model):
    judul = models.CharField(max_length=200)
    konten = CKEditor5Field('Text', config_name='extends')
    gambar = models.ImageField(upload_to="artikel", blank=True, null=True)
    status = models.BooleanField(default=False) # Jika True, maka nanti akan muncul ditampilkan
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.judul
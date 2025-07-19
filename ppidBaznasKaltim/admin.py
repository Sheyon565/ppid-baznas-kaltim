from django.contrib import admin
from .models import ArtikelBaznas

# Register your models here.
class ArtikelAdmin(admin.ModelAdmin):
    list_display = [ 'judul', 'created_at', 'created_by']
    search_fields = ['judul']
admin.site.register(ArtikelBaznas, ArtikelAdmin)
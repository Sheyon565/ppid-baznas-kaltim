from django.contrib import admin
from .models import ArtikelBaznas, Pimpinan

# Register your models here.
class ArtikelAdmin(admin.ModelAdmin):
    list_display = [ 'judul', 'created_at', 'created_by']
    search_fields = ['judul']
admin.site.register(ArtikelBaznas, ArtikelAdmin)

@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ('nama',)
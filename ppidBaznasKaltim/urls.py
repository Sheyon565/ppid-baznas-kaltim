from django.urls import path
from . import views

app_name = 'ppid'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('informasi-publik/', views.InformasiPublikView.as_view(), name='informasi_publik'),
    path('layanan-informasi/', views.LayananInformasiView.as_view(), name='layanan_informasi'),
    path('regulasi/', views.regulasi, name='regulasi'),
    path('laporan/', views.LaporanView.as_view(), name='laporan'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]
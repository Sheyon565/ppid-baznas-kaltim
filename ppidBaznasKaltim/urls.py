from django.urls import path
from . import views

app_name = 'ppid'

urlpatterns = [
    #### Admin ####
    path('admin-users/', views.user_list, name='user_list'),
    path('admin-users-add/', views.user_create, name='user_create'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('akun-edit/', views.edit_akun, name='edit_akun'), 
    path('admin-login/', views.login_view, name='login'),
    path('admin-logout/', views.logout_view, name='logout'),
    
    path('artikel/', views.artikel_list, name='artikel_list'),
    path('artikel/<int:pk>/', views.detail_artikel, name='artikel_detail'),
    path('artikel/tambah/', views.artikel_create, name='artikel_create'),
     # ArtikelBaznas
    path('admin-artikel/', views.admin_artikel_list, name='admin_artikel_list'),
    path('artikel-tambah/', views.admin_artikel_tambah, name='admin_artikel_tambah'),
    path('artikel/edit/<int:id_artikel>/', views.admin_artikel_update, name='admin_artikel_update'),
    path('artikel/hapus/<int:id_artikel>/', views.admin_artikel_delete, name='admin_artikel_delete'),

    # Pimpinan
    path('pimpinan/', views.admin_pimpinan_list, name='admin_pimpinan_list'),
    path('pimpinan/tambah/', views.admin_pimpinan_tambah, name='admin_pimpinan_tambah'),
    path('pimpinan/edit/<int:id_pimpinan>/', views.admin_pimpinan_update, name='admin_pimpinan_update'),
    path('pimpinan/hapus/<int:id_pimpinan>/', views.admin_pimpinan_delete, name='admin_pimpinan_delete'),
    
    path('', views.HomeView.as_view(), name='home'),
    path('regulasi/', views.regulasi, name='regulasi'),
    path('faq/', views.FAQView, name='faq'),
    
    ##PPID##
    path('profil/', views.profil_view, name='profil'),
     path('struktur-ppid/', views.struktur_ppid, name='struktur_ppid'),
    path('pimpinan/tambah/', views.tambah_pimpinan, name='tambah_pimpinan'),
    path('pimpinan/edit/<int:id>/', views.edit_pimpinan, name='edit_pimpinan'),
    path('visi-misi/', views.visi_misi_view, name='visi_misi'),
    path('tugas-fungsi/', views.Tugas_view, name='tugas_fungsi'),
    
    ### Layanan Informasi ####
    path('layanan-pengaduan/', views.layanan_pengaduan, name='layanan_pengaduan'),
    path('maklumat-pelayanan/', views.maklumat_pelayanan, name='maklumat_pelayanan'),
    path('rekomendasi-laz/', views.rekomendasi_laz, name='rekomendasi_laz'),
    
    ### Informasi Berkala ####
    path('informasi-berkala/', views.informasi_berkala, name='informasi_berkala'),
    path('laz-kabkota/', views.laz_kabkota, name='laz_kabkota'),
    path('alamat-baznas-kaltim/', views.alamat_baznas_jabar, name='alamat_baznas_kaltim'),
    path('struktur-baznas-kaltim/', views.struktur_baznas_jabar, name='struktur_baznas_kaltim'),
    path('kantor-layanan-baznas-kaltim/', views.kantor_layanan_baznas_jabar, name='kantor_layanan_baznas_kaltim'),
    
    ### Informasi Serta Merta ###
    path('informasi-serta-merta/', views.informasi_serta_merta, name='informasi_serta_merta'),
    path('informasi-setiap-saat/', views.informasi_setiap_saat, name='informasi_setiap_saat'),
    
    ### Regulasi ###
    path('informasi-publik/', views.layanan_informasi, name='informasi_publik'),
    path('upz/', views.upz, name='upz'),
]
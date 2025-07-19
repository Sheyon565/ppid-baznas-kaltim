from django.urls import path
from . import views

app_name = 'ppid'

urlpatterns = [
    #### Admin ####
    path('artikel/', views.artikel_list, name='artikel_list'),
    path('artikel/<int:pk>/', views.artikel_detail, name='artikel_detail'),
    path('artikel/tambah/', views.artikel_create, name='artikel_create'),
    
    path('', views.HomeView.as_view(), name='home'),
    path('regulasi/', views.regulasi, name='regulasi'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]
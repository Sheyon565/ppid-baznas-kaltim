from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from .models import ArtikelBaznas
from .forms import ArtikelForms  # Pastikan file forms.py punya ArtikelForms

# ✅ List artikel yang sudah publish
def artikel_list(request):
    artikels = ArtikelBaznas.objects.filter(status=True).order_by('-created_at')
    return render(request, 'Artikel/artikel_list.html', {'artikels': artikels})

# ✅ Detail artikel
def artikel_detail(request, pk):
    artikel = get_object_or_404(ArtikelBaznas, pk=pk, status=True)
    return render(request, 'Artikel/artikel_detail.html', {'artikel': artikel})

# ✅ Form tambah artikel (hanya untuk user login)
@login_required
def artikel_create(request):
    if request.method == 'POST':
        form = ArtikelForms(request.POST, request.FILES)
        if form.is_valid():
            artikel = form.save(commit=False)
            artikel.created_by = request.user
            artikel.save()
            return redirect('artikel_list')  # Sesuaikan dengan nama URL kamu
    else:
        form = ArtikelForms()
    return render(request, 'Artikel/artikel_form.html', {'form': form})

# ✅ Home page
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'PPID Baznas Kaltim',
            'latest_info': ArtikelBaznas.objects.filter(status=True).order_by('-created_at')[:5],
            'contact_info': {
                'alamat': 'Jl. Contoh Alamat No. 123',
                'email': 'info@baznasprovkaltim.or.id',
                'telepon': '(0541) 123456'
            }
        })
        return context

# ✅ Halaman regulasi (statis)
def regulasi(request):
    return render(request, 'regulasi.html')

# ✅ FAQ page
class FAQView(TemplateView):
    template_name = 'ppid/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'FAQ - PPID Baznas Kaltim',
            'faqs': [
                {'pertanyaan': 'Apa itu PPID?', 'jawaban': 'PPID adalah Pejabat Pengelola Informasi dan Dokumentasi.'},
                {'pertanyaan': 'Bagaimana cara mengajukan permohonan informasi?', 'jawaban': 'Isi formulir permohonan informasi di website ini.'}
            ]
        })
        return context

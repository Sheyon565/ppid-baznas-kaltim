from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ArtikelBaznas, Pimpinan
from .forms import ArtikelForms, PimpinanForm, CustomUserChangeForm

def is_admin_or_operator(user):
    return user.is_superuser or user.groups.filter(name='Operator').exists()

### User ###
@login_required
@user_passes_test(is_admin_or_operator)
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin/user_list.html', {'users': users})

# Tambah user
@login_required
@user_passes_test(is_admin_or_operator)
def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ppid:user_list')
    else:
        form = UserCreationForm()
    return render(request, 'admin/user_form.html', {'form': form})

@login_required
def edit_akun(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)  # Penting agar user tidak logout
            user.save()
            return redirect('ppid:user_list')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'admin/edit_akun.html', {'form': form})


#### Admin ####
def is_admin(user):
    return user.is_staff

def login_view(request):
    if request.user.is_authenticated:
        return redirect('ppid:admin_dashboard') 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None and (user.is_staff or user.groups.filter(name='Operator').exists()):
                login(request, user)
                return redirect('ppid:admin_dashboard')
            else:
                messages.error(request, 'Username atau password salah atau Anda tidak punya akses.')
        else:
            messages.error(request, 'Mohon isi username dan password.')

    return render(request, 'admin/admin_login.html')


@login_required
def admin_dashboard(request):
    # Semua user login bisa akses
    artikel_count = ArtikelBaznas.objects.count()
    pimpinan_count = Pimpinan.objects.count()
    artikel_terbaru = ArtikelBaznas.objects.order_by('-created_at')[:5]
    return render(request, 'admin/admin_dashboard.html', {
        'artikel_count': artikel_count,
        'pimpinan_count': pimpinan_count,
        'artikel_terbaru': artikel_terbaru
    })

def logout_view(request):
    logout(request)
    return redirect('ppid:login')

def artikel_list(request):
    artikels = ArtikelBaznas.objects.filter(status=True).order_by('-created_at')
    return render(request, 'Artikel/artikel_list.html', {'artikels': artikels})

def artikel_detail(request, pk):
    artikel = get_object_or_404(ArtikelBaznas, pk=pk, status=True)
    return render(request, 'Artikel/artikel_detail.html', {'artikel': artikel})

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

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ambil artikel yang sudah publish
        artikels = ArtikelBaznas.objects.filter(status=True).order_by('-created_at')[:5]

        context.update({
            'title': 'PPID Baznas Kaltim',
            'artikels': artikels,  # Ganti jadi 'artikels' agar lebih konsisten
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
def FAQView(request):
    return render(request, 'FAQ.html')

## PPID BAznas ###
def profil_view(request):
    pimpinan_list = Pimpinan.objects.all()  # ambil semua data pimpinan
    return render(request, 'PPID/Profil.html', {'pimpinan_list': pimpinan_list})

# Tambah pimpinan
def tambah_pimpinan(request):
    if request.method == 'POST':
        form = PimpinanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('daftar_pimpinan')  # sesuaikan dengan nama url list pimpinan
    else:
        form = PimpinanForm()
    return render(request, 'PPID/form_pimpinan.html', {'form': form, 'title': 'Tambah Pimpinan'})

# Edit pimpinan
def edit_pimpinan(request, id):
    pimpinan = get_object_or_404(Pimpinan, id=id)
    if request.method == 'POST':
        form = PimpinanForm(request.POST, request.FILES, instance=pimpinan)
        if form.is_valid():
            form.save()
            return redirect('daftar_pimpinan')
    else:
        form = PimpinanForm(instance=pimpinan)
    return render(request, 'PPID/form_pimpinan.html', {'form': form, 'title': 'Edit Pimpinan'})

def visi_misi_view(request):
    return render(request, 'PPID/VisiMisi.html')

def Tugas_view(request):
    return render(request, 'PPID/Tugas.html')

#### Layanan Informasi ####
def layanan_pengaduan(request):
    return render(request, 'Layanan Informasi/layanan_pengaduan.html')

def maklumat_pelayanan(request):
    return render(request, 'Layanan Informasi/maklumat_pelayanan.html')

def rekomendasi_laz(request):
    return render(request, 'Layanan Informasi/rekomendasi_laz.html')

### Informasi Publik ###
def informasi_berkala(request):
    return render(request, 'Informasi Publik/berkala.html')

def laz_kabkota(request):
    return render(request, 'Informasi Publik/Berkala/laz_kabkota.html')

def alamat_baznas_jabar(request):
    return render(request, 'Informasi Publik/Berkala/alamat_baznas_kaltim.html')

def struktur_baznas_jabar(request):
    return render(request, 'Informasi Publik/Berkala/struktur_baznas_kaltim.html')

def kantor_layanan_baznas_jabar(request):
    return render(request, 'Informasi Publik/Berkala/kantor_layanan_baznas_kaltim.html')

#### Informasi Serta Merta ####
def informasi_serta_merta(request):
    return render(request, 'Informasi Publik/sertamerta.html')

#### Informasi Setiap Saat
def informasi_setiap_saat(request):
    return render(request, 'Informasi Publik/setiap_saat.html')

#### Regulasi ####
def layanan_informasi(request):
    return render(request, 'Regulasi/layanan_informasi.html')

# === ARTIKEL ===
@login_required
def admin_artikel_list(request):
    artikel = ArtikelBaznas.objects.all()
    return render(request, "admin/artikel_list.html", {"artikel": artikel})

@login_required(login_url='/auth-login')
def admin_artikel_tambah(request):
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil menambahkan artikel')
            return redirect('ppid:admin_artikel_list')
    else:
        forms = ArtikelForms()
    return render(request, "admin/artikel_form.html", {"form": forms})

@login_required(login_url='/auth-login')
def admin_artikel_update(request, id_artikel):
    artikel = get_object_or_404(ArtikelBaznas, id=id_artikel)
    if request.method == "POST":
        form = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil memperbarui artikel')
            return redirect('ppid:admin_artikel_list')
    else:
        form = ArtikelForms(instance=artikel)
    return render(request, "admin/artikel_form.html", {"form": form})

@login_required
def admin_artikel_delete(request, id_artikel):
    artikel = get_object_or_404(ArtikelBaznas, id=id_artikel)
    try:
        artikel.delete()
        messages.success(request, 'Berhasil menghapus artikel')
    except Exception as e:
        messages.error(request, f'Gagal menghapus artikel: {str(e)}')
    return redirect('ppid:admin_artikel_list')

# === PIMPINAN ===
@login_required
def admin_pimpinan_list(request):
    pimpinan = Pimpinan.objects.all()
    return render(request, "admin/pimpinan_list.html", {"pimpinan": pimpinan})

@login_required(login_url='/auth-login')
def admin_pimpinan_tambah(request):
    if request.method == "POST":
        forms = PimpinanForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Berhasil menambahkan pimpinan')
            return redirect('ppid:admin_pimpinan_list')
    else:
        forms = PimpinanForm()
    return render(request, "admin/pimpinan_forms.html", {"form": forms})

@login_required(login_url='/auth-login')
def admin_pimpinan_update(request, id_pimpinan):
    pimpinan = get_object_or_404(Pimpinan, id=id_pimpinan)
    if request.method == "POST":
        form = PimpinanForm(request.POST, request.FILES, instance=pimpinan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil memperbarui pimpinan')
            return redirect('ppid:admin_pimpinan_list')
    else:
        form = PimpinanForm(instance=pimpinan)
    return render(request, "admin/pimpinan_forms.html", {"form": form})

@login_required(login_url='/auth-login')
def admin_pimpinan_delete(request, id_pimpinan):
    pimpinan = get_object_or_404(Pimpinan, id=id_pimpinan)
    try:
        pimpinan.delete()
        messages.success(request, 'Berhasil menghapus pimpinan')
    except Exception as e:
        messages.error(request, f'Gagal menghapus pimpinan: {str(e)}')
    return redirect('ppid:admin_pimpinan_list')

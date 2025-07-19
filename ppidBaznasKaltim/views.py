from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'PPID Baznas Kaltim',
            'latest_info': [
                {
                    'date': '10/01/2025',
                    'title': 'Pemberian Tumpeng Kepada Gubernur Kaltim',
                    'description': (
                        'BAZNAS Provinsi Kalimantan Timur menyerahkan pemberian Tumpeng kepada '
                        'Gubernur Kalimantan Timur Isran Noor di Kantor Gubernur Kaltim, Samarinda.'
                    ),
                    'image': 'images/info1.jpg'
                },
                {
                    'date': '08/01/2025',
                    'title': 'Rapat Koordinasi Kabupaten Maros Sulawesi dan Tanjungpinang Provinsi',
                    'description': (
                        'BAZNAS Kaltim mengadakan rapat koordinasi dengan Kabupaten Maros dan Tanjungpinang '
                        'untuk membahas program zakat, infaq dan shadaqah.'
                    ),
                    'image': 'images/info2.jpg'
                }
            ],
            'contact_info': {
                'address': 'Jl. Harmonika No. 01 Samarinda Ulu, Dadi Mulya Kalimantan Timur',
                'phone': '08115846664',
                'fax': '08115846664'
            }
        })
        return context

class InformasiPublikView(TemplateView):
    template_name = 'ppid/informasi_publik.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Informasi Publik - PPID Baznas Kaltim',
            'documents': [
                {'title': 'Laporan Keuangan 2024', 'type': 'PDF', 'size': '2.5 MB'},
                {'title': 'Program Kerja 2025', 'type': 'PDF', 'size': '1.8 MB'},
                {'title': 'Struktur Organisasi', 'type': 'PDF', 'size': '500 KB'},
                {'title': 'Profil BAZNAS Kaltim', 'type': 'PDF', 'size': '3.2 MB'}
            ]
        })
        return context

class LayananInformasiView(TemplateView):
    template_name = 'ppid/layanan_informasi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Layanan Informasi - PPID Baznas Kaltim',
            'services': [
                {'name': 'Permohonan Informasi Online', 'description': 'Ajukan permohonan informasi secara online'},
                {'name': 'Konsultasi PPID', 'description': 'Konsultasi mengenai informasi publik'},
                {'name': 'Pengaduan', 'description': 'Sampaikan pengaduan atau keluhan'},
                {'name': 'Download Dokumen', 'description': 'Unduh dokumen informasi publik'}
            ]
        })
        return context

def regulasi(request):
    return render(request, 'ppid/regulasi.html')

class RegistrasiView(TemplateView):
    template_name = 'ppid/registrasi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrasi - PPID Baznas Kaltim'
        return context

class LaporanView(TemplateView):
    template_name = 'ppid/laporan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Laporan - PPID Baznas Kaltim',
            'reports': [
                {'year': '2024', 'title': 'Laporan Tahunan 2024', 'status': 'Tersedia'},
                {'year': '2023', 'title': 'Laporan Tahunan 2023', 'status': 'Tersedia'},
                {'year': '2022', 'title': 'Laporan Tahunan 2022', 'status': 'Tersedia'}
            ]
        })
        return context

class FAQView(TemplateView):
    template_name = 'ppid/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'FAQ - PPID Baznas Kaltim',
            'faqs': [
                {
                    'question': 'Apa itu PPID?',
                    'answer': (
                        'PPID adalah Pejabat Pengelola Informasi dan Dokumentasi yang bertugas '
                        'melaksanakan kebijakan informasi dan dokumentasi.'
                    )
                },
                {
                    'question': 'Bagaimana cara mengajukan permohonan informasi?',
                    'answer': (
                        'Anda dapat mengajukan permohonan informasi melalui formulir online '
                        'atau datang langsung ke kantor BAZNAS Kaltim.'
                    )
                },
                {
                    'question': 'Berapa lama proses permohonan informasi?',
                    'answer': (
                        'Proses permohonan informasi maksimal 10 hari kerja sesuai dengan '
                        'UU Keterbukaan Informasi Publik.'
                    )
                }
            ]
        })
        return context

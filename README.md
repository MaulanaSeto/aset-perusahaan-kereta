# Tugas 2
1. Implementasi Daftar Periksa (*Checklist*)
   * Membuat Proyek DJango
     * Membuat Direktori dan Repositori serta Mengaktifkan Lingkungan Virtual (*Virtual Environment*)<br>Membuat direktori `aset-perusahaan-kereta`, membuat repoositori GitHub `aset-perusahaan-kereta`, kemudian menginisiasikan direktori sebagai repositori lokal dengan repositori GitHub. Selanjutnya membuat lingkungan virtual dengan perintah prompt berikut.
       ```bash
       python -m venv env
       ```
       Selanjutnya menjalankan lingkungan virtual untuk mengisolasi paket dan dependensi aplikasi agar tidak bertabrakan dengan versi lain dengan perintah berikut.
       ```bash
       env\Scripts\activate.bat
       ```
     * Mempersiapkan Dependensi dan Membuat Proyek Django<br>Membuat berkas `requirements.txt` di direktori yang sama berisi dependensi lalu memasang dependensi dengan perintah prompt berikut.
       ```bash
       pip install -r requirements.txt
       ```
       Setelah dependensi terpasang, membuat proyek Django bernama `aset-perusahaan-kereta` dengan perintah prompt berikut.
       ```bash
       django-admin startproject shopping_list .
       ```
     * Mengonfigurasi Proyek<br>Menambahkan `*` pada `ALLOWED_HOSTS` di `settings.py` untuk menizinkan akses dari semua host sesuai kode berikut.
       ```python
       ...
       ALLOWED_HOSTS = ["*"]
       ...
       ```
     * Mengunggah Proyek ke Repositori GitHub<br>Menambahkan berkas `.gitignore` lalu mengunggah proyek ke repositori GitHub.
   * Membuat Aplikasi `main`<br>Membuat aplikasi `main` dengan perintah prompt berikut.
       ```bash
       python manage.py startapp main
       ```
   * Merutekan `main` ke Proyek<br>Menambahkan `main` ke variabel `INSTALLED_APPS` pada berkas `settings.py` di subdirektori `shopping_list` sesuai kode berikut.
     ```python
     INSTALLED_APPS = [
         ...,
         'main',
         ...
     ]
     ```
   * Membuat Model Aplikasi
     * Mengubah Berkas `models.py`<br>Mengisi berkas `models.py` di direktori `main` dengan kode berikut.
       ```python
       from django.db import models

       class Product(models.Model):
           type = models.CharField(max_length=255)
           name = models.CharField(max_length=255)
           amount = models.IntegerField()
           owner = models.CharField(max_length=255)
           date_added = models.DateField(auto_now_add=True)
           description = models.TextField()
       ```
     * Memigrasi Model<br>Membuat migrasi model dengan perintah prompt berikut.
       ```bash
       python manage.py makemigrations
       ```
       Lalu melakukan migrasi dengan perintah prompt berikut.
       ```bash
       python manage.py migrate
       ```
   * Membuat Fungsi di `vews.py`<br>Mengimpor pustaka dan menambahkan fungsi `show_main` pada berkas `views.py` di subdirektori `main` dengan kode berikut.
     ```bash
     def show_main(request):
         context = {
             'name': 'Maulana Seto',
             'class': 'PBP B'
         }
         return render(request, "main.html", context)
     ```
   * Melakukan Perutean `urls.py`<br>Mengisi berkas `urls.py` pada subdirektori `main` dengan kode berikut.
     ```python
     from django.urls import path
     from main.views import show_main

     app_name = 'main'

     urlpatterns = [
         path('', show_main, name='show_main'),
     ]
     ```
   * Melakukan *Deployment* ke Adaptable
3. Bagan
4. ENV
5. 

# Tugas 3
1. Perbedaan `POST` dan `GET`<br>Perbedaan metode `POST` dan `GET` dalam Django yaitu metode `POST` digunakan untuk mengirim data ke server untuk mengubah atau menyimpan data, sedangkan metode `GET` digunakan untuk mengambil atau membaca data dari server.
2. Perbedaan XML, JSON, dan HTML
   * XML<br>XML digunakan untuk menggambarkan struktur data dan metadata. Ini adalah bahasa markup yang sangat serbaguna yang dapat digunakan untuk menyimpan dan mengirim data.
   * JSON<br>JSON digunakan untuk pertukaran data ringan antar aplikasi. Ini adalah format yang sangat populer dalam pengembangan web dan API karena kemampuan mudah dibaca oleh manusia dan kemampuannya untuk menggambarkan struktur data yang kompleks.
   * HTML<br> HTML digunakan untuk menggambarkan struktur dan konten halaman web. Ini adalah format khusus untuk membangun tampilan web.
3. Alasan JSON Sering Digunakan dalam Pertukaran Data antara Aplikasi Web Modern<br>JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena ringan, efisien, mudah dibaca oleh manusia, berformat standar dalam API Web, bersifat lintas platform, dan terintegrasi dengan JavaScript.
4. Implementasi Daftar Periksa (*Checklist*)
   * Membuatan Masukan *Form*<br>Untuk membuat masukan *form*, dibuat berkas bernama `forms.py` pada direktori `main` untuk menerima produk baru dengan isi kode berikut.
     ```python
     from django.forms import ModelForm
     from main.models import Product

     class ProductForm(ModelForm):
     class Meta:
          model = Product
          fields = ["type", "name", "amount", "owner", "description"]
     ```
     Kemudian  mengimpor beberapa pustaka dan membuat fungsi `create_product` yang digunakan untuk menerima permintaan dari pengguna dengan kode berikut.
     ```python
     from django.http import HttpResponseRedirect
     from main.forms import ProductForm
     from django.urls import reverse    

     def create_product(request):
         form = ProductForm(request.POST or None)
         if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
         context = {'form': form}
         return render(request, "create_product.html", context)
     ```
     Fungsi ini bertujuan untuk menghasilkan dan menangani formulir yang memungkinkan pengguna untuk menambahkan data produk ke dalam sistem secara otomatis melalui form yang dikirim.
   * Membuat Fungsi `view`
     * HTML<br>Mengubah fungsi `show_main` pada berkas `views.py` di folder `main` menjadi sebagai berikut.
       ```python
       def show_main(request):
           products = Product.objects.all()
           context = {
             'name': 'Maulana Seto',
             'class': 'PBP B', 
             'products': products
           }
           return render(request, "main.html", context)
       ```
     * XML<br>Mengimpor beberapa pustaka lalu membuat fungsi `show_xml` dengan parameter `request` dengan kode berikut.
       ```python
       from django.http import HttpResponse
       from django.core import serializers

       def show_xml(request):
           data = Product.objects.all()
           return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
     * JSON<br>Membuat fungsi `show_json` dengan parameter `request` dengan kode sebagai berikut.
       ```python
       def show_json(request):
           data = Product.objects.all()
           return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
     * XML by ID<br>Membuat fungsi `show_xml_by_id` dengan parameter `request` dan `id` dengan kode berikut.
       ```python
       def show_xml_by_id(request, id):
           data = Product.objects.filter(pk=id)
           return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
     * JSON by ID<br>Membuat fungsi `show_json_by_id` dengan parameter `request` dan `id` dengan kode berikut.
       ```python
       def show_json_by_id(request, id):
           data = Product.objects.filter(pk=id)
           return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
  
   * Perutean URL `view`<br>Untuk membuat perutean URL kelima `view`, mengimpor kelima fungsi `view` yang telah dibuat ke berkas `urls.py` di folder `main` dengan kode berikut.
     ```python
     from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
     ```
     Kemudian menambahkan jalur URL masing-masing `view` ke dalam `urlpatterns` dengan kode berikut.
     ```python
     ...
     path('xml/', show_xml, name='show_xml'),
     path('json/', show_json, name='show_json'),
     path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
     path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
     ...
     ```

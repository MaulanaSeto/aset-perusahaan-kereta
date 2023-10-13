# Tugas 2
1. Implementasi Daftar Periksa (*Checklist*)
   * Membuat Proyek DJango
     * Membuat Direktori dan Repositori serta Mengaktifkan Lingkungan Virtual (*Virtual Environment*)<br>Membuat direktori `aset-perusahaan-kereta`, membuat repoositori GitHub `aset-perusahaan-kereta`, kemudian menginisiasikan direktori sebagai repositori lokal dengan repositori GitHub. Selanjutnya membuat lingkungan virtual dengan perintah prompt berikut.
       ```bash
       python -m venv env
       ```
       Selanjutnya menjalankan lingkungan virtual dengan perintah berikut.
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
           owner = models.CharField(max_length=255)
           amount = models.IntegerField()
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
   * Membuat Fungsi di `views.py`<br>Mengimpor pustaka dan menambahkan fungsi `show_main` pada berkas `views.py` di subdirektori `main` dengan kode berikut.
     ```python
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
2. Bagan Pola Django<br>![Bagan Pola Django](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Bagan%20Pola%20Django.png)<br>Ketika pengguna memberikan permintaan, permintaan tersebut akan dieksekusi oleh `urls.py` sebagai Konfigurator URL untuk memilih `view` pada `views.py`. Setelah `view` didapat, `views.py` akan memilih templat HTML lalu menampilkannya. `views.py` juga mengirimkan kueri ke Model. Ketika Model menerima kueri maupun respons data, Model melakukan transaksi data dengan Basis Data.
3. Alasan Penggunaan Lingkungan Virtual<br>Lingkungan virtual digunakan untuk mengisolasi paket serta dependensi dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. meskipun begitu, pembuatan proyek Django tanpa lingkungan virtual tetap dapat dilakukan.
4. Perbedaan PMVC, MVT, dan MVVM
   * MVC (Model-View-Controller)<br>MVC adalah konsep yang digunakan dalam pengembangan web tradisional.
   * MVT (Model-View-Template)<br>MVT adalah konsep yang digunakan dalam *framework* Django untuk pengembangan web dengan Python.
   * MVVM (Model-View-ViewModel)<br>MVVM lebih umum digunakan dalam pengembangan aplikasi berbasis klien dan memberikan pemisahan yang lebih kuat antara tampilan pengguna dan logika bisnis daripada MVC atau MVT.

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
  
   * Perutean URL `view`<br>Untuk membuat perutean URL kelima `view`, mengimpor seluruh fungsi `view` yang telah dibuat ke berkas `urls.py` di folder `main` dengan kode berikut.
     ```python
     from main.views import *
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
5. Tangkapan Layar Postman
   * HTML<br>![HTML](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Screenshot%201.png)
   * XML<br>![XML](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Screenshot%202.png)
   * JSON<br>![JSON](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Screenshot%203.png)
   * XML by ID<br>![XML by ID](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Screenshot%204.png)
   * JSON by ID<br>![JSON by ID](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Screenshot%205.png)

# Tugas 4
1. Django `UserCreationForm`<br>Django `UserCreationForm` adalah salah satu bentuk formulir yang disediakan oleh Django, sebuah kerangka kerja pengembangan web Python yang populer. Formulir ini digunakan untuk membuat dan mendaftarkan pengguna baru dalam aplikasi web yang dibangun dengan Django. `UserCreationForm` telah disediakan oleh Django secara bawaan untuk memudahkan pengembang dalam proses pembuatan dan manajemen akun pengguna.
   * Kelebihan
     * Mudah digunakan.
     * Dapat memvalidasi data secara otomatis.
     * Mudah diintegrasikan.
     * *Customizable*.
   * Kekurangan
     * Memiliki tampilan yang standar.
     * Kurang fleksibel untuk kasus khusus.
     * Tidak memiliki fitur keamanan bawaan lanjutan.
2. Autentikasi dan Otorisasi
   * Autentikasi<br>Autentikasi adalah proses mengidentifikasi pengguna dan memeriksa apakah pengguna tersebut adalah entitas yang diklaim. Ini adalah langkah pertama dalam mengelola akses ke aplikasi web dan mengidentifikasi pengguna berdasarkan kredensial, seperti nama pengguna dan kata sandi.
   * Otorisasi<br>Otorisasi adalah proses yang terjadi setelah autentikasi. Ini berkaitan dengan menentukan apa yang diizinkan atau tidak diizinkan oleh pengguna yang telah terautentikasi. Dalam istilah sederhana, ini adalah tentang memberikan atau menolak akses pengguna ke sumber daya atau tindakan tertentu dalam aplikasi.
   * Pentingnya Autentikasi dan Otorisasi<br>Autentikasi dan otorisasi sangat penting untuk menjaga keamanan aplikasi web. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan atau mengakses data yang sesuai dengan peran atau izin mereka.
3. *Cookies*<br>*Cookies* adalah sejumlah kecil informasi dikirim oleh server web ke peramban kemudian dikirim kembali oleh peramban pada permintaan halaman berikutnya. *Cookies* digunakan dalam konteks aplikasi web untuk menyimpan informasi tertentu yang perlu dipertahankan antara permintaan-permintaan yang dilakukan oleh pengguna ke server. Ini membantu dalam menjaga keadaan sesi pengguna, pelacakan preferensi, autentikasi, dan banyak hal lain dalam aplikasi web. Data sebuah *cookie* terdiri dari sebuah pasangan nama atau nilai yang dikirim dalam *header* permintaan HTTP `GET` atau `POST` klien. Dalam mengelola data sesi pengguna, Django akan membaca parameter *cookie* yang diteruskan oleh peramban, menyimpan data dalam bentuk sesi, memodifikasi informasi dalam sesi tersebut, dan mengirim kembali `cookie` yang sesuai ke peramban.
4. Penggunaan *Cookies*<br>Penggunaan *cookies* dalam pengembangan web dapat aman jika dikelola dengan benar, namun ada beberapa risiko potensial yang harus diwaspadai.
   * Keamanan Data<br>*Cookies* dapat digunakan untuk menyimpan informasi sensitif seperti token autentikasi atau data pengguna. Jika *cookies* ini tidak dienkripsi atau tidak diatur dengan benar, mereka bisa menjadi target potensial bagi penyerang untuk mencuri data pengguna.
   * Pelacakan<br>*Cookies* sering digunakan untuk melacak perilaku pengguna secara daring. Ini dapat menciptakan masalah privasi jika tidak diatur dengan benar atau jika data yang dikumpulkan tidak dilindungi.
   * Kebocoran Data<br>Jika *cookies* mengandung data yang terlalu banyak atau terlalu rinci, *cookies* bisa menjadi risiko kebocoran data jika terjadi pelanggaran keamanan.
6. Implementasi Daftar Periksa
   * Mengimplementasi Fungsi Pendaftaran, Masuk, dan Keluar
     * Membuat Fungsi Pendaftaran<br>Menjalankan lingkungan virtual kemudian mengimpor beberapa pustaka pada berkas `views.py` di subdirektori `main` dengan kode berikut.
       ```python
       from django.shortcuts import redirect
       from django.contrib.auth.forms import UserCreationForm
       from django.contrib import messages  
       ```
       Lalu membuat fungsi `register` dengan kode berikut.
       ```python
       def register(request):
           form = UserCreationForm()
           if request.method == "POST":
               form = UserCreationForm(request.POST)
               if form.is_valid():
                   form.save()
                   messages.success(request, 'Your account has been successfully created!')
                   return redirect('main:login')
           context = {'form':form}
           return render(request, 'register.html', context)
       ```
       Terakhir, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls,py` di subdirektori `main` dengan kode berikut.
       ```python
       ...
       path('register/', register, name='register'),
       ...
       ```
     * Membuat Fungsi Masuk<br>Mengimpor pustaka pada berkas `views.py` di subdirektori `main` dengan kode berikut.
       ```python
       from django.contrib.auth import authenticate, login
       ```
       Lalu membuat fungsi `login_user` dengan kode berikut.
       ```python
       def login_user(request):
           if request.method == 'POST':
               username = request.POST.get('username')
               password = request.POST.get('password')
               user = authenticate(request, username=username, password=password)
               if user is not None:
                   login(request, user)
                   return redirect('main:show_main')
               else:
                   messages.info(request, 'Sorry, incorrect username or password. Please try again.')
           context = {}
           return render(request, 'login.html', context)
       ```
       Terakhir, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls,py` di subdirektori `main` dengan kode berikut.
       ```python
       ...
       path('login/', login_user, name='login'),
       ...
       ```
     * Membuat Fungsi Keluar<br>Mengimpor pustaka pada berkas `views.py` di subdirektori `main` dengan kode berikut.
       ```python
       from django.contrib.auth import logout
       ```
       Lalu membuat fungsi `logout_user` dengan kode berikut.
       ```python
       def logout_user(request):
           logout(request)
           return redirect('main:login')
       ```
       Terakhir, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls,py` di subdirektori `main` dengan kode berikut.
       ```python
       ...
       path('logout/', logout_user, name='logout'),
       ...
       ```
   * Membuat Akun<br>![Akun 1](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Akun%201.png)
     ![Akun 2](https://github.com/MaulanaSeto/aset-perusahaan-kereta/blob/master/Akun%202.png)
   * Menghubungkan Model `Product` dengan `User`<br>Pertama, mengimpor pustaka pada berkas `models.py` di subdirektori `main` dengan kode berikut.
     ```python
     from django.contrib.auth.models import User
     ```
     Kedua, menambahkan kode baru di kelas `Product` dengan kode berikut.
     ```python
     class Product(models.Model):
         user = models.ForeignKey(User, on_delete=models.CASCADE)
     ...
     ```
     Ketiga, memperbarui kode fungsi `create_product` pada berkas `views.py` di subdirektori `main` menjadi kode berikut.
     ```python
     def create_product(request):
         form = ProductForm(request.POST or None)
         if form.is_valid() and request.method == "POST":
             product = form.save(commit=False)
             product.user = request.user
             product.save()
             return HttpResponseRedirect(reverse('main:show_main'))
     ...
     ```
     Terakhir, memperbarui kode fungsi `show_main` menjadi kode berikut.
     ```python
     def show_main(request):
         products = Product.objects.filter(user=request.user)
         context = {
             'name': request.user.username,
     ...
     ```
   * Menampilkan Detail Informasi Pengguna dan Menerapkan *Cookies*<br>Pertama, mengimpor beberapa pustaka pada berkas `views.py` di subdirektori `main` dengan kode berikut.
     ```python
     import datetime
     from django.http import HttpResponseRedirect
     from django.urls import reverse
     ```
     Kedua, memperbarui kode fungsi `login_user`pada blok `if user not None` menjadi kode berikut.
     ```python
     ...
     if user is not None:
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main")) 
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response
     ...
     ```
     Ketiga, menambahkan isi *dictionary* variabel `context` padafungsi `show_main` dengan kode berikut.
     ```python
     ...
     'last_login': request.COOKIES['last_login'],
     ...
     ```
     Keempat, memperbarui kode fungsi `logout_user` menjadi kode berikut.
     ```python
     def logout_user(request):
         logout(request)
         response = HttpResponseRedirect(reverse('main:login'))
         response.delete_cookie('last_login')
         return response
     ```
     Terakhir, menambah kode berikut ke dalam berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
     ```html
     ...
     <h5>Sesi terakhir masuk: {{last_login}}</h5>
     ...
     ```
   * Menambahkan Fitur Tambah dan Kurangi Jumlah<br>Pertama, mengimpor pustaka pada berkas `views.py` di subdirektori `main` dengan kode berikut.
     ```python
     from django.shortcuts import get_object_or_404
     ```
     Kedua, membuat fungsi `increase_product_amount` dan `decrease_product_amount` dengan kode berikut.
     ```python
     def increase_product_amount(request, product_id):
         product = get_object_or_404(Product, id=product_id)
         product.amount += 1
         product.save()
         return redirect('main:show_main')

     def decrease_product_amount(request, product_id):
         product = get_object_or_404(Product, id=product_id)
         if product.amount > 0:
             product.amount -= 1
             product.save()
         return redirect('main:show_main')
     ```
     Ketiga, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls,py` di subdirektori `main` dengan kode berikut.
     ```python
     ...
     path('product/increase/<int:product_id>/', increase_product_amount, name='increase_product_amount'),
     path('product/decrease/<int:product_id>/', decrease_product_amount, name='decrease_product_amount'),
     ...
     ```
     Terakhir, membuat tombol `Tambah` dan `Kurangi` pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
     ```html
     ...
     <td>{{product.owner}}</td>
     <td>
         <span>{{product.amount}}</span>
         <div>
             <a href="{% url 'main:increase_product_amount' product.id %}">
                 <button>Tambah</button>
             </a>
             <a href="{% url 'main:decrease_product_amount' product.id %}">
                 <button>Kurangi</button>
             </a>
         </div>
     </td>
     <td>{{product.date_added}}</td>
     ...
     ```
   * MenambahkanFitur Hapus Produk<br>Pertama, membuat fungsi `delete_product` pada berkas `views.py` di subdirektori `main` dengan kode berikut.
     ```python
     def delete_product(request, product_id):
         product = get_object_or_404(Product, id=product_id, user=request.user)
         product.delete()
         return HttpResponseRedirect(reverse('main:show_main'))
     ```
     Kedua, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls.py` di subdirektori `main` dengan kode berikut.
     ```python
     ...
     path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
     ...
     ```
     Terakhir, membuat tombol `Hapus` pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
     ```html
     ....
     <td>{{product.description}}</td>
     <td>
         <a href="{% url 'main:delete_product' product.id %}">
             <button>Hapus</button>
         </a>
     </td>
     ...
     ```
# Tugas 5
1. Manfaat *Selector*
   * *Element Selector*<br>*Elemen Selector* bermanfaat untuk menerapkan suatu properti pada elemen-elemen yang sama.
   * *ID Selector*<br>*ID Selector* bermanfaat untuk menerapkan suatu properti ke elemen-elemen dalam cakupan ID yang sama.
   * *Class Selector*<br>*Class Selector* bermanfaat untuk menerapkan suatu properti ke dalam kelompok kelas berkarakteristik sama.
2. HTML5 *Tag*
   * `<!DOCTYPE>`<br>Mendefinisikan jenis dokumen dan versi HTML yang digunakan.
   * `<html>`<br>Menandai awal dan akhir berkas HTML.
   * `<head>`<br>Berisi informasi meta, tautan ke berkas eksternal, atau skrip JavaScript yang mendefinisikan halaman web.
   * `<title>`<br>Menentukan judul halaman web yang ditampilkan di bilah judul peramban.
   * `<meta>`<br>Memberikan metadata tentang dokumen.
   * `<link>`<br>Menghubungkan dokumen dengan sumber daya eksternal seperti berkas CSS.
   * `<style>`<br>Mendefinisikan gaya CSS dalam berkas HTML.
   * `<script>`<br>Menyematkan skrip JavaScript di dalam berkas HTML.
   * `<body>`<br>Berisi konten utama dokumen HTML, seperti teks, gambar, dan elemen-elemen lainnya.
   * `<p>`<br>Menandai paragraf teks.
   * `<a>`<br>Membuat tautan *hyperlink* ke halaman web atau sumber daya lainnya.
   * `<img>`<br>Menyisipkan gambar ke dalam berkas.
3. Perbedaan *Margin* dan *Padding*
   * *Margin*<br>*Margin* adalah ruang di luar batas elemen (garis tepi elemen) yang mengontrol jarak antara elemen dengan elemen-elemen lain.
   * *Padding*<br>*Padding* adalah ruang di antara batas elemen (garis tepi elemen) dan konten yang mengontrol jarak antara konten elemen dan batas elemen.
4. Perbedaan Kerangka Kerja CSS *Tailwind* dan *Bootstrap*
   * *Tailwind*
     * Membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.
     * Memiliki berkas CSS yang lebih kecil sedikit dibandingkan Bootstrap dan hanya akan memuat kelas-kelas utilitas yang ada
     * Memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek.
     * Memiliki pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana menggabungkannya untuk mencapai tampilan yang diinginkan.
   * *Bootstrap*
     * Menggunakan gaya dan komponen yang telah didefinisikan, yang memiliki tampilan yang sudah jadi dan dapat digunakan secara langsung.
     * Memiliki berkas CSS yang lebih besar dibandingkan dengan *Tailwind* karena termasuk banyak komponen yang telah didefinisikan.
     * Sering kali menghasilkan tampilan yang lebih konsisten di seluruh proyek karena menggunakan komponen yang telah didefinisikan.
     * Memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.
   * Simpulan<br>*Tailwind* dapat digunakan jika membutuhkan fleksibilitas yang tinggi, menginginkan desain yang unik, membutuhkan kinerja yang lebih baik, dan sudah memahami dasar-dasar CSS; sedangkan *Bootstrap* dapat digunakan jika membutuhkan solusi yang mudah dan cepat, membutuhkan dokumentasi lengkap, sedang bekerja dalam proyek besar, serta menginginkan dukungan lintas peramban yang kuat.
5. Implementasi Daftar Periksa
   * Mmbuat Folder<br>Pada subfolder `main` membuat folder `static` dan membuat folder `css` di dalam folder `static`.
   * Membuat Berkas CSS<br>Membuat berkas CSS di folder `css` untuk setiap berkas HTML di folder `templates` pada subdirektori `main`.
   * Merutekan Folder `static`<br>Mengimpor pustaka pada berkas `settings.py` di subdirektori `aset_perusahaan_kereta` sesuai kode berikut.
     ```python
     import os
     ```
     Lalu menambahkan variabel `STATIC_ROOT` di atas variabel `STATIC_URL` dengan kode berikut.
     ```python
     STATIC_ROOT = os.path.join(BASE_DIR, 'main/static')
     ```
   * Mengumpulkan Semua Berkas Statis ke Suatu Direktori<br>Menjalankan lingkungan virtual lalu menjalankan perintah prompt berkut.
     ```bash
     python manage.py collectstatic
     ```
   * Menghubungkan Berkas HTML ke CSS<br>Menambahkan kode `{% load static %}` ke setiap berkas HTML seletah kode `{% extends 'base.html' %}` lalu menambahkan rute ke berkas CSS masing-masing dengan kode berikut.
     ```html
     <link rel="stylesheet" href="{% static 'css/[nama-berkas].css'%}"> 
     ```
# Tugas 6
1. Perbedaan Pemrograman Sinkron dan Asinkron
   * Pemrograman Sinkron<br>Pada pemrograman sinkron, tugas-tugas dieksekusi secara berurutan satu per satu. Artinya, tugas pertama harus selesai sebelum tugas kedua dimulai, dan seterusnya. Ketika tugas I/O dilakukan, program akan terblokir atau "menggantung" sampai tugas I/O tersebut selesai.
   * Pemrograman Asinkron<br>Pada pemrograman asinkron, tugas-tugas dapat dilakukan secara bersamaan atau non-blokir. Artinya, program tidak perlu menunggu tugas I/O selesai sebelum melanjutkan tugas lain. Tugas I/O yang memakan waktu lama dapat dipindahkan ke latar belakang dan program dapat melanjutkan eksekusi tugas lain tanpa harus menunggu.
2. Paradigma *Event-Driven Programming*<br>*Event-driven programming* adalah paradigma pemrograman dengan alur eksekusi program ditentukan oleh kejadian atau peristiwa yang terjadi, bukan oleh urutan instruksi yang tertulis dalam kode. Program merespons peristiwa atau sinyal eksternal yang terjadi di lingkungan eksekusi, seperti interaksi pengguna (seperti klik tetikus atau masukan *keyboard*), sinyal dari perangkat keras, atau data yang diterima melalui jaringan. Pada tugas ini, metode `addProduct` diimplementasikan sebagai metode *event-driven* yang akan dieksekusi jika tombol `Tambah` di `Tambah Produk (AJAX)` diklik.
3. Penerapan Pemrograman Asinkron pada AJAX
   * XMLHttpRequest<br>XMLHttpRequest adalah objek JavaScript klasik yang digunakan untuk membuat koneksi ke server dan mengirimkan atau menerima data tanpa harus memuat ulang halaman web secara keseluruhan.
   * Fetch API<br>Fetch API adalah standar modern untuk mengambil dan mengirim data menggunakan JavaScript. Ia menyediakan antarmuka yang lebih powerful dan fleksibel daripada XMLHttpRequest.
   * *Async* dan *Await*<br>*Async* dan *Await* adalah fitur ES2017 yang memudahkan penanganan kode asinkron dengan cara yang lebih mirip dengan gaya sinkron. Dengan *Async* dan *Await*, kode asinkron dapat ditulis dengan tampilan yang lebih bersih dan mudah dimengerti.
4. *Fetch API* dan *jQuery*
   * Fetch API
     * Modern dan Natif<br>Fetch API adalah standar modern yang sudah ada di peramban terbaru tanpa memerlukan pustaka eksternal. Ini membuatnya menjadi pilihan alami untuk proyek-proyek yang ingin menggunakan fitur terbaru dari JavaScript.
     * *Promise-Biased*<br>Fetch API mengembalikan Promise yang memungkinkan penggunaan Async/Await untuk menangani kode asinkron dengan cara yang bersih dan mudah dimengerti.
     * Lebih Ringan<br>Fetch API memiliki *overhead* yang lebih rendah dibandingkan dengan jQuery karena itu adalah bagian dari JavaScript natif.
   * jQuery
     * Mudah Digunakan<br>jQuery menyederhanakan sintaks AJAX dan menyediakan metode dan *event handling* yang konsisten di berbagai peramban. Ini membuatnya mudah digunakan terutama untuk pengembang yang baru belajar atau yang memerlukan solusi cepat.
     * *Cross-Browser Compatibility*<br>jQuery dirancang untuk menangani perbedaan implementasi di berbagai peramban, memastikan konsistensi perilaku di seluruh kerangka kerja.
     * Plugin Ekstnsif<br>jQuery memiliki banyak plugin yang memperluas fungsionalitasnya. jQuery memiliki berbagai fitur tambahan seperti animasi, manipulasi DOM, dan lain-lain.
   * Simpulan<br>Secara umum, penggunaan Fetch API dalam pengembangan aplikasi web modern adalah pilihan yang baik karena ini merupakan standar modern dan memberikan fleksibilitas lebih besar.
6. Implementasi Daftar Periksa
   * AJAX GET
     * Mengubah Kode Item<br>Pertama, mengosongkan blok `table` dan menambahkannya atribut pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
       ```html
       <table id="product_table"></table>
       ```
       Terakhir, membuat blok `script` berisi kode berikut.
       ```javascript
       async function refreshProducts() {
           document.getElementById("product_table").innerHTML = ""
           const products = await getProducts()
           let htmlString = `<tr>
               <th>Jenis</th>
               <th>Nama</th>
               <th>Pemilik</th>
               <th>Jumlah</th>
               <thTanggal Ditambahkan</th>
               <th>Deskripsi</th>
               <th>Aksi</th>
           </tr>`
           products.forEach((item) => {
               htmlString += `\n<tr class="isi-tabel {% if forloop.last %}produk-terakhir{% endif %}">
               <td class="jenis">${item.fields.type}</td>
               <td class="nama">${item.fields.name}</td>
               <td class="pemilik">${item.fields.owner}</td>
               <td class="jumlah">${item.fields.amount}</td>
               <td class="tanggal">${item.fields.date_added}</td>
               <td class="deskripsi">${item.fields.description}</td>
               <td class="hapus"><button onclick="deleteProduct(${item.pk})">Hapus</button></td>
           </tr>`
           })
           document.getElementById("product_table").innerHTML = htmlString
       }
       refreshProducts()
       ```
     * Melakukan Pengembalian Item<br>Pertama, menambahkan fungsi `get_product_json` pada berkas `views.py`di subdirektori `main` dengan kode berikut.
       ```python
       def get_product_json(request):
           product_item = Product.objects.all()
           return HttpResponse(serializers.serialize('json', product_item))
       ```
       Kedua, menambahkan fungsi `getProducts` pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
       ```javascript
       async function getProducts() {
           return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
       }
       ```
       Terakhir, merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls.py` di subdirektori `main` dengan kode berikut.
       ```python
       ...
       path('get-product/', get_product_json, name='get_product_json'),
       ...
       ```
   * AJAX POST
     * Membuat Tombol Modal<br>Pertama, menambahkan tombol `Tambah Produk (AJAX)` di antara tombol `Tambah Produk` dan informasi sesi terakhir masuk pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
       ```html
       <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Tambah Produk (AJAX)</button>
       ```
       Terakhir, membuat modal dengan kode berikut.
       ```html
       <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
           <div class="modal-dialog">
               <div class="modal-content">
                   <div class="modal-header">
                       <h1 class="modal-title fs-5" id="exampleModalLabel">Tambah Produk</h1>
                       <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                   </div>
                   <div class="modal-body">
                       <form id="form" onsubmit="return false;">
                           {% csrf_token %}
                           <div class="mb-3">
                               <label for="type" class="col-form-label">Jenis:</label>
                               <input type="text" class="form-control" id="type" name="type"></input>
                           </div>
                           <div class="mb-3">
                               <label for="name" class="col-form-label">Nama:</label>
                               <input type="text" class="form-control" id="name" name="name"></input>
                           </div>
                           <div class="mb-3">
                               <label for="owner" class="col-form-label">Pemilik:</label>
                               <input type="text" class="form-control" id="owner" name="owner"></input>
                           </div>
                           <div class="mb-3">
                               <label for="amount" class="col-form-label">Jumlah:</label>
                               <input type="number" class="form-control" id="amount" name="amount"></input>
                           </div>
                           <div class="mb-3">
                               <label for="description" class="col-form-label">Deskripsi:</label>
                               <textarea class="form-control" id="description" name="description"></textarea>
                           </div>
                       </form>
                   </div>
                   <div class="modal-footer">
                       <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Tambah</button>
                       <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                   </div>
               </div>
           </div>
       </div>
       ```
     * Membuat Fungsi *View*<br>Pertama, menambahkan isi blok `script` pada berkas `main.html` pada folder `templates` di subdirektori `main` dengan kode berikut.
       ```javascript
       function addProduct() {
           fetch("{% url 'main:create_ajax' %}", {
               method: "POST",
               body: new FormData(document.querySelector('#form'))
           }).then(refreshProducts)
           document.getElementById("form").reset()
            return false
       }
       
       async function deleteProduct(id) {
           const confirmation = confirm("Apakah Anda yakin ingin menghapus produk tersebut?");
           if (confirmation) {
               await fetch(`{% url 'main:delete_ajax' %}?id=${id}`, {
                  method: "DELETE",
               });
           refreshProducts();
           }
       }
       ```
       Kedua, menambahkan fungsi `create_ajax` dan `delete_ajax` pada berkas `views.py`di subdirektori `main` dengan kode berikut.
       ```python
       @csrf_exempt
       def create_ajax(request):
           if request.method == 'POST':
               type = request.POST.get("type")
               name = request.POST.get("name")
               owner = request.POST.get("owner")
               amount = request.POST.get("amount")
               description = request.POST.get("description")
               user = request.user
               new_product = Product(type=type, name=name, owner=owner, amount=amount, description=description, user=user)
               new_product.save()
               return HttpResponse(b"CREATED", status=201)
           return HttpResponseNotFound()

       @csrf_exempt
       def delete_ajax(request):
           if request.method == "DELETE":
               product_id = request.GET.get("id")
               try:
                   product = Product.objects.get(pk=product_id, user=request.user)
                   product.delete()
                   return HttpResponse(status=204)
               except Product.DoesNotExist:
                   return HttpResponseNotFound()
           return HttpResponseNotFound()
       ```
     * Membuat Jalur<br>Merutekan fungsi tersebut ke dalam `urlpatterns` pada berkas `urls.py` di subdirektori `main` dengan kode berikut.
       ```python
       ...
       path('create-ajax/', create_ajax, name='create_ajax'),
       path('delete_ajax/', delete_ajax, name='delete_ajax'),
       ...
       ```
     * Menghubungkan Formulir dengan Jalur
       Menambahkan kode berikut ke blok `script` pada berkas `main.html` pada folder `templates` di subdirektori `main`.
       ```javascript
       document.getElementById("button_add").onclick = addProduct
       ```
     * Melakukan *Refresh*
   * Melakukan Perintah `collecstatic`<br>Menjalankan lingkungan virtual lalu menjalankan perintah prompt berkut.
     ```bash
     python manage.py collectstatic
     ```

# Tugas 2
1. Implementasi Daftar Periksa (*Checklist*)
2. 

# Tugas 3
1. Perbedaan metode `POST` dan `GET` dalam Django yaitu, metode `POST` digunakan untuk mengirim data ke server untuk mengubah atau menyimpan data, sedangkan metode `GET` digunakan untuk mengambil atau membaca data dari server.
2. Perbedaan XML, JSON, dan HTML
   * XML<br>XML digunakan untuk menggambarkan struktur data dan metadata. Ini adalah bahasa markup yang sangat serbaguna yang dapat digunakan untuk menyimpan dan mengirim data.
   * JSON<br>JSON digunakan untuk pertukaran data ringan antar aplikasi. Ini adalah format yang sangat populer dalam pengembangan web dan API karena kemampuan mudah dibaca oleh manusia dan kemampuannya untuk menggambarkan struktur data yang kompleks.
   * HTML<br> HTML digunakan untuk menggambarkan struktur dan konten halaman web. Ini adalah format khusus untuk membangun tampilan web.
3. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena ringan, efisien, mudah dibaca oleh manusia, berformat standar dalam API Web, bersifat lintas platform, dan terintegrasi dengan JavaScript.
4. Implementasi Daftar Periksa (*Checklist*)
   * Untuk membuat masukan `form`, dibuat berkas bernama `forms.py` pada direktori `main` untuk menerima produk baru dengan isi kode berikut.
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
   * Membuat Fungsi `views`
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
  
   * Untuk membuat perutean URL kelima `view`, mengimpor kelima fungsi `view` yang telah dibuat ke berkas `urls.py` di folder `main` dengan kode berikut.
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

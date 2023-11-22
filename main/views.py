import datetime
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        if product.amount < 0:
            return render(request, "create_product.html", {'form': form})
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = Product.objects.create(
            user = request.user,
            type = data["type"],
            name = data["name"],
            owner = data["owner"],
            amount = int(data["amount"]),
            description = data["description"]
        )
        new_product.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Anda telah berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Maaf, nama pengguna atau kata sandi salah. Silakan coba kembali.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_product_amount(request, id):
    product = Product.objects.get(pk=id)
    product.amount += 1
    product.save()
    return redirect('main:show_main')

def decrease_product_amount(request, id):
    product = Product.objects.get(pk=id)
    if product.amount > 0:
        product.amount -= 1
        product.save()
    return redirect('main:show_main')

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
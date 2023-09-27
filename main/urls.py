from django.urls import path
from main.views import *

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('product/increase/<int:product_id>/', increase_product_amount, name='increase_product_amount'),
    path('product/decrease/<int:product_id>/', decrease_product_amount, name='decrease_product_amount'),
]
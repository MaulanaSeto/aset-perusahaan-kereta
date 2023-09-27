from django.forms import ModelForm, ValidationError
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["type", "name", "owner", "amount", "description"]
        labels = {
            "type": "Jenis",
            "name": "Nama",
            "owner": "Pemilik",
            "amount": "Jumlah",
            "description": "Deskripsi",
        }
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise ValidationError('Jumlah tidak boleh negatif!')
        return amount
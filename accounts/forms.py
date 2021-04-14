from django.forms import ModelForm
from .models import Customer,Order

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','phone']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
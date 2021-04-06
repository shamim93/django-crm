from django.contrib import admin
from .models import Customer,Product,Order

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone',)
    readonly_fields = ('created',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category',)
    readonly_fields = ('created',)
    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
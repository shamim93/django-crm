from django.contrib import admin
from .models import Customer,Product,Order,Tag,Category

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone',)
    readonly_fields = ('created',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category',)
    readonly_fields = ('created',)
    
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','product','created','status',)
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
 
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
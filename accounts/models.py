from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model): 
    
    # CATEGORY_CHOICES=(
    #     ('indoor','Indoor'),
    #     ('Outdoor','Out Door'),
    # )
    
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    # category = models.CharField(max_length=250,choices = CATEGORY_CHOICES, null=True,default='indoor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True)
    tags = models.ManyToManyField("Tag")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)

        

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('processing','Processing'),
        ('delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    created=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending')
    

    # def __str__(self):
    #     return self.customer

    class Meta:
        ordering=('-created',)
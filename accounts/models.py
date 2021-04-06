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
    
class Product(models.Model):
    CATEGORY_CHOICES=(
        ('indoor','Indoor'),
        ('Outdoor','Out Door'),
    )
    
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250,choices = CATEGORY_CHOICES, null=True,default='indoor')
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)

class Order(models.Model):
    STATUS_CHOICES=(
        ('pending','Pending'),
        ('processing','Processing'),
        ('delivered','Delivered'),
    )
    
    created=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending')
    

    def __str__(self):
        pass

    class Meta:
        ordering=('-created',)
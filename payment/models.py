from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
from django_jalali.db.models import jDateField
import jdatetime


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    shipping_full_name= models.CharField(max_length=250)
    shipping_email= models.EmailField(max_length=300)
    shipping_phone = models.CharField(max_length=24,blank=True)
    shipping_adress1 = models.CharField(max_length=240,blank=True)
    shipping_adress2 = models.CharField(max_length=240,blank=True)
    shipping_city =  models.CharField(max_length=24,blank=True)
    shipping_state =  models.CharField(max_length=24,blank=True)
    shipping_zipcode =  models.CharField(max_length=24,blank=True)
    shipping_country =  models.CharField(max_length=24,blank=True)
    shipping_old_cart = models.CharField(max_length=200,blank=True, null=True)
    
    def __str__(self):
        return f'Shipping Address From {self.shipping_full_name}'

def create_shipping_user (sender, instance, created, **kwarg):
    if created:
     user_shipping = ShippingAddress(user=instance)
     user_shipping.save()

post_save.connect(create_shipping_user,sender= User)

class Order(models.Model):
    STATUS_ORDER = [
        ('Pending', 'در انتظار پرداخت' ),
        ('Processing', 'درحال پردازش' ),
        ('Shipped', 'ارسال شده به پست' ),
        ('Delivered', 'تحویل داده شده' ),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=100)
    shipping_address= models.TextField(max_length=1500)
    amount_paid = models.DecimalField(decimal_places=0, max_digits=12)
    date_ordered = jmodels.jDateTimeField(auto_now_add=True)
    status = models.CharField(max_length=24, choices=STATUS_ORDER, default='Pending')
    last_update = jmodels.jDateTimeField(auto_now=True)

    def save(self,*args, **kwargs):
        if self.pk:
            old_status = Order.objects.get(id=self.pk).status
            if old_status!= self.status:
                self.last_update = jdatetime.datetime.now()

        super().save(*args, **kwargs)        

    def __str__(self):
        return f'order - {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=0, max_digits=12)

    def __str__(self):
        if self.user is not None:
            return f'Order Item = {self.id}- for {self.user}'
        else:
            return f'Order Item = {self.id}'

from django.db import models
import datetime 
import os
from django.contrib.auth.models import User


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_keywords = models.CharField(max_length=150, null=True, blank=True)
    meta_description = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=150, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    original_price = models.FloatField(null=True, blank=True)
    selling_price = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False, help_text='0=default, 1=Hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1=hidden')
    tag = models.CharField(max_length=150, null=True, blank=True)
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_keywords = models.CharField(max_length=150, null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    order_status = (
        ('Pending', 'Pending'),
        ('Out For Shipping', 'Out For Shipping'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=150, choices=order_status, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    pincode = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
        
    
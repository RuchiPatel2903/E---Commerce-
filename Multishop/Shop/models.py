from email import message
from itertools import product
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254)
    message = models.TextField()

    def __str__(self):
        return self.name

class Catagory(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    disc = models.TextField()
    price = models.IntegerField()
    pimage = models.ImageField(upload_to='prod_img/')
    cat_id = models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Top_product(models.Model):
    tid = models.AutoField(primary_key=True)
    prod_id = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_id.name

class Cart(models.Model):
    cid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.u_id.username

    def sub_total(self):
        return self.pid.price * self.quantity

class Wishlist(models.Model):
    wid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Product,on_delete=models.CASCADE)
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.u_id.username

class O_tracker(models.Model):
    otid = models.AutoField(primary_key=True) 
    status = models.CharField(max_length=30)
    
    def __str__(self):
        return self.status
    
class Order(models.Model):
    oid = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    amount = models.IntegerField()
    p_type = models.CharField(max_length=30)
    u_id = models.ForeignKey(User,on_delete=models.CASCADE)
    ot_id = models.ForeignKey(O_tracker,on_delete=models.CASCADE)
    odate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class O_item(models.Model):
    item_id = models.AutoField(primary_key=True) 
    o_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()


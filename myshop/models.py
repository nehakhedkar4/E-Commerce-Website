from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    locality = models.CharField(max_length=34)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    state = models.CharField(max_length=18)

    def __str__(self):
        return self.name

Category_choice = (
    ('EL','Electronics'),
    ('M','Mobiles'),
    ('F','Fashion'),
    ('H','Home'),
    ('T','Toys'),
    ('TD','Today deals'),
)

class Product(models.Model):
    product = models.CharField(max_length=25)
    selling_price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="productimg")
    category = models.CharField(choices=Category_choice,max_length=30)
    brand = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.product

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    ordered_date = models.DateField(auto_now_add=True)

    select = [
        ('Order Placed','Order Placed'),
        ('Packed','Packed'),
        ('Shipped','Shipped'),
        ('On the way','On the way'),
        ('Delivered','Delivered'),
        ]
    status = models.CharField(choices=select,max_length=20,default='Order Placed')
    
    class Meta:
        verbose_name_plural = 'OrderPlaced'

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Cart'

from django.contrib import admin
from . import models

@admin.register(models.customer)
class UserRegistration(admin.ModelAdmin):
    list_display = ('id','user','name','locality','city','pincode','state')

@admin.register(models.Product)
class UserRegistration(admin.ModelAdmin):
    list_display = ('id','product','selling_price','discount_price','description','category','brand','image')

@admin.register(models.OrderPlaced)
class UserRegistration(admin.ModelAdmin):
    list_display = ('id','user','customer','product','Quantity','ordered_date','status')

@admin.register(models.Cart)
class UserRegistration(admin.ModelAdmin):
    list_display = ('id','user','product','Quantity')
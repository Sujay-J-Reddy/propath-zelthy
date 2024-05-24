from django.db import models
from zelthy.apps.dynamic_models.models import DynamicModelBase
from zelthy.apps.dynamic_models.fields import ZForeignKey
from zelthy.core.storage_utils import ZFileField
from ..franchise.models import Franchisee
from ..academy.models import School

class Order(DynamicModelBase):
    franchise = ZForeignKey(Franchisee, on_delete=models.CASCADE)
    kits = models.JSONField(null=True)  
    items = models.JSONField(null=True) 
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)

class Vendor(DynamicModelBase):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kit(DynamicModelBase):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(DynamicModelBase):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    qty = models.PositiveIntegerField(default=0)
    last_purchase_price = models.PositiveIntegerField(default=0)
    kit = ZForeignKey(Kit, on_delete=models.SET_NULL, null=True,blank=True, related_name='kit_name')

class Log(DynamicModelBase):
    vendor = ZForeignKey(Vendor,on_delete=models.DO_NOTHING, related_name='vendor')
    items = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

class SchoolOrder(DynamicModelBase):
    school = ZForeignKey(School, on_delete=models.DO_NOTHING)
    kits = models.JSONField(null=True) 
    items = models.JSONField(null=True)  
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)


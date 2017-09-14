
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission, User


# Create your models here.
class crop(models.Model):

    cropid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=250)
    cimage = models.ImageField(upload_to = 'Desktop/', default = 'Desktop/None/no-img.jpg')
    def __str__(self):
        return self.cname

class farmer(models.Model):
    user = models.ForeignKey(User, default=1)
    fname = models.CharField(max_length=250)
    crop_details = models.ForeignKey(crop)
    #cropname = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    aadhar_no = models.IntegerField(default=0)

    def __str__(self):
        return self.fname


class qty(models.Model):
    fid = models.CharField(max_length=250)
    crop_details =  models.ForeignKey(crop)
    q = models.IntegerField
    price = models.FloatField


class retailer(models.Model):
    user = models.ForeignKey(User, default=1)
    rname = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    aadhar_no = models.IntegerField(default=0)
    def __str__(self):
        return self.rname

class r_ad_details(models.Model):
    user = models.ForeignKey(User, default=1)
    retailer_details = models.ForeignKey(retailer,blank=True, null=True)
    crop_details = models.ForeignKey(crop,blank=True, null=True)
    qty_details = models.ForeignKey(qty,blank=True, null=True)
    status_update = models.BooleanField(default = False)

class f_ad_details(models.Model):
    farmer_details = models.ForeignKey(farmer)
    crop_details = models.ForeignKey(crop)
    qty_details = models.ForeignKey(qty)
    status_update = models.BooleanField

class sell(models.Model):
    user = models.ForeignKey(User, default=1)
    farmer_details = models.ForeignKey(farmer)
    crop_details = models.ForeignKey(crop)
    retailer_details = models.ForeignKey(User , default=2, related_name="retailer_details")
    qty_sold_at = models.ForeignKey(qty)


class fcomplain(models.Model):
    user = models.ForeignKey(User, default=1)
    f = models.ForeignKey(farmer)
    complain = models.CharField(max_length=250)
    status_update = models.CharField(max_length=250,default='unread')

class rcomplain(models.Model):
    user = models.ForeignKey(User, default=1)
    r = models.ForeignKey(retailer)
    complain = models.CharField(max_length=250)
    status_update = models.CharField(max_length=250,default='unread')

from django.db import models
from django import forms
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
Car_category= [
    ('carcategory', 'Select Category'),
    ('4-door sedan', '4-Door Sedan'),
    ('station wagon', 'Station Wagon'),
    ('sports car', 'Sports Car'),
    ('2-door coupes', '2-Door Coupes'),
    ('convertibles', 'Convertibles'),
    ('mini-vans', 'Mini-vans'),
    ('suv', 'SUV'),
    ('pickup trucks', 'Pickup Trucks'),
    ('vans', 'Vans'),
    ('hatchback', 'Hatchback'),
    ]

fuel_category = [
    ('fuel type', 'Select Fuel Type'),
    ('petrol', 'Petrol'),
    ('Disel', 'Disel'),
    ('cng', 'CNG'),
    ('electric', 'Electric'),
    
    ]  

class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	uimg = models.ImageField(upload_to='Profilepics/',default='ics.jpg')
	t = [(1,'Guest'),(2,'Manager'),(3,'User')]
	role = models.IntegerField(choices=t,default=3)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	rltype = models.IntegerField(choices=f)
	pfe = models.ImageField(upload_to='Rolereqpics/',default='ics.jpg')
	is_checked = models.BooleanField(default=False)
	uname = models.CharField(max_length=50)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)



      
class Car(models.Model):
    carname = models.CharField(max_length=30)
    carprice = models.IntegerField()
    
    carmodel= models.CharField(choices=Car_category,max_length=20,default=("carcategory"))
    purchased_year = models.IntegerField()
    carfuel =  models.CharField(choices=fuel_category,max_length=20,default=("fuel type"))
    carseats = models.IntegerField()
    carkms = models.IntegerField()
    carimg = models.ImageField(upload_to='static/',default='w.jpg')
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        	return self.rname
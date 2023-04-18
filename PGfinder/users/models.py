
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
gender_ch=(("Male","male"),("Female","female"))
class Users(AbstractUser):
    is_owner=models.BooleanField(default=False)
    is_rendor=models.BooleanField(default=False,null=True)
    gender= models.CharField(choices=gender_ch,max_length=10)
    contact= models.IntegerField(default=0)
    image=models.ImageField(upload_to='Owner_images/',null=True,blank=True)
    aadhar_no=models.IntegerField(default=0)
    aadharcard= models.FileField(upload_to='Aadhar/')
    pan_no=models.IntegerField(default=0)
    pancard=models.ImageField(upload_to='Pan_images/',null=True,blank=True)
    address=models.CharField(max_length=500)
    
    class Meta:
        db_table='users'

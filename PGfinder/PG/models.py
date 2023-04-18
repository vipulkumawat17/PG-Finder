from django.db import models
from users.models import Users
from django.conf import settings
# Create your models here.
gender_ch=(("Male","male"),("Female","female"))
class PG(models.Model):
    Users = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(choices=gender_ch,max_length=10)
    rooms=models.IntegerField(default=1)
    room_sharing=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    pg_addres=models.CharField( max_length=500)

    class Meta:
        db_table='PG'
    
    def __str__(self):
        return self.name
    
pg_typech=(("AC","ac"),("Non-AC","non-ac"))
class PG_details(models.Model):
    Users = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    no_of_cupboard= models.IntegerField(default=1)
    no_of_beds=models.IntegerField(default=1)
    pg_type=models.CharField(choices=pg_typech,max_length=10)
    pgdetails_id=models.CharField(max_length=50)
    pg_image= models.ImageField(upload_to='PGimages',null=True,blank=True)
    desc=models.CharField( max_length=1000)
    room_sharing=models.IntegerField(default=0)
    area=models.CharField(max_length=500)
    near_by_place=models.CharField(max_length=200)
    
    def __str__(self):
        return self.area
    class Meta:
        db_table='PG_details'
    


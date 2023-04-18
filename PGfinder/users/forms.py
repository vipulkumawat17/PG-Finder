from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Users

class OwnerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Users
        fields=('first_name','last_name','username','gender','email','contact','aadhar_no','image','aadharcard','pan_no','pancard','address')

    @transaction.atomic
    def save(self):
        users= super().save(commit=False)
        users.is_owner = True
        users.save()
        return users
    
    
class RenderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Users
        fields=('first_name','last_name','gender','email','contact','address')

    @transaction.atomic
    def save(self):
        users= super().save(commit=False)
        users.is_render = True
        users.save()
        return users

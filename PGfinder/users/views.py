from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import Users
from .forms import OwnerRegisterForm,RenderRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.core.mail import send_mail

def Home(request):
    return render(request,'user/dashboard.html')

def Service(request):
     return render(request,'user/Service.html')

def AboutUs(request):
     
     return render(request,'user/AboutUs.html')

def ContactUs(request):
     return render(request,'user/ContactUs.html')

def Help(request):
     return render(request,'user/Help.html')

class OwnerRegisterView(CreateView):
    model=Users
    form_class= OwnerRegisterForm
    template_name= 'user/ownerregister.html'
    success_url="/"

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'owner'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        users = form.save()
        login(self.request,users)
        self.sentmail(users.email)
        return super().form_valid(form)
    
    def sentmail(self,user_mail):
        subject= 'Register manager successfully '
        message= 'Thanks for register'
        email_from= settings.EMAIL_HOST_USER
        recipient_list=[user_mail]
        send_mail(subject,message,email_from,recipient_list)
             
        return HttpResponse('mail sent')
    
class RenderRegisterView(CreateView):
    model=Users
    form_class= RenderRegisterForm
    template_name= 'user/renderregister.html'
    #success_url="/"

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'render'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        users = form.save()
        login(self.request,users)
        self.sentmail(users.email)
        return super().form_valid(form)
    
    def sentmail(self,user_mail):
        subject= 'Register manager successfully '
        message= 'Thanks for register '
        email_from= settings.EMAIL_HOST_USER
        recipient_list=[user_mail]
        send_mail(subject,message,email_from,recipient_list)
             
        return HttpResponse('mail sent')
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_owner:
                return '/pg/addpg/'
            else:
                return '/rendor/'
            
class UserLogoutView(LogoutView):
    template_name= 'user/logout.html'
    success_url="/home/"


   
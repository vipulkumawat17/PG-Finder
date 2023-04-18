from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import PG,PG_details
from .form import AddPGform,AddPGdetailsform
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PgView(CreateView):
    model= PG
    form_class=AddPGform
    template_name='PG/registerpg.html'
    success_url='../addpgdetail/'

class PgDetailView(CreateView):
    model= PG_details
    form_class=AddPGdetailsform
    template_name='PG/addpgdetail.html'
    success_url='/'

    def get(self, request, *args, **kwargs):
        pg = PG.objects.get(id=id)
        pgd=PG_details.objects.get(id=id)

        return render(request,'PG/pgdetails.html',{'pglist':pg,'pgdetails':pgd})


class PgListView(ListView):
    def get(self, request, *args, **kwargs):
        
        pg = PG.objects.all().values()
        
        return render(request, 'PG/pglist.html',{
            'pglist':pg,
        })

    template_name = 'user/manager_dashboard.html'
class PgUpdateView(UpdateView):
    model=PG
    template_name='PG/pgupdate.html'
    fields='__all__'
    success_url='./pglist.html'

class PgDetailsUpdateView(UpdateView):
    model=PG_details
    template_name='PG/pgdetailsupdate.html'
    fields='__all__'
    success_url='./pglist.html'

class PgDeleteView(DeleteView):
    model=PG
    template_name='PG/pgdelete.html'
    success_url='./pglist.html'

class PgGetDetailsView(DetailView):
    template_name = 'PG/pgdetails.html'
    def get(self, request,id, *args, **kwargs):
        pg = PG.objects.get(id=id)
        pgd=PG_details.objects.get(id=id)

        return render(request,'PG/pgdetails.html',{'pglist':pg,'pgdetails':pgd})
    template_name = 'PG/pgdetails.html'







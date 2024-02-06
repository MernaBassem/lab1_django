from django.shortcuts import render,reverse
from django.contrib.auth.forms import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

def MyLogin(request):
    context={'form',authenticate()}
    return render (request ,  'registration/login.html',context)
def MyProfile(request):
    return HttpResponseRedirect(reverse("product"))
def myLogOut(request):
    return render(request, 'registration/logged_out.html')
class myRegister(CreateView):
    model=User
    template_name =  'registration/register.html'
    context_object_name="form"
    form_class = UserCreationForm
    success_url=reverse_lazy('login')


# class myRegister(CreateView):
#     model=User
#     template_name = 'registration/register.html'
#     context_object_name ="form"
#     form_class = UserCreationForm
#     success_url=reverse_lazy('MyLogin')
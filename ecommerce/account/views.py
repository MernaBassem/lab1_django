from django.shortcuts import render,reverse
from django.contrib.auth.forms import authenticate
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def MyLogin(request):
    context={'form',authenticate()}
    return render (request ,  'registration/login.html',context)
def MyProfile(request):
    return HttpResponseRedirect(reverse("product"))
def myLogOut(request):
    # return render(request, 'registration/logged_out.html')
    return HttpResponseRedirect(reverse('MyLogin'))
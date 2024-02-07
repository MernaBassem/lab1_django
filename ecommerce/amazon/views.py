from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import UpdateView 

from django.views.generic.detail import DetailView
from .models import Product


    
def product(request):
    query = request.GET.get('search', '') 
    
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()

    context = {'products': products, 'search_value': query}
    return render(request, 'pages/product.html', context)
@login_required()
def add(request):
    if(request.method=="POST"):
        Product.objects.create(title=request.POST['title'],
                                category=request.POST['category'],
                                price=request.POST['price'],
                                image=request.POST['image'],
                                img=request.FILES['img']
                                )    
        return redirect('product') 
    return render(request, 'pages/add.html')

# -------------------------------------------------------------
@login_required()
def addForm(request):
    form = ProductForm()
    context={'form':form}
    if request.method == "POST":
        form=ProductForm(request,request.POST,request.FILES)
        if(form.is_valid):
                Product.objects.create(title=request.POST['title'],
                            category=Category.objects.get(id=request.POST['category']),
                            price=request.POST['price'],
                            image=request.POST['image'],
                            img=request.FILES['img']
                            ) 
                
                return HttpResponseRedirect(reverse("product"))
        else:
            context['msg']="complete your data please!"
    return render(request, 'pages/addForm.html',context)
# ---------------------------------------------------------------

# -----------------------------------------------
# @login_required
class productUpdateView(UpdateView):
    model=Product
    template_name = 'pages/updateForms.html'
    context_object_name='form'
    form_class= ProductForm
    success_url=reverse_lazy('product')
    

#-----------------------------------

@login_required()
def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    product_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
# .................
class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/productDetail.html'
    context_object_name = 'product'

def category(request):
    context = {'products': Product.objects.all()}
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')


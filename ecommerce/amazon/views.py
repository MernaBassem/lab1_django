from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
# from django.views.generic import UpdateView , ListView

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
# class ProductUpdateView(UpdateView):
#     model=Product
#     template_name = 'pages/updateForms.html'
#     context_object_name='form'
#     form_class= ProductForm
#     success_url=reverse_lazy('product')
    

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
    
    
    
# def productDetail(request, productID):
#     product = next((p for p in Product.objects.all() if p.id == productID), None)
#     context = {'product': product}
#     if product:
#         return render(request, 'pages/productDetail.html', context)
#     return HttpResponse('<span style="color:red">Product not found</span>')

# ---------------------

# class productDetail(ListView):
#     model = Product
#     template_name = 'pages/productDetail.html'
#     context_object_name = 'product'




def category(request):
    context = {'products': Product.objects.all()}
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')


# @login_required()
# def update(request, productID):
#     product = get_object_or_404(Product, id=productID)
#     context = {'product': product}

#     if request.method == 'POST':
#         name = request.POST['name']
#         category = request.POST['category']
#         price = request.POST['price']
#         image = request.POST['image']

#         if name and category and price and image:
#             product.title = name
#             product.category = category
#             product.price = price
#             product.image = image
#             product.save()
#             return redirect('productDetail', productID=product.id)
#         else:
#             if(request.POST['name'] == '') : 
#               product.title = ''
#             if(request.POST['category'] == '') : 
#               product.category = ''
#             if(request.POST['price'] == '') : 
#               product.price = ''
#             if(request.POST['image'] == '') : 
#               product.image = ''
#             context['msg'] = 'All fields are required'

#     return render(request, 'pages/update.html', context)
#--------------update


# @login_required
# def UpdateForm(request, productID):
#     product = Product.objects.get(id=productID)
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("product"))
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'pages/updateForm.html', {'form': form})



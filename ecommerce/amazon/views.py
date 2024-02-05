from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import *
def product(request):
    query = request.GET.get('search', '') 
    
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()

    context = {'products': products, 'search_value': query}
    return render(request, 'pages/product.html', context)

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

# ----------------------



def addForm(request):
    form = ProductForm()
    context={'form':form}
    if(request.method=="POST"):
        
        Product.objects.create(title=request.POST['title'],
                                category=request.POST['category'],
                                price=request.POST['price'],
                                image=request.POST['image'],
                                img=request.FILES['img']
                                )    
        return redirect('product') 
    return render(request, 'pages/addForm.html',context)
# -------------------------------------------------------------
# def addForm(request):
#     form = ProductForm()
#     context={'form':form}
#     if request.method == "POST":
#         form=ProductForm(request,request.POST,request.FILES)
#         if(form.is_valid()):
#             Product.objects.create(title=request.POST['title'],
#                         category=request.POST['category'],
#                         price=request.POST['price'],
#                         image=request.POST['image'],
#                         img=request.FILES['img']
#                         ) 
         
#             return HttpResponseRedirect(reverse("product"))
#         else:
#             context['msg']="complete your data please!"
#     return render(request, 'pages/addForm.html',context)
# ---------------------------------------------------------------


# def addForm(request):
#     form = ProductForm()
#     context={'form':form}
#     if request.method == "POST":
#         form=ProductForm(request,request.POST,request.FIELS)
#         if(form.is_valid()):

#             product_id = request.POST.get('id')
#             title = request.POST.get('title')
#             price = request.POST.get('price')
#             category = request.POST.get('category')
#             image = request.POST.get('image') 
#             img = request.FILES.get('img') 

        
#             Product.objects.create(
#                 id=product_id,
#                 title=title,
#                 price=price,
#                 category=category,
#                 image=image,
#                 img=img
#             )
#             r=reverse("product")
#             return HttpResponseRedirect(r)
#         else:
#             context['msg']="complete your data please!"
#     return render(request, 'pages/addForm.html',context)
  




def delete_product(request, product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)
    product_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def productDetail(request, productID):
    product = next((p for p in Product.objects.all() if p.id == productID), None)
    context = {'product': product}
    if product:
        return render(request, 'pages/productDetail.html', context)
    return HttpResponse('<span style="color:red">Product not found</span>')

def update(request, productID):
    product = get_object_or_404(Product, id=productID)
    context = {'product': product}

    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        price = request.POST['price']
        image = request.POST['image']

        if name and category and price and image:
            product.title = name
            product.category = category
            product.price = price
            product.image = image
            product.save()
            return redirect('productDetail', productID=product.id)
        else:
            if(request.POST['name'] == '') : 
              product.title = ''
            if(request.POST['category'] == '') : 
              product.category = ''
            if(request.POST['price'] == '') : 
              product.price = ''
            if(request.POST['image'] == '') : 
              product.image = ''
            context['msg'] = 'All fields are required'

    return render(request, 'pages/update.html', context)


def category(request):
    context = {'products': Product.objects.all()}
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')

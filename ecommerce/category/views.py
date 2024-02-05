from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category
from django.shortcuts import render, get_object_or_404

def categoryList(request):
    query = request.GET.get('search', '') 
    
    if query:
        Categorys = Category.objects.filter(title__icontains=query)
    else:
        Categorys = Category.objects.all()

    context = {'Categorys': Categorys, 'search_value': query}
    return render(request, 'pages/categoryList.html', context)

def addCategory(request):
    if(request.method=="POST"):
        Category.objects.create(title=request.POST['title'],
                                )    
        return redirect('categoryList') 
    return render(request, 'pages/addCategory.html')

# -------------------------------------------------------------



def delete_category(request, category_id):
    Category_to_delete = get_object_or_404(Category, pk=category_id)
    Category_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



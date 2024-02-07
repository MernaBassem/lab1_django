from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView
def categoryList(request):
    query = request.GET.get('search', '') 
    
    if query:
        Categorys = Category.objects.filter(title__icontains=query)
    else:
        Categorys = Category.objects.all()

    context = {'Categorys': Categorys, 'search_value': query}
    return render(request, 'pages/categoryList.html', context)
@login_required()
# def addCategory(request):
#     if(request.method=="POST"):
#         Category.objects.create(title=request.POST['title'],
#                                 )    
#         return redirect('categoryList') 
#     return render(request, 'pages/addCategory.html')



def addCategory(request):
    form = CategoryForm()
    context={'form':form}
    if (request.method=='POST'):
        form=CategoryForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(reverse('categoryList'))
    return render (request, 'pages/categoryForm.html',context)


# -------------------------------------------------------------
# @login_required
class categoryUpdateView(UpdateView):
    model = Category
    template_name = 'pages/categoryUpdate.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categoryList')

# @login_required()
# def delete_category(request, category_id):
#     Category_to_delete = get_object_or_404(Category, pk=category_id)
#     Category_to_delete.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class delete_category(DeleteView):
    model = Category
    template_name = 'pages/categoryDelete.html'
    success_url = reverse_lazy('categoryList')

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import AppForm

from .models import App

def app_list_view(request):
    obj = App.objects.all()
    context = {
        'object': obj
    }
    return render(request, "apps/app_all.html", context)

def app_detail_view(request):
    obj = App.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "apps/app_all.html", context)

def app_create_view(request):
    form = AppForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('success')
        form = AppForm()

    context = {
        'form': form
    }
    return render(request, "apps/app_create.html", context)

def app_delete_view(request, id):
    obj = get_object_or_404(App, id=id) # model, lookupparameter id
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "apps/app_delete.html", context)
    
def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def dynamic_look_view(request, id):
    obj = App.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "apps/app_detail.html", context)


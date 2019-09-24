from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    ListView
)

from .forms import AppForm
from .models import App 

class AppObjectMixin(object):
    model = App
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

class AppsView(AppObjectMixin, View):
    template_name = "apps/app_detail.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

class AppListView(ListView):
    template_name = "apps/app_list.html"
    queryset = App.objects.all()
# class AppListView(ListView):
#     # template_name = "apps/app_list.html"
#     # queryset = App.objects.all()

#     # def get_queryset(self):
#     #     return self.queryset

#     # def get(self, request, *args, **kwargs):
#     #     context = {'object_list': self.get_queryset()}
#     #     return render(request, self.template_name, context)

class AppCreateView(View):
    template_name = "apps/app_create.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = AppForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppForm()
        context = {"form": form}
        return render(request, self.template_name, context)

class AppUpdateView(AppObjectMixin, View):
    template_name = "apps/app_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(App, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = AppForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = AppForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class AppDeleteView(AppObjectMixin, View):
    template_name = "apps/app_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/apps/')
        return render(request, self.template_name, context)

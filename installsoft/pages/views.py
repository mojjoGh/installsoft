from django.shortcuts import render

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)
def about_view(request, *args, **kwargs):
    context = {}
    return render(request, "about.html", context)
def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, "contact.html", context)

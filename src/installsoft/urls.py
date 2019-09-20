from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view, contact_view

urlpatterns = [
    path('apps/', include('apps.urls')), # import include
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
# end of custom code
    path('admin/', admin.site.urls),
]

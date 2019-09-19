from django.contrib import admin
from django.urls import path

from pages.views import home_view, about_view, contact_view
from apps.views import (
    app_list_view,
    app_create_view,
    app_delete_view,
    dynamic_look_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # app urls
    path('apps/', app_list_view, name='app-list'),
    path('apps/<int:id>/', dynamic_look_view, name='app-detail'),
    path('apps/<int:id>/delete/', app_delete_view, name='app-delete'),
    path('apps/create/', app_create_view, name='app-create'),
# end of custom code
    path('admin/', admin.site.urls),
]

from django.urls import path

from .views import (
    app_list_view,
    app_create_view,
    app_delete_view,
    dynamic_look_view
)

app_name = 'apps'
urlpatterns = [
    path('', app_list_view, name='app-list'),
    path('<int:id>/', dynamic_look_view, name='app-detail'),
    path('<int:id>/delete/', app_delete_view, name='app-delete'),
    path('create/', app_create_view, name='app-create'),
]

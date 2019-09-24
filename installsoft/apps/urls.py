from django.urls import path

from .views import (
    AppsView,
    AppListView,
    AppCreateView,
    AppUpdateView,
    AppDeleteView
)

app_name = 'apps'
urlpatterns = [
    path('', AppListView.as_view(), name='apps-list'),
    path('<int:id>/', AppsView.as_view(), name='apps-detail'),
    path('<int:id>/delete/', AppDeleteView.as_view(), name='apps-delete'),
    path('<int:id>/update/', AppUpdateView.as_view(), name='apps-update'),
    path('create/', AppCreateView.as_view(), name='apps-create'),
]

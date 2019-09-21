from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,          
)

app_name = 'articles' # for namespacing
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), # default is pk not id , --> views>get_object
    path('create/', ArticleCreateView.as_view(), name='article-create'),    
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
]
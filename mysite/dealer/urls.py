from django.urls import path
from . import views
from django.views.generic import TemplateView

# TODO: include year, month in general views

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'dealer'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    # path('main/create/', views.CatCreate.as_view(), name='cat_create'),  
    # path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    # path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),  

    # path('breed/', views.BreedView.as_view(), name='breed_list'),
    # path('breed/create/', views.BreedCreate.as_view(), name='breed_create'),  
    # path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    # path('breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),  

]

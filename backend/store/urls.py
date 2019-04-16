from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('api/', views.ListVar.as_view()),
    path('api/<int:pk>/', views.DetailVar.as_view()),
]

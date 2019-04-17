from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('api/word/', views.ListWord.as_view()),
    path('api/word/<int:pk>/', views.DetailWord.as_view()),
    path('api/variable/', views.ListVar.as_view()),
    path('api/variable/<int:pk>/', views.DetailVar.as_view()),
]

from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD:cooking/urls.py
    path('list/', views.variable_list, name='variable_list')
=======
    path('search/', views.index, name='search'),
>>>>>>> upstream/master:store/urls.py
]

from django.urls import path,include
from rest_framework import routers
from ChefedeCozinha import views

from . import views

routers = routers.DefaultRouter()

routers.register(r'getAllSet',views.getAllSet)

urlpatterns = [
    path('',views.index,name='index'),
    path('getAll',views.getAll,name="getAll"),
    path('<int:produto_id>',views.getId,name='produto'),
    path('postProduto/<int:produto_id>',views.postProduto,name="postProduto"),
    path('editProduto/<int:produto_id',views.editProduto,name="editProduto"),
    path('delProduto/<int:produto_id',views.delProduto,name="delProduto")
]
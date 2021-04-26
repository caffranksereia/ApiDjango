from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import models

from ChefedeCozinha.serializers import CardapioSerializer



class (viewsets.ModelViewSet):
    """
        Api Endepoint that allows  users
    """ 
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def getAll(request):
    listProduto = produto.objects('produto_id')
    template = loader.get_template('polls/template/index.html')
    context = {
        'listProduto':listProduto,
    }
    return HttpResponse(template.render(context,request))

def getId(request):
    return HttpResponse("hello getId")

def postProduto(request):
    return HttpResponse("hello post")

def editProduto(request):
    return HttpResponse("hello edit")

def delProduto(request):
    return HttpResponse("hello delete")
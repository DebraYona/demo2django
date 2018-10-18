from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from transaccion.models import Banco
from transaccion.serializers import *
# Create your views here.


class ListCreateBanco(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView ):

    queryset =Banco.objects.all()
    serializer_class= BancoSerializer

    def get(self, request, *args, **kwargs):
        print(request)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

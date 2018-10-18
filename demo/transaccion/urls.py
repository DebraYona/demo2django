from django.urls import path
from transaccion import views

urlpatterns=[
    path('bancos/',views.ListCreateBanco.as_view()),
]

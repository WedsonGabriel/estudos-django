from django.urls import path
from . import views

app_name = 'imc'
urlpatterns = [path('index/', views.calcular_imc, name='calculadora_imc')]
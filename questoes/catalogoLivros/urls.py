from django.urls import path
from . import views

app_name = 'catalogoLivros'
urlpatterns = [
    path('index/', views.pagina_catalogoLivros, name='catalogoDeLivros'),
    path('buscar-tabela/', views.buscar_tabela, name='buscarTabela'),
]
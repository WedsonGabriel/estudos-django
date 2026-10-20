from django.urls import path
from . import views

app_name = 'controleDespesas'
urlpatterns = [
    path('index/', views.pagina_controleDespesas, name='controleDeDespesas'),
    path('showTabela', views.mostrar_tabela, name='tabelaDespesas')
]
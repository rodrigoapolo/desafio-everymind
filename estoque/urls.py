from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-produto', views.cadastrar_produto, name='cadastrar_produto'),
    path('update-produto', views.update_produto, name='update_produto'),
    path('delete-produto', views.delete_produto, name='delete_produto'),
]

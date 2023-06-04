from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
# router.register('cliente', views.ClienteView)
# router.register('endereco', views.EnderecoView)
# router.register('conta', views.ContaView)
# router.register('cartao', views.CartaoView)

urlpatterns = [
    path('cliente/', view=views.ClienteListCreate.as_view()),
    path('cliente/<int:pk>', view=views.ClienteDetailView.as_view()),

    path('endereco/', view=views.EnderecoListCreate.as_view()),
    path('endereco/<int:pk>', view=views.EnderecoDetailView.as_view()),

    path('conta/', view=views.ContaListCreate.as_view()),
    path('conta/<int:pk>', view=views.ContaDetailView.as_view()),

    path('cartao/', view=views.CartaoListCreate.as_view()),
    path('cartao/<int:pk>', view=views.CartaoDetailView.as_view()),

    path('transacoes/', view=views.TransacoesListCreate.as_view()),
    path('transacoes/<int:pk>', view=views.TransacoesDetailView.as_view()),

    path('emprestimos/', view=views.EmprestimosListCreate.as_view()),
    path('emprestimos/<int:pk>', view=views.EmprestimosDetailView.as_view()),
] + router.urls

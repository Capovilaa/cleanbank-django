from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
import base64 
from django.core.files.base import ContentFile
from rest_framework.response import Response

def base64_file(data, name):    
    format, img_str = data.split(';base64,')
    ext = 'png'
    return ContentFile(base64.b64decode(img_str), name='{}.{}'.format(name, ext))

# CLIENTES
class ClienteListCreate(ListCreateAPIView):    
    permission_classes = (IsAuthenticated, )
    queryset = Cliente.objects.all()
    serializer_class = SerializerCliente

    def get_queryset(self):
        queryset = Cliente.objects.all()
        cpf_res = self.request.query_params.get("cpf_cliente")
        if cpf_res is not None:
            queryset = queryset.filter(cpf_cliente=cpf_res)
            return queryset        
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(" ")[1]
        dados_TOKEN = AccessToken(token)
        usuario = dados_TOKEN['user_id']
        print(usuario)
        criacao = CustomUser.objects.get(pk=usuario)
        print(criacao)
        dados = request.data

        criar = Cliente.objects.create(nome=dados['nome'], cpf_cliente=dados['cpf_cliente'], email=dados['email'],  foto=base64_file(dados['foto'],'PERFIL'), data_nascimento=dados['data_nascimento'], user=criacao )
        criar.save()

        serializer = SerializerCliente(criar)

        return Response(serializer.data)
    

    
class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Cliente.objects.all()
    serializer_class = SerializerCliente



# ENDERECO
class EnderecoListCreate(ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = SerializerEndereco


class EnderecoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Endereco.objects.all()
    serializer_class = SerializerEndereco



# CONTA
class ContaListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Conta.objects.all()
    serializer_class = SerializerConta

    def get_queryset(self):
        queryset = Conta.objects.all()
        id_res = self.request.query_params.get("cliente_id")
        if id_res is not None:
            queryset = queryset.filter(cliente_id=id_res)
            return queryset        
        return super().get_queryset()



class ContaDetailView(RetrieveUpdateDestroyAPIView):    
    permission_classes = (IsAuthenticated, )
    queryset = Conta.objects.all()
    serializer_class = SerializerConta

    

# CARTAO
class CartaoListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Cartao.objects.all()
    serializer_class = SerializerCartao    


class CartaoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Cartao.objects.all()
    serializer_class = SerializerCartao



# TRANSACOES
class TransacoesListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Transacoes.objects.all()
    serializer_class = SerializerTransacoes

    def get_queryset(self):
        queryset = Transacoes.objects.all()
        id_res = self.request.query_params.get("cliente_id")
        if id_res is not None:
            queryset = queryset.filter(cliente_id=id_res)
            return queryset        
        return super().get_queryset()


class TransacoesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Transacoes.objects.all()
    serializer_class = SerializerTransacoes



# EMPRÉSTIMO
class EmprestimosListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Emprestimo.objects.all()
    serializer_class = SerializerEmprestimo


class EmprestimosDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Emprestimo.objects.all()
    serializer_class = SerializerEmprestimo
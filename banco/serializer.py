from rest_framework import serializers
from .models import *


class SerializerCliente(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf_cliente', 'email',
        'foto', 'data_nascimento', 'data_abertura', 'user']
        


class SerializerEndereco(serializers.ModelSerializer):
    class Meta: 
        model = Endereco
        fields = ['id', 'cliente', 'logradouro', 'bairro', 'cidade', 'uf', 'cep']



class SerializerConta(serializers.ModelSerializer):
    class Meta: 
        model = Conta
        fields = ['id', 'cliente', 'agencia', 'conta', 'saldo', 'situacao_cartao']



class SerializerCartao(serializers.ModelSerializer):
    class Meta: 
        model = Cartao
        fields = ['id', 'cliente', 'conta', 'numero', 'validade', 'cvv', 'bandeira', 'situacao']        



class SerializerTransacoes(serializers.ModelSerializer):
    class Meta: 
        model = Transacoes
        fields = ['id', 'cliente', 'tipo_transacao', 'valor', 'destinatario', 'data']        



class SerializerEmprestimo(serializers.ModelSerializer):
    class Meta: 
        model = Emprestimo
        fields = ['id', 'conta', 'valor_solicitado', 'valor_final', 'juros', 'quantidade_parcelas', 'valor_parcelas', 'data_solicitacao']        



from django.contrib.auth.models import AbstractUser
from django.db import models
from config import settings
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
    

class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, password, **extra_fields):
        if not cpf:
            raise ValueError(_("Precisa passar o cpf"))        
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
 

class CustomUser(AbstractUser):
    username = None
    cpf = models.CharField(max_length=18, unique=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.cpf
    


class Cliente (models.Model):    
    nome = models.CharField(max_length=40)
    cpf_cliente = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='media/', null=True)
    data_nascimento = models.DateField()
    data_abertura = models.DateField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome  



class Endereco (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=25)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=15)



class Conta (models.Model): 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agencia = models.CharField(max_length=4)
    conta = models.CharField(max_length=9)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)    
    situacao_cartao = models.BooleanField(default=False)
    


class Cartao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    numero = models.CharField(max_length = 10)
    validade = models.DateField()
    cvv = models.CharField(max_length = 5)
    bandeira = models.CharField(max_length = 5)
    situacao = models.CharField(max_length = 50)



class Transacoes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_transacao = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    destinatario = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)



class Emprestimo(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor_solicitado = models.DecimalField(max_digits=12, decimal_places=2)
    valor_final = models.DecimalField(max_digits=12, decimal_places=2)
    juros = models.DecimalField(max_digits=12, decimal_places=2)
    quantidade_parcelas = models.IntegerField()
    valor_parcelas = models.DecimalField(max_digits=12, decimal_places=2)
    data_solicitacao = models.DateField(auto_now=True)
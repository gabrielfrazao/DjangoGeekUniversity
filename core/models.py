from django.db import models

# Create your models here.


#Criando uma classe produto por herança
class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField("Quantidade em estoque")


    def __str__ (self):
        return self.nome

class Pacientes(models.Model):
    nome = models.CharField('nome', max_length=100)
    idade = models.IntegerField('idade')
    sexo = models.CharField('sexo', max_length=10)
    email = models.EmailField('E-mail', max_length=100)

#Criando Função para exibição dos campos.
    def __str__(self):
        return f'{self.nome} {self.idade} {self.sexo} {self.email}'





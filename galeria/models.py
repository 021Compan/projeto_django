from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Membro [nome={self.nome}]"

class Post(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Post [nome={self.nome}]"

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)


    def __str__(self):
        return f"Produto [nome={self.nome}]"

class Hero(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Hero [nome={self.nome}]"

class Hero_membro(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Membro [nome={self.nome}]"
    
class Evento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Membro [nome={self.nome}]"
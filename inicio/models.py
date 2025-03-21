from django.db import models


class Questoes(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

# Modelo para Alternativa
class Alternativa(models.Model):
    texto = models.CharField(max_length=255)
    is_correta = models.BooleanField(default=False)
    explicacao = models.TextField()

# Modelo para Pergunta
class Pergunta(models.Model):
    texto = models.CharField(max_length=255)
    alternativas = models.ManyToManyField(Alternativa)
    questao = models.ForeignKey(Questoes, on_delete=models.CASCADE)
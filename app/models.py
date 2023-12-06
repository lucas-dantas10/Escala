from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Escala(models.Model):
    nome = models.CharField(max_length=255)
    start_at = models.TimeField()

class Missa(models.Model):
    escala_id = models.ForeignKey(Escala, on_delete=models.CASCADE)

class Participacao(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    missa_id = models.ForeignKey(Missa, on_delete=models.CASCADE)
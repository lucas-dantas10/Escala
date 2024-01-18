from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Escala(models.Model):
    name = models.CharField(max_length=255)
    start_at = models.TimeField()

    class Meta:
        db_table = 'tb_escala'

class Missa(models.Model):
    escala = models.ForeignKey(Escala, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_missa'

class Participacao(models.Model):
    ministro = models.ForeignKey(User, on_delete=models.CASCADE)
    missa = models.ForeignKey(Missa, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = 'tb_participacao'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Escala(models.Model):
    name = models.CharField(max_length=255)
    start_at = models.TimeField()

    class Meta:
        db_table = 'tb_escala'

class Missa(models.Model):
    escala_id = models.ForeignKey(Escala, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_missa'

class Participacao(models.Model):
    ministro_id = models.ForeignKey(User, on_delete=models.CASCADE)
    missa_id = models.ForeignKey(Missa, on_delete=models.CASCADE),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),

    class Meta:
            db_table = 'tb_participacao'
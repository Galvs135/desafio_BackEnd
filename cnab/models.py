from django.db import models


class CnabFile(models.Model):
    type = models.CharField(max_length=1)
    date = models.DateField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    credit_card = models.CharField(max_length=12)
    hour = models.TimeField(max_length=6)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)
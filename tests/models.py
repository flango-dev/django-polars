from django.db import models


class BuiltinFieldModel(models.Model):
    int: models.IntegerField = models.IntegerField()
    bigint: models.BigIntegerField = models.BigIntegerField()
    float: models.FloatField = models.FloatField()
    decimal: models.DecimalField = models.DecimalField(max_digits=3, decimal_places=2)
    text: models.TextField = models.TextField()

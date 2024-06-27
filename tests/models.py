from django.db import models


class PkBuiltinFieldModel(models.Model):
    int: models.IntegerField = models.IntegerField(primary_key=True)
    bigint: models.BigIntegerField = models.BigIntegerField()
    float: models.FloatField = models.FloatField()
    decimal: models.DecimalField = models.DecimalField(max_digits=3, decimal_places=2)
    text: models.TextField = models.TextField()


class BuiltinFieldModel(models.Model):
    # https://docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields
    int: models.IntegerField = models.IntegerField()
    bigint: models.BigIntegerField = models.BigIntegerField()
    float: models.FloatField = models.FloatField()
    decimal: models.DecimalField = models.DecimalField(max_digits=3, decimal_places=2)
    text: models.TextField = models.TextField()


class View(models.Model):
    bigint: models.BigIntegerField = models.BigIntegerField()
    float: models.FloatField = models.FloatField()
    decimal: models.DecimalField = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = "view"

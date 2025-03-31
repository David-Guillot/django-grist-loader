from django.db import models


class GristModel(models.Model):
    class Meta:
        abstract = True

    external_id = models.PositiveBigIntegerField(primary_key=True)

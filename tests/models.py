from django.db import models

from grist_loader.models import GristModel


class ModelA(GristModel):
    field_a = models.CharField(max_length=100, blank=True)
    field_b = models.IntegerField(null=True, blank=True)


class ModelB(GristModel):
    fk_to_a = models.ForeignKey(ModelA, on_delete=models.CASCADE, null=True, blank=True)
    m2m_to_a = models.ManyToManyField(ModelA)

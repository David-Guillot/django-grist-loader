import factory

from . import models


class ModelAFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ModelA

    external_id = factory.Sequence(lambda n: n)
    field_a = factory.Sequence(lambda n: f"A {n}")
    field_b = factory.Sequence(lambda n: n)


class ModelBFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ModelB

    external_id = factory.Sequence(lambda n: n)
    relation_to_a = factory.SubFactory(ModelAFactory)

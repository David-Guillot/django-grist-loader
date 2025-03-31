from pytest_factoryboy import register

from . import factories

register(factories.ModelAFactory)
register(factories.ModelAFactory, "model_a_other")
register(factories.ModelBFactory)

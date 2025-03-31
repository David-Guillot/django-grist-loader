from grist_loader.loader import GristLoader

from .models import ModelA, ModelB


class ModelALoader(GristLoader):
    table = "TableA"
    model = ModelA
    required_cols = ("col_a",)
    fields = {
        "col_a": ModelA.field_a,
        "col_b": ModelA.field_b,
    }


class ModelBLoader(GristLoader):
    table = "TableB"
    model = ModelB
    required_cols = ("col_reference_to_a",)
    fields = {
        "col_reference_to_a": ModelB.fk_to_a,
        "col_references_to_a": ModelB.m2m_to_a,
    }

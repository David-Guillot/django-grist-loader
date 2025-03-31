import pytest

from grist_loader.loader import gristapi

from .models import ModelA, ModelB
from .grist import ModelALoader, ModelBLoader


@pytest.mark.django_db
def test_load_model_a(monkeypatch, model_a):
    # GIVEN we have one ModelA
    assert ModelA.objects.count() == 1
    existing = ModelA.objects.first()
    assert existing.pk == model_a.pk
    assert existing.field_a != "Custom field a"

    # GIVEN the Grist API returns some TableA
    def mock_list_records(*args, **kwargs):
        return 200, [
            {"id": model_a.pk, "col_a": "Custom field a", "col_b": 12},
            {"id": 2, "col_a": "Other custom field a", "col_b": 47},
        ]

    monkeypatch.setattr(gristapi, "list_records", mock_list_records)

    # WHEN loading ModelA
    ModelALoader().load()

    # THEN we have 2 ModelA
    # the existing one had its field_a updated
    assert ModelA.objects.count() == 2
    assert set(ModelA.objects.values_list("pk", flat=True)) == {model_a.pk, 2}
    existing.refresh_from_db()
    assert existing.field_a == "Custom field a"
    assert ModelA.objects.get(pk=2).field_a == "Other custom field a"


@pytest.mark.django_db
def test_load_model_b(monkeypatch, model_a, model_a_other):
    # GIVEN we have no ModelB
    assert not ModelB.objects.exists()

    # GIVEN the Grist API returns one TableB
    def mock_list_records(*args, **kwargs):
        return 200, [
            {"id": 1, "col_reference_to_a": model_a.pk, "col_references_to_a": ["L2", model_a.pk, model_a_other.pk]},
        ]

    monkeypatch.setattr(gristapi, "list_records", mock_list_records)

    # WHEN loading ModelB
    ModelBLoader().load()

    # THEN we have 1 ModelB
    # no new ModelA has vbeen created
    # Fk is pointing to model_a
    # m2m field is referencing model_a and model_a_other
    assert ModelA.objects.count() == 2
    assert ModelB.objects.count() == 1
    model_b = ModelB.objects.first()
    assert model_b.fk_to_a == model_a
    assert set(model_b.m2m_to_a.all()) == {model_a, model_a_other}

import polars as pl
import pytest
from django.db import connection
from polars.testing import assert_frame_equal

from django_polars.io import read_frame
from tests.models import BuiltinFieldModel, PkBuiltinFieldModel, View


@pytest.fixture
def builtin_field_model_dataframe() -> pl.DataFrame:
    data = {
        "int": [1, 2],
        "bigint": [100000, 200000],
        "float": [0.1, 0.2],
        "decimal": [0.01, 0.02],
        "text": ["bla", "blub"],
    }
    return pl.DataFrame(data)


@pytest.fixture
def builtin_field_model_fixture() -> None:
    BuiltinFieldModel.objects.create(
        int=1, bigint=100000, float=0.1, decimal=0.01, text="bla"
    )
    BuiltinFieldModel.objects.create(
        int=2, bigint=200000, float=0.2, decimal=0.02, text="blub"
    )
    return None


@pytest.fixture
def builtin_view_dataframe() -> pl.DataFrame:
    data = {
        "bigint": [100000, 200000],
        "float": [0.1, 0.2],
        "decimal": [0.01, 0.02],
    }
    return pl.DataFrame(data)


@pytest.fixture
def pk_builtin_field_model_fixture() -> None:
    PkBuiltinFieldModel.objects.create(
        int=1, bigint=100000, float=0.1, decimal=0.01, text="bla"
    )
    PkBuiltinFieldModel.objects.create(
        int=2, bigint=200000, float=0.2, decimal=0.02, text="blub"
    )
    return None


@pytest.mark.django_db
def test_df_builtin_field_type_model_df_roundtrip(builtin_field_model_dataframe):
    for cols in builtin_field_model_dataframe.rows(named=True):
        BuiltinFieldModel.objects.create(
            int=cols["int"],
            bigint=cols["bigint"],
            float=cols["float"],
            decimal=cols["decimal"],
            text=cols["text"],
        )

    df_out = read_frame(con=connection, qs=BuiltinFieldModel.objects.filter(int=1))
    assert_frame_equal(builtin_field_model_dataframe.slice(0, 1), df_out)

    s = pl.Series("id", [1, 2])
    builtin_field_model_dataframe.insert_column(0, s)
    df_out_1 = read_frame(
        con=connection, qs=BuiltinFieldModel.objects.filter(int=1), drop_id=False
    )
    assert_frame_equal(builtin_field_model_dataframe.slice(0, 1), df_out_1)


@pytest.mark.django_db
def test_pk_model_to_df(pk_builtin_field_model_fixture, builtin_field_model_dataframe):
    df_out = read_frame(
        con=connection, qs=PkBuiltinFieldModel.objects.all(), drop_id=False
    )
    assert_frame_equal(builtin_field_model_dataframe, df_out)


@pytest.mark.django_db
def test_view_to_df(builtin_view_dataframe, builtin_field_model_fixture):
    assert "tests_builtinfieldmodel" in connection.introspection.table_names()

    with connection.cursor() as c:
        c.execute(
            "CREATE VIEW view AS SELECT id, bigint, float, decimal FROM tests_builtinfieldmodel;"
        )

    df_out = read_frame(con=connection, qs=View.objects.all())

    assert_frame_equal(builtin_view_dataframe, df_out)

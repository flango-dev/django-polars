import polars as pl
import pytest
from django.db import connection
from polars.testing import assert_frame_equal

from django_polars.io import read_frame
from tests.models import BuiltinFieldModel


@pytest.mark.django_db
def test_df_builtin_field_type_model_df_roundtrip():
    data = {
        "int": [1, 2],
        "bigint": [100000, 200000],
        "float": [0.1, 0.2],
        "decimal": [0.01, 0.02],
        "text": ["bla", "blub"],
    }
    df_in = pl.DataFrame(data)
    for cols in df_in.rows(named=True):
        BuiltinFieldModel.objects.create(
            int=cols["int"],
            bigint=cols["bigint"],
            float=cols["float"],
            decimal=cols["decimal"],
            text=cols["text"],
        )

    df_out = read_frame(con=connection, qs=BuiltinFieldModel.objects.filter(int=1))
    assert_frame_equal(df_in.slice(0, 1), df_out)

    s = pl.Series("id", [1, 2])
    df_in.insert_column(0, s)
    df_out_1 = read_frame(
        con=connection, qs=BuiltinFieldModel.objects.filter(int=1), drop_idx=False
    )
    assert_frame_equal(df_in.slice(0, 1), df_out_1)

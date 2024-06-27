from django.db.models.query import QuerySet
from polars import DataFrame, read_database
from polars.type_aliases import ConnectionOrCursor


def read_frame(
    con: ConnectionOrCursor, qs: QuerySet, drop_idx: bool = True
) -> DataFrame:
    raw_sql = qs.query.__str__()
    df = read_database(query=raw_sql, connection=con)
    if drop_idx:
        df.drop_in_place("id")
    return df

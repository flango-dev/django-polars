from django.db.models.query import QuerySet
from polars import DataFrame, read_database
from polars.type_aliases import ConnectionOrCursor
from sqlglot import transpile


def read_frame(
    con: ConnectionOrCursor, sel: QuerySet | str, drop_id: bool = True
) -> DataFrame:
    if isinstance(sel, QuerySet):
        raw_sql = sel.query.__str__()
    else:
        transpile(sel)
        raw_sql = sel
    df = read_database(query=raw_sql, connection=con)
    if drop_id:
        df.drop_in_place("id")
    return df

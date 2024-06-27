# django-polars

Like [django-pandas](https://github.com/chrisdev/django-pandas/) but [way faster](https://pola.rs/posts/benchmarks/), with support for [parallel DataFrame processing](https://docs.pola.rs/user-guide/migration/pandas/#polars-has-more-support-for-parallel-operations-than-pandas) and  [larger-than-memory DataFrame processing](https://docs.pola.rs/user-guide/lazy/execution/#execution-on-larger-than-memory-data).

Uses [polars](https://github.com/pola-rs/polars) under the hood.

## Usage

Head over to test code in `tests/test_*`.

Conceptually `polars` differs from `pandas`.
E.g. [`polars` does not have a multi-index/index](https://docs.pola.rs/user-guide/migration/pandas/#polars-does-not-have-a-multi-indexindex)
and a different behavior w.r.t. [missing data](https://docs.pola.rs/user-guide/migration/pandas/#missing-data).
As a consequence `django-polars` will not be API-compatible with `django-pandas`.
Refer to the [migration from `pandas` user guide](https://docs.pola.rs/user-guide/migration/pandas/) for more information.

## Limitations

- Reading a `DataFrame` via `django_polars.io.read_frame(...)` with an [asynchronous connection is unstable ATM](https://docs.pola.rs/api/python/stable/reference/api/polars.read_database.html#polars-read-database).

## Contribution

We appreciate [contributions](https://github.com/flango-dev/django-polars/blob/main/CONTRIBUTING.md).

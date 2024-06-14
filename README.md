# django-polars

Like [django-pandas](https://github.com/chrisdev/django-pandas/) but [way faster](https://pola.rs/posts/benchmarks/), with support for [parallel DataFrame processing](https://docs.pola.rs/user-guide/migration/pandas/#polars-has-more-support-for-parallel-operations-than-pandas) and  [larger-than-memory DataFrame processing](https://docs.pola.rs/user-guide/lazy/execution/#execution-on-larger-than-memory-data).

Uses [polars](https://github.com/pola-rs/polars) under the hood.

## Development

- Fork this project in GitHub,
- [install `rye`](https://rye.astral.sh/guide/installation/),
- create a `.venv` with `rye sync`,
- add production and test code,
- run `rye run precommit`,
- create PR.
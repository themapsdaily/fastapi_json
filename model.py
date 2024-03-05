from sqlalchemy import Column, Integer, String, Table, MetaData

metadata = MetaData()

example_table = Table(
    "title",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("state_ut", String),
    Column("year", String),
    Column(data_column, Float)
)

import sqlite3
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = "datafile.sqlite"
engine = create_engine("sqlite:///%s" % dbPath)
metadata = MetaData(engine)
people = Table(
    "people",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("count", Integer),
)
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship
from Src.Circle import Circle

metadata = MetaData()

circles = Table(
    'circles', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('radius', Integer),
    Column('centerX', Integer),
    Column('centerY', Integer),
)

def start_mappers():
    mapper(Circle, circles)
   

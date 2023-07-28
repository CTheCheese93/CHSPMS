from orm.db_session import db_session

from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    query: db_session.query_property()

# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# Base.query = db_session.query_property()
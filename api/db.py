import os

from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

from api.models import Base


# Database configuration
def get_url():
    return os.getenv("DATABASE_URL", "sqlite:///sqllite3.db")


# Database engine creation using SQLAlchemy
_engine = create_engine(get_url())
# Session creation
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=_engine))


# Creates db schema
def init_db():
    Base.metadata.create_all(bind=_engine)

init_db()

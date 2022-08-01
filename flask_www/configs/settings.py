from flask_www.configs import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


mysqldb_url = app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(mysqldb_url, echo=True, pool_size=20, max_overflow=0)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
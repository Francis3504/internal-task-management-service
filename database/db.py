from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from core.url import DATABASE_URL

engine=create_engine(DATABASE_URL,echo=True)

Session=sessionmaker(expire_on_commit=False,autoflush=False,bind=engine)

Base=declarative_base()
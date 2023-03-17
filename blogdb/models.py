from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Text


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'posts'
    
    id = mapped_column('id', Integer, primary_key=True, autoincrement=True)
    title = mapped_column('title', String(250), nullable=False)
    date = mapped_column('date', String(250), nullable=False)
    body = mapped_column('body', Text, nullable=False)
    author = mapped_column('author', String(250), nullable=False)
    img_url = mapped_column('img_url', String(250), nullable=False)
    subtitle = mapped_column('subtitle', String(250), nullable=False)

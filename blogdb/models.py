from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'posts'
    
    id = mapped_column('id', Integer, primary_key=True, autoincrement=True)
    title = mapped_column('title', String(100), nullable=False)
    subtitle = mapped_column('subtitle', String(100), nullable=False)
    content = mapped_column('content', String(1000), nullable=False)

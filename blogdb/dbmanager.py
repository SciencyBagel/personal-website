import sqlalchemy
from sqlalchemy.orm import Session

from blogdb.models import Post, Base


class DBManager:
    def __init__(self, connection_string: str):
        # Create engine
        self.engine = sqlalchemy.create_engine(connection_string, echo=True)

        # Create tables if they don't exist
        Base.metadata.create_all(self.engine)

    def get_posts(self):
        with Session(self.engine) as session:
            stmt = sqlalchemy.select(Post)
            posts = session.scalars(stmt).all()
            return posts

    def get_post(self, post_id: int):
        with Session(self.engine) as session:
            stmt = sqlalchemy.select(Post).where(Post.id == post_id)
            post = session.scalar(stmt)
            return post
        
    def delete_post(self, post_id: int) -> None:
        with Session(self.engine) as session:
            stmt = sqlalchemy.select(Post).where(Post.id == post_id)
            post = session.scalar(stmt)
            session.delete(post)
            session.commit()
            
    def add_post(self, post: Post):
        with Session(self.engine) as session:
            session.add(post)
            session.commit()
            

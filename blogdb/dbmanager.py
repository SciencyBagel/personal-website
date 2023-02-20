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
            posts = session.query(Post).all()
            return posts

    def get_post(self, post_id: int):
        with Session(self.engine) as session:
            post = session.query(Post).filter(Post.id == post_id).first()
            return post

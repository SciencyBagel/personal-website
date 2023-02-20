from sqlalchemy.orm import Session
from sqlalchemy import Engine
from models import Post


class DataIO:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_posts(self):
        with Session(self.engine) as session:
            posts = session.query(Post).all()
            return posts

    def get_post(self, post_id: int):
        with Session(self.engine) as session:
            post = session.query(Post).filter(Post.id == post_id).first()
            return post

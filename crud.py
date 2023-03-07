from sqlalchemy.orm import Session
from sqlalchemy import desc
from models import Post


def get_post(db: Session, post_id_list: list):
    return db.query(Post).filter(Post.id.in_(post_id_list)).order_by(Post.created_date).all()
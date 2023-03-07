from sqlalchemy.orm import Session
from models import Post


def get_post(db: Session, post_id_list: list):
    return db.query(Post).filter(Post.id.in_(post_id_list)).order_by(Post.created_date).all()

def delete_post(db: Session, post_id: int):
    db.query(Post).filter(Post.id == post_id).delete()
    db.commit()
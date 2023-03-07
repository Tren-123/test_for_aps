from sqlalchemy import Column, Integer, Text, DateTime
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_date = Column(DateTime)
    rubrics = Column(Text)
    
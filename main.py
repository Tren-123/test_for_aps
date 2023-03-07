from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from sqlalchemy.orm import Session
from crud import get_post
from database import SessionLocal
from settings import *


# Create the elastic client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
)
app = FastAPI()


# create db session instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Text(BaseModel):
    text: str


@app.post("/search/")
def search_by_text(text: Text,  db: Session = Depends(get_db)):
    query = {
    "match": {
      "text": text.text
    }}
    elastic_search_results = client.search(index=INDEX_NAME, query=query, size=20)["hits"]["hits"]
    if elastic_search_results:
        ids_list = []
        for item in elastic_search_results:
            ids_list.append(item["_source"]["id"])
        db_search_results = get_post(db, post_id_list=ids_list)
        return db_search_results
    return elastic_search_results
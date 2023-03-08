from typing import List
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from sqlalchemy.orm import Session
from crud import get_post, delete_post
from schemas import PostBase, DeleteResponse
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


class TextToSearch(BaseModel):
    text: str


@app.post("/search/")
def search_by_text(text: TextToSearch,  db: Session = Depends(get_db)) -> List[PostBase]:
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
    return []
    

@app.post("/delete/{post_id}", responses = {200: {"model": DeleteResponse}, 400: {"model": DeleteResponse}})
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    query = {
    "term": {
      "id": post_id
    }}
    elastic_document = client.search(index=INDEX_NAME, query=query)["hits"]["hits"]
    if elastic_document:
        elastic_document_id = elastic_document[0]["_id"]
        client.delete(index=INDEX_NAME, id=elastic_document_id)
        delete_post(db, post_id=post_id)
        return JSONResponse(status_code=200, content={"detail": f"Post with id:{post_id} deleted from index and database successfully"})
    return JSONResponse(status_code=400, content={"detail": f"Post with id:{post_id} not in index"})

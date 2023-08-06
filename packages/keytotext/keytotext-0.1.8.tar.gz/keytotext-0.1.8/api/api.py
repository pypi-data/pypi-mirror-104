from fastapi import FastAPI, Query
from typing import List
from keytotext.pipeline import pipeline

app = FastAPI()


def generate(keywords, model="k2t"):
    nlp = pipeline(model)
    return nlp(keywords)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api")
def k2t_post(data: List[str]):
    return {
        "keywords": data,
        "text": generate(data)
    }


@app.get("/api")
def k2t_get(data: List[str] = Query(...)):
    return {
        "keywords": data,
        "text": generate(data)
    }

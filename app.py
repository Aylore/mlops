from fastapi import FastAPI
import logging
from data_models import SamplePostRequest

app = FastAPI()
logging.basicConfig(level=logging.INFO)


@app.get("/")
def home():
    return "Welcome home "


@app.post("/predict")
def predict(request : SamplePostRequest):

    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    return [request.a  + request.b[0], request.c]
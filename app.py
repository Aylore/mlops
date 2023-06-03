from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Fuck you "
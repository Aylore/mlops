from fastapi.testclient import TestClient
from app import app


client = TestClient(app)




def test_predict():

    payload = {"a": 1,  "b":[1, 2] , "c" :"This is string"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()[0] == 2
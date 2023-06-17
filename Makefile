install:
        pip install -r requirements.txt


lint:
        pylint main.py

test:
        python -m pytest -vv tests/


run:
        uvicorn app:app --reload --host 0.0.0.0 --port 8000



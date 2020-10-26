## Wizeline Golang bootcamp assessment

This is a simple REST API built on Python + Flask
This project can be either run with [Python](#run-with-python) or [Docker](#run-with-docker)

### Run with python
```sh
pip install -r requirements.txt
cd app/
export FLASK_APP=server.py
flask run
```

### Run with docker 
```sh
docker build -t wize-assessment .
docker run wize-assessment
```


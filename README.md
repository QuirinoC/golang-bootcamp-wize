## Wizeline Golang bootcamp assessment

This is a simple REST API built on Python + Flask
This project can be either run with [Python](#run-with-python) or [Docker](#run-with-docker)

### Endpoints

* GET / | Returns a simple Hello, World
* GET /pokedex?pokemon={pokemon_name} | Given a `pokemon_name` it returns the names of the games the pokemon has appeared at 

### Example
[http://localhost:8080/pokedex?pokemon=squirtle](http://localhost:8080/pokedex?pokemon=squirtle)
[http://localhost:8080/pokedex?pokemon=pikachu](http://localhost:8080/pokedex?pokemon=pikachu)

### Run with python
```sh
cd app/
pip install -r requirements.txt
export FLASK_APP=server.py
flask run
```

### Run with docker 
```sh
cd app/
docker build -t wize-assessment .
docker run -it -p 8080:8080 wize-assessment
```


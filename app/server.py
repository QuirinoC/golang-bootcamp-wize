from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
POKE_URL = "https://pokeapi.co/api/v2/pokemon/{}"


@app.route('/', methods=['GET'])
def root():
    return jsonify({"data": "Hello, World"})


@app.route('/pokedex', methods=['GET'])
def pokedex():
    '''
        Get the names the pokemon appears at
    '''
    pokemon_name = request.args.get('pokemon')
    data = requests.get(POKE_URL.format(pokemon_name))
    if data.status_code != 200:
        return jsonify({"error": "Pokemon not found"})

    games = []
    for game in data.json().get("game_indices", {}):
        if game.get('version', {}).get('name'):
            games.append(game['version']['name'])

    return jsonify({"data": games})

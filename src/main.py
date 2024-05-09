from pokemon_repository import PokemonRepository
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world again"}


@app.get("/allPokemon")
def get_users():
    repo = PokemonRepository()
    return repo.get_all_pokemon()


@app.get("/pokemon/{pokedex_number}")
def get_user(pokedex_number: int):
    repo = PokemonRepository()
    return repo.get_pokemon_by_pokedex_number(pokedex_number)


@app.get("/pokemon/{pokedex_number}/{name}")
def get_user(pokedex_number: int, name: str):
    repo = PokemonRepository()
    return repo.get_pokemon_by_pokedex_number_and_name(pokedex_number, name)

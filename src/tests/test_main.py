from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_info():
    response = client.get("/pokemon/4/Charmander")
    assert response.status_code == 200
    assert response.json() == {
    "Pokedex_Number": 4,
    "Name": "Charmander",
    "Type_1": "Fire",
    "Type_2": None,
    "Total_Stats": 309,
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Sp_Atk": 60,
    "Sp_Def": 50,
    "Speed": 65,
    "Generation": 1,
    "Legendary": 0
}
import requests

# Definir la URL base del servidor Flask
SERVER_URL = 'http://localhost:5000'

def register_team(team_name):
    url = f'{SERVER_URL}/register_team'
    data = {'team_name': team_name}
    response = requests.post(url, json=data)
    return response.json()

def join_team(team_name, player_name):
    url = f'{SERVER_URL}/join_team'
    data = {'team_name': team_name, 'player_name': player_name}
    response = requests.post(url, json=data)
    return response.json()

def start_game():
    url = f'{SERVER_URL}/start_game'
    response = requests.post(url)
    return response.json()

def roll_dice():
    url = f'{SERVER_URL}/roll_dice'
    response = requests.post(url)
    return response.json()

def game_status():
    url = f'{SERVER_URL}/game_status'
    response = requests.get(url)
    return response.json()

# Ejemplo de uso
if __name__ == '__main__':
    # Registrar un equipo
    register_team('Equipo A')

    # Unirse a un equipo
    join_team('Equipo A', 'Jugador 1')

    # Iniciar el juego
    start_game()

    # Realizar tirada de dado
    roll_dice()

    # Obtener estado del juego
    game_status()
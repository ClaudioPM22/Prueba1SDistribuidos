from flask import Flask,request,jsonify,render_template
import random  

app = Flask(__name__)

teams = {}
game_started = False
turn_order = []
current_team_index = 0
board_size = 100
max_dice_value = 6

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register_team', methods=['POST'])
def register_team():
    team_name = request.json['team_name']
    teams[team_name] = []
    return jsonify({'message': f'Team {team_name} registered successfully.'})

@app.route('/join_team', methods=['POST'])
def join_team():
    team_name = request.json['team_name']
    player_name = request.json['player_name']
    if team_name not in teams:
        return jsonify({'error': f'Team {team_name} does not exist.'}), 404
    teams[team_name].append(player_name)
    return jsonify({'message': f'Player {player_name} joined team {team_name}.'})

@app.route('/start_game', methods=['POST'])
def start_game():
    global game_started, turn_order
    if len(teams) < 2:
        return jsonify({'error': 'At least 2 teams are required to start the game.'}), 400
    if game_started:
        return jsonify({'error': 'Game has already started.'}), 400
    game_started = True
    turn_order = list(teams.keys())
    random.shuffle(turn_order)
    return jsonify({'message': 'Game started.', 'turn_order': turn_order})

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    global current_team_index
    if not game_started:
        return jsonify({'error': 'Game has not started yet.'}), 400
    team_name = turn_order[current_team_index]
    roll_result = random.randint(1, max_dice_value)
    teams[team_name].append(roll_result)
    current_team_index = (current_team_index + 1) % len(turn_order)
    return jsonify({'team': team_name, 'roll_result': roll_result})

@app.route('/game_status', methods=['GET'])
def game_status():
    if not game_started:
        return jsonify({'message': 'Game has not started yet.'})
    if max(sum(scores) for scores in teams.values()) >= board_size:
        winner = max(teams, key=lambda team: sum(teams[team]))
        return jsonify({'message': f'Game over. Team {winner} wins!', 'scores': teams})
    else:
        return jsonify({'message': 'Game in progress.', 'scores': teams})

if __name__ == '__main__':
    app.run(debug=True)


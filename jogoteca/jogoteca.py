from flask import Flask, render_template, request, redirect


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('God of War', 'Rack n Slash', 'PS2')
game3 = Game('Mortal Kombat', 'Luta', 'PS2')
game_list = [game1, game2, game3]


app = Flask(__name__)

@app.route('/')


def index():
   
    return render_template('game-list.html', title='Jogos', games = game_list)

@app.route('/newgame')

def new_game():
    return render_template("new-game.html", title='Novo Jogo')

@app.route("/create", methods=['POST',])

def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Game(nome, categoria, console)
    game_list.append(jogo)
    return redirect('/')


app.run(debug=True)
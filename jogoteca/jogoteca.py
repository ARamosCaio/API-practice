from flask import Flask, render_template


class game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


app = Flask(__name__)

@app.route('/home')

def greeting():
    game1 = game('Tetris', 'Puzzle', 'Atari')
    game2 = game('God of War', 'Rack n Slash', 'PS2')
    game3 = game('Mortal Kombat', 'Luta', 'PS2')
    game_list = [game1, game2, game3]
    return render_template('game-list.html', title='Jogos', games = game_list)

@app.route('/newgame')

def new_game ():
    return render_template("new_game.html", title='Novo Jogo')


app.run()
from flask import Flask, render_template 
import raspieats
from raspieats import Game
import catchem


app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/catchem')
def catchemOne():
    print("catchemOne")
    return render_template('catchem.html')
    

@app.route('/game')
def game():
    my_game = Game()
    my_game.run()

@app.route('/game2')
def game2():
    return "Game2 ran"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



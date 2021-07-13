from flask import Flask, render_template

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def index() :
  lista = ['https://www.youtube.com/embed/jJ7p8ObqbHk', 'https://www.youtube.com/embed/vJ-3mQLKxSU', 'https://www.youtube.com/embed/0LB3FSfjvao', 'https://www.youtube.com/embed/N1hTsbW50eM']
  return render_template('index.html', lista=lista)
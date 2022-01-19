from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'please work'

from . import routes

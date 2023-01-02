"""Main package for source code."""

from flask import Flask

from src import routes


app = Flask(__name__)
app.register_blueprint(routes.bp)
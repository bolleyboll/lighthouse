from flask import Flask

app = Flask(__name__)

from light import routes

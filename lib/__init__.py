# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)
# app.config.from_pyfile('config.py')
app.config.from_object('lib.server.config')

# avoid circular reference, must imort views after
# initializing app
from server import views  

# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

# avoid circular reference, must imort views after
# initializing app
from lib import views  
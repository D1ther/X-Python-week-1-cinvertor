"""
Імпортування всіх обробників сторінок, для їх роботи
"""

from flask import (
    Flask,
)

# Об'єкт класу Flask
app = Flask(__name__)

from app.routs import *

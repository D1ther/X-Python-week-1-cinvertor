"""
обробляється головна сторінка, на неї нічого не передається
"""

from flask import (
    render_template,
)
from app import app

#  обробник головної сторінки
@app.route('/')
def main_menu_foots():
    """відображення головної функції"""
    return render_template('main_menu.html')

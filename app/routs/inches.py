"""
модуль відображення сторінки з перетворення футів в дюйми
"""

from flask import (
    render_template,
    request,
)

from app import app
from app.convertor import convert_feets

# обробник перетворення в дюйми
@app.route('/inches', methods=['POST', 'GET'])
def transform_inches():
    """отримання даних для перетворення та перетворення"""
    if request.method == 'POST':
        feet = request.form.get('feet')
        inches = convert_feets(feet=feet, numb=12)
    else:
        inches = 0
    return render_template('transformation.html', result=inches)

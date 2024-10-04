"""
модуль відображення сторінки з перетворення футів в дюйми
"""

from flask import (
    render_template,
    request,
)

from app import app
from app.convertor import convert_feets
    
# обробник перетворення в ярди
@app.route('/yards', methods=['POST', 'GET'])
def transform_yards():
    """отримання даних для перетворення та перетворення"""
    if request.method == 'POST':
        feet=request.form.get('feet')
        yards=convert_feets(feet=feet, numb=0.333333333)
    else:
        yards=0
    return render_template('transformation.html', result=yards) 

"""
модуль відображення сторінки з перетворення футів в милі
"""

from flask import(
    render_template,
    request,
)

from app import app 
from app.convertor import convert_feets
    
# обробник перетворення в милі
@app.route('/miles', methods=['POST', 'GET'])
def transform_miles():
    """отримання даних для перетворення та перетворення"""
    if request.method == 'POST':
        feet=request.form.get('feet')
        miles=convert_feets(feet=feet, numb=0.000189393939)
    else:
        miles='0'
    return render_template('transformation.html', result=miles)

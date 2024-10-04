"""
Функція конвертування
"""

def convert_feets(feet:int, numb:int):
    """функція конвертація футів в милі"""
    # якщо даних не отримано, то ярди = 0
    if feet == '':
        miles = 0
    else:
        feet = int(feet)
        miles = feet*numb # результат
    return miles

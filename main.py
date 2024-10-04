"""
Файл запуску 
"""

from app import app

# Головна функція
def main():
    """налаштування запуску сервераі"""
    app.run(port=5000, debug=True, host='0.0.0.0')

if __name__ == '__main__':
    main()

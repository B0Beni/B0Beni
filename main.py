# каркасный вариант конструктора сайта фласк
from flask import Flask, url_for, Markup, request


app = Flask(__name__)# создаем приложение
@ app.route('/')  # функции декоратора
@ app.route('/index')
def index():
    return 'Адмирал!<br><a href="/poster">Слоган</a>'
@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" type= "text/css href="{url_for('static',filename='css/style.css')}">
</head>
<body>
<h1 class="red">Постер к фильму</h1>
<img src="{url_for('static',filename='images/admiral3.jpg')}"
alt="Картинка не нашлась">
<p>И крепка, как смерть, любовь!</p>
</body>
</html>"""


@ app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start!')
    return '<br>'.join(lst)
@ app.route('/slogan')

def slogan():
        return 'Ибо крепка, как смерть, любовь!<br><a href="/">Назад</a>'
if __name__ == '__main__':
    # запускаем приложение именновыми аргументами порты и хосты
    # эмулятор сервера
    app.run(host='127.0.0.1', port=5000, debug=True)
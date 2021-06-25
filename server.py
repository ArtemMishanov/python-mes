# save this as app.py
import time
from datetime import datetime

from flask import Flask, request
import json


app = Flask(__name__)


#  https://build-system.fman.io/qt-designer-download
#  pip --trusted-host=pypi.org --trusted-host=files.pythonhosted.org install pyqt6
#  Создали мини БД
database = [
    {
        'name': 'Jack-Sparrow',
        'text': 'Hello word!',
        'time': 0.01
    },
    {
        'name': 'Mary',
        'text': 'Hello, Captain Jack-Sparrow!',
        'time': 0.02
    },
]


#  @app.route("/") - Серверный метод выглядет как декоратор
@app.route("/")
def hello():
    return "Hello, SkillBox! <a href='/status'>Статус</a><br></br><a href='/s2'> off </a>"


#  Дополнить метод статус, чтобы он также возвращал
#  -общее количество пользователей (уникальных имен) и сообщений на сервере.
@app.route("/status")
def status():
   message = {
       "Status": "True",
       "Name": "Artem-Messanger",
       "time": datetime.now().strftime('%H:%M'),
       "UserCount": uniqu_name_list(),
       "MessagesCount": len(database),
       'MessagesAll': database[:30]
       #'time6': datetime.now().strftime('%H:%M:%S')

   }
   return json.dumps(message, ensure_ascii = False)


def uniqu_name_list():
    #  Альтернативный:
    # set - объект "Множество"  может содержать только уникальные елементы
    # count = len(set(message['name'] for message in database))

    x = []
    i = 0
    count = 0
    if isinstance(database[0], dict):
        while i < len(database):
            if database[i]['name'] not in x:
                x.append(database[i]['name'])
            i += 1
            count = str(len(x))
    else:
        count = 0

    #  Альтернативный:
    # for element in database:
    #     if element['name'] not in x:
    #         x.append(element['name'])
    #     else:
    #         continue

    #  return (f"Users in chatt:  {len(x)}")
    return (f"Пользователей вчате:   {len(x)}")


@app.route("/s2")
def s2():
  return "off"



#  Создали метод добавления элемента словаря с ключами
#  Данный метод работает только на получение инфы от клиента
#  metods=['POST']) - указали в декораторе что он поддерживает только пост метод!!!
@app.route("/send", methods=['POST'])
def send_message():
    #request - метод, импортированный из Flask. Хранит информацию о текущем запросе
    data = request.json  # TODO validate

    #  Если данные не являються словарем - не продолжать
    if not isinstance(data, dict):
        return abort(400)

    #  Проверяю что в объекте словарь есть ключи(если есть это не подмененный)
    if 'name' not in data or 'text' not in data:
        return abort(400)


    name = data['name']
    text = data['text']

    print(name)
    print (len(name))
    print(type(name))

    #  Отсееваем пустые сообщения
    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)

    if not (0 < len(name) < 128):
        return abort(400)

    #  Text длина сообщения не более 1000 символов
    if not (0 < len(text) < 1000):
        return abort(400)


    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)

    #  print(database)  # TODO remove

    #  Базовая идея реализации Бота
    if '/help' == text:
        database.append({
            'name': 'Bot',
            'text': 'Привет я Бот, работаю автономно',
            'time': time.time()
        })


    return {'ok': True}



@app.route("/messages")
def get_messages():

    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []  # Временная БД, объявленная как пустой список

    for message in database:
        if message['time'] > after:
            messages.append(message)  # В цикле перебираем все СВЕЖИЕ (отсортированные по времени) сообщениея и копируем во временную БД

    #  return messages - Json Не принимает список. Только словарь или строку
    #  messages[:50]  - За раз можно получить не более 50 сообщений.
    #  Каждый раз при подгрузке сообщений сервер больше нагружаеться
    return {'messages': messages[:50]}



app.run()  # тогда будет запускаться по дефолту
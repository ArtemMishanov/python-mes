#  Файл клиент который обращаеться к server.py метод get_messages():
#  Програмка которая ПОЛУЧАЕТ сообщения
from datetime import datetime
import time
import requests


# Создаем метод вывода сообщение из ДБ-Словаря, по индексу сообщения в БД
def print_messages(messages):
    # В цикле печатаем все переданные сообщения
    for message in messages:
        dt = datetime.fromtimestamp(message['time'])
        # f - строка отформатированная по заданному шаблону
        # print(f'{dt.hour}:{dt.minute}', message['name'])
        print(dt.strftime('%H:%M:%S'),  message['name']) # Выведи дату в формате и Имя пославшего сообщение
        print(message['text'])  # Выведи текст сообщения
        print()  # Выведи разделитель "пустая строкой"


after = 0
#  Данный цикл выполняеться бесконечно
while True:
    response = requests.get(
        url='http://127.0.0.1:5000/messages',
        params={'after': after}
    )
    messages = response.json()['messages']

    #  Получаем только новые сообщения
    #  Получаем время последнего сообщения и просим сервер выслать все сообщения после последнего
    if messages:
        print_messages(messages)
        after = messages[-1]['time']

    time.sleep(2)  #  Проверять есть-ли новые сообщения каждые 2 сек

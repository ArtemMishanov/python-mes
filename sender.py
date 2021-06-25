#  Сдесь реализован клиент нашего сервера
#  Програмка которая ПОСЫЛАЕТ сообщения на сервер
import requests



name = input('Введите имя: ')  # Позволяет ввести текст из консоли в реальном времени

while True:
    text = input()  #

    response = requests.post(
        url='http://127.0.0.1:5000/send',
        json={'name': name, 'text': text }
    )


#  Использовали в начале как ТЕСТ
#  print(response.status_code)
#  print(type(response.text))
#  print(response.text)

import datetime
import time

print('https://replit.com/@Levashov/messenger')

# print(time.time())
# dt = datetime.datetime.fromtimestamp(time.time())
# print(dt)

# dt = datetime.datetime.now()
# print(dt)
# print(dt.year)

# 100
# 100.5
# 'Привет'
# [100, 200, 300, 'четыреста', [0, 1, 2]]
# {
#     'name': 'Jack',
#     'text': 'Привет всем!',
#     'time': '2021-06-07 21:00:00'
# }

# Создали список и наполнили словарями с ключами: name, text, time
#  Jack, Mary, Artem, Anton
database = [
    {
        'name': 'Jack',
        'text': 'Привет всем!',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Привет, Jack!',
        'time': time.time()
    },
    {
        'name': 'Artem',
        'text': 'Привет, Jack and Marry!',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Привет, Artem!',
        'time': time.time()
    },
    {
        'name': 'Jack',
        'text': 'Привет, Jack! How are you?',
        'time': time.time()
    },
    {
        'name': 'Anton',
        'text': 'Привет, Jack! Привет Marry',
        'time': time.time()
    },
]


def uniqu_name_list():
    x = []
    i = 0

    while i < len(database):
        if database[i]['name'] not in x:
            x.append(database[i]['name'])
        i += 1
        #  print('At index {} the letter is {}' .format(index_count,letter))
    return ('Пользователей в чате:  {}'.format(len(x)))




# Создали метод добавления элемента словаря с ключами
def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)


# Вызываем метод чтобы добавить элемент
send_message('admin', 'Я щас вас заблочу')
send_message('Jack', 'Не надо не блочь')


# Создаем метод вывода сообщение из ДБ-Словаря, по индексу сообщения в БД
def print_messages(messages):
    # В цикле печатаем все переданные сообщения
    for message in messages:
        dt = datetime.datetime.fromtimestamp(message['time'])
        # f - строка строка отформатированная по заданному шаблону
        # print(f'{dt.hour}:{dt.minute}', message['name'])
        print(dt, message['name'])  # Выведи дату в формате и Имя пославшего сообщение
        print(message['text'])  # Выведи текст сообщения
        print()  # Выведи разделитель "пустая строкой"


def get_messages(after):
    messages = []  # Временная БД, объявленная как пустой список
    for message in database:
        if message['time'] > after:
            messages.append(message)  # В цикле перебираем все СВЕЖИЕ (отсортированные по времени) сообщениея и копируем во временную БД

    return messages


#  Выводим только НОВЫЕ сообщения относительно последнего
print_messages(get_messages(0))



class ExampleApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()  #  Проводим инициализацию самого виджета, чтобы потом можно было добавить свои методы
        self.setupUi(self)

        # class Ui_MainWindow(object):

        app = QtWidgets.QApplication([])  # Обертка главного App-который управляет окнами

        windows = ExampleApp()  # Создаем окошко которое стаовиться экземпляром этого класса
        #  Автоматически вызываеться мметод - def __init__(self):

        windows.show()

        app.exec()  # Обертка главного App-который
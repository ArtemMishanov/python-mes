import requests
from PyQt6 import QtWidgets, QtCore
import client_ui
from datetime import datetime


class Messenger(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):

    def __init__(self):
        super().__init__()  #  Проводим инициализацию самого виджета,
        # чтобы потом можно было добавить свои методы
        self.setupUi(self)

        #  Событие нажатия кнопки "Отправка сообщения"
        self.pushButton.pressed.connect(self.send_message)

        #  Получение сообщения от сервера каждые 2 сек.
        self.after = 0
        self.timer = QtCore.QTimer()  # Отдельная часть библиотеки PyQt
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(2000)  # 1000-milisec = 1 sec.


    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(
                url='http://127.0.0.1:5000/send',
                json={'name': name, 'text': text}
            )
        except:
            self.textBrowser.append('Сервер недоступен')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Неправильное имя или текст')
            self.textBrowser.append('')
            return

        self.textEdit.clear()  # Чистим поле ввод текста

    # Создаем метод вывода сообщение из ДБ-Словаря, по индексу сообщения в БД
    def show_messages(self, messages):
        #  В цикле печатаем все переданные сообщения
        for message in messages:
            dt = datetime.fromtimestamp(message['time'])
            firstLine = dt.strftime('%H:%M:%S') + ' ' + message['name']

            self.textBrowser.append(firstLine)
            self.textBrowser.append(message['text'])
            self.textBrowser.append(' ')



    def get_messages(self):

        try:
            response = requests.get(
                url='http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
            messages = response.json()['messages']
        except:
            return

        #  Получаем только новые сообщения
        #  Получаем время последнего сообщения и просим сервер выслать все сообщения после последнего
        if messages:
            self.show_messages(messages)
            self.after = messages[-1]['time']



app = QtWidgets.QApplication([])  # Обертка главного App-который управляет окнами
windows = Messenger()  # Создаем окошко которое стаовиться экземпляром этого класса
        #  Автоматически вызываеться мметод - def __init__(self):
windows.show()
app.exec()  # Обертка главного App-который
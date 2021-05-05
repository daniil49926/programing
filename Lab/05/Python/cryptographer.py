from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QImage

from sys import argv, exit


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"textEdit")
        self.text_edit.setGeometry(QRect(0, 0, 600, 761))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 200, 391, 171))
        self.push_button = QPushButton(self.centralwidget)
        self.push_button.setObjectName(u"pushButton")
        self.push_button.setGeometry(QRect(605, 150, 295, 51))
        self.push_button_2 = QPushButton(self.centralwidget)
        self.push_button_2.setObjectName(u"pushButton_2")
        self.push_button_2.setGeometry(QRect(605, 100, 295, 51))
        self.push_button_3 = QPushButton(self.centralwidget)
        self.push_button_3.setObjectName(u"pushButton_3")
        self.push_button_3.setGeometry(QRect(605, 50, 295, 51))
        self.push_button_4 = QPushButton(self.centralwidget)
        self.push_button_4.setObjectName(u"pushButton_4")
        self.push_button_4.setGeometry(QRect(605, 0, 295, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0443\u0442 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.push_button_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.push_button_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.push_button_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi


def set_bit(img, ind, val):
    pixel = ind // 3
    horizon = pixel % img.width()
    vertical = pixel // img.width()
    px = ind % 3
    if px == 0:
        img.setPixel(horizon, vertical, (img.pixel(horizon, vertical) & ~0x010000) | (val << 16))
    if px == 1:
        img.setPixel(horizon, vertical, (img.pixel(horizon, vertical) & ~0x000100) | (val << 8))
    if px == 2:
        img.setPixel(horizon, vertical, (img.pixel(horizon, vertical) & ~0x000001) | val)


def take_bit(image, index):
    pixel = index // 3
    horizon = pixel % image.width()
    vertical = pixel // image.width()
    px = index % 3
    if px == 0:
        return (image.pixel(horizon, vertical) >> 16) & 1
    if px == 1:
        return (image.pixel(horizon, vertical) >> 8) & 1
    if px == 2:
        return image.pixel(horizon, vertical) & 1


def in_bits(val):
    return val * 8


def bytes_read(image, start, length):
    array = QByteArray()
    buffer = 0
    for i in range(in_bits(start), in_bits(start + length)):
        buffer = (buffer << 1) | take_bit(image, i)
        if i % 8 == 7:
            array.push_back(bytes((buffer,)))
            buffer = 0
    return array


def bytes_write(image, array, start):
    for i in range(in_bits(start), in_bits(start + array.size())):
        set_bit(image, i, (int.from_bytes(array[i // 8], byteorder="big") >> (7 - i % 8)) & 1)


class Coder:
    def __init__(self):
        self.curr_power = 0
        self.max_power = 0

    def less(self):
        return self.curr_power < self.max_power

    def max_(self):
        return self.curr_power == self.max_power

    def overflow(self):
        return self.curr_power > self.max_power

    def diff(self):
        return self.max_power - self.curr_power

    def rdiff(self):
        return self.curr_power - self.max_power


class MainWindow(QMainWindow):
    bytes_key = bytes((0b11100010, 0b10011101, 0b10100100))

    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = UiMainWindow()
        self.data = Coder()
        self.ui.setup_ui(self)

        self.ui.text_edit.textChanged.connect(self.message_changed)
        self.ui.push_button.clicked.connect(self.read_image)
        self.ui.push_button_2.clicked.connect(self.write_image)
        self.ui.push_button_4.clicked.connect(self.encode_text)
        self.ui.push_button_3.clicked.connect(self.decode_text)
        self.image = None
        self.ui.label.setWordWrap(True)
        self.reset_state()

    def clear_image(self):
        if not self.image:
            return

        del self.image
        self.image = None

    def reset_state(self):
        self.clear_image()
        self.update_activity_state()

    def update_activity_state(self):
        self.ui.text_edit.setEnabled(self.image is not None)
        self.ui.push_button_2.setEnabled(self.image is not None)
        self.ui.push_button_3.setEnabled(self.image is not None)
        self.ui.push_button_4.setEnabled(self.image is not None)

    def get_input(self):
        return self.ui.text_edit.toPlainText()

    @Slot()
    def read_image(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Открыть картинку", "", "Допустимые форматы (*.png)")

        if not filepath:
            return

        self.reset_state()

        if not QFile.exists(filepath):
            self.set_output_message("Изображение {} не найдено.".format(
                filepath
            ))
            return

        self.image = QImage()
        if not self.image.load(filepath):
            self.set_output_message("Изображение {} не загружено.".format(
                filepath
            ))
            self.clear_image()
            return

        self.image.convertTo(QImage.Format_ARGB32)

        self.data.max_power = (self.image.width() * self.image.height() * 3) // 8 - len(
            MainWindow.bytes_key) - 4

        self.set_output_message("Изображение успешно загружено")
        self.update_activity_state()

    @Slot()
    def write_image(self):
        if self.image is None:
            self.set_output_message("Ошибка загрузки")
            return

        filepath, _ = QFileDialog.getSaveFileName(self, "Сохранить картинку", "", "Допустимые форматы (*.png)")

        if self.image.save(filepath, "PNG"):
            self.set_output_message("Изображение сохранено в {}".format(
                filepath
            ))
            return

        self.set_output_message("Ошибка сохранения")

    @Slot()
    def encode_text(self):
        if self.image is None:
            self.set_output_message("Ошибка загрузки.")
            return

        array = QByteArray()
        array.push_back(self.get_input().encode())

        self.data.curr_power = len(array)

        if self.data.overflow():
            self.set_output_message("Сильно большой текст для кодирования в эту картинку.")
            return

        for i in range(4):
            array.push_front(bytes(((self.data.curr_power >> in_bits(i)) & 0xff,)))

        for i in range(len(MainWindow.bytes_key) - 1, -1, -1):
            array.push_front(bytes((MainWindow.bytes_key[i],)))

        bytes_write(self.image, array, 0)

        self.set_output_message("Сообщение закодировано!")

    @Slot()
    def decode_text(self):
        if self.image is None:
            self.set_output_message("Ошибка загрузки!")
            return

        header = len(MainWindow.bytes_key) + 4

        array = bytes_read(self.image, 0, header)

        for i in range(0, len(MainWindow.bytes_key)):
            if bytes((MainWindow.bytes_key[i],)) != array[i]:
                self.set_output_message("Сообщение отсутствует!")
                return

        size = 0

        for i in range(len(MainWindow.bytes_key), len(MainWindow.bytes_key) + 4):
            size = (size << 8) + int.from_bytes(array[i], byteorder="big")

        if size > self.data.max_power:
            self.set_output_message("Ошибка декодирования! Размер заголовка превышает размер сообщения.")
            return

        array.clear()
        array = bytes_read(self.image, header, size)

        text = bytes(array).decode("utf-8")

        self.ui.text_edit.setPlainText(text)
        self.set_output_message("Присутствует сообщение длиной {} байт.".format(
            size
        ))

    @Slot()
    def message_changed(self):
        array = QByteArray()
        array.push_back(self.get_input().encode())
        self.data.curr_power = len(array)

        if self.data.less():
            argument = self.data.diff()
            self.set_output_message("Ещё можно ввести: {} байт.".format(
                argument
            ))
            return

        if self.data.max_():
            self.set_output_message("Размер сообщения достиг максимума.")
            return

        argument = self.data.rdiff()
        self.set_output_message("Размер сообщения превышен на: {} байт.".format(
            argument
        ))

    def set_output_message(self, text):
        self.ui.label.setText(text)


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())
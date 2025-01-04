import io
import sys
import csv
import random

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QColor
names = ["Молоко", "Хлеб", "Яблоко", "Банан", "Яйцо", "Булка", "Мак"]
prices = [20, 35, 15, 15, 1, 151, 134]
form_string = '\n'.join(f'"{name}";{price};' for name, price in zip(names, prices))

with open("price.csv", "w", encoding='UTF-8') as price:
    price.write("Название;Цена\n" + form_string)

design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>801</width>
      <height>541</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>560</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Итого:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="total">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>550</y>
      <width>113</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QPushButton" name="updateButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>550</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Обновить</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Expensive(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design)
        uic.loadUi(f, self)  # Загружаем дизайн

        f = open('price.csv', mode='r', encoding='utf8')
        data = sorted([[list(i.values())[0], list(i.values())[1]] for i in
                       csv.DictReader(f, delimiter=';', quotechar='"')], key=lambda x: (int(x[1]), x[0]))[::-1]

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(3)

        # Устанавливаем заголовки столбцов
        header_labels = ['Название', 'Цена', 'Количество']
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for i in range(len(data)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i][0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i][1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(0)))

        for j in range(5):
            background = QColor(random.randrange(256), random.randrange(256), random.randrange(256))
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.item(j, i).setBackground(background)

        self.tableWidget.itemChanged.connect(self.act)
        self.updateButton.clicked.connect(self.act1)

    def act(self):
        n = 0
        for i in range(self.tableWidget.rowCount()):
            n += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.total.setText(str(n))

    def act1(self):
        n = 0
        for i in range(self.tableWidget.rowCount()):
            n += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.total.setText(str(n))

        for j in range(5):
            background = QColor(random.randrange(256), random.randrange(256), random.randrange(256))
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.item(j, i).setBackground(background)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Expensive()
    program.show()
    sys.exit(app.exec())

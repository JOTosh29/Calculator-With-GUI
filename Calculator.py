import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('CalculatorWidgetDesign.ui', self)  # Assuming the UI file is named CalculatorWidgetDesign.ui

        # Connect signals and slots
        self.pushButton_11.clicked.connect(self.number_clicked)
        self.pushButton_21.clicked.connect(self.number_clicked)
        self.pushButton_2.clicked.connect(self.number_clicked)
        self.pushButton_13.clicked.connect(self.number_clicked)
        self.pushButton_5.clicked.connect(self.squared_clicked)  # Connect squared button only
        self.pushButton_12.clicked.connect(self.number_clicked)
        self.pushButton_22.clicked.connect(self.operation_clicked)
        self.pushButton_17.clicked.connect(self.number_clicked)
        self.pushButton_4.clicked.connect(self.operation_clicked)
        self.pushButton_9.clicked.connect(self.operation_clicked)
        self.pushButton.clicked.connect(self.clear_display)
        self.pushButton_7.clicked.connect(self.number_clicked)
        self.pushButton_20.clicked.connect(self.compute_result)
        self.pushButton_14.clicked.connect(self.operation_clicked)
        self.pushButton_19.clicked.connect(self.number_clicked)
        self.pushButton_16.clicked.connect(self.number_clicked)
        self.pushButton_18.clicked.connect(self.decimal_clicked)
        self.pushButton_8.clicked.connect(self.number_clicked)
        self.pushButton_6.clicked.connect(self.toggle_sign)
        self.pushButton_3.clicked.connect(self.backspace_clicked)  # Connect backspace button
        self.pushButton_10.clicked.connect(self.sqrt_clicked)  # Connect square root button

        self.current_number = ''
        self.pending_operation = None
        self.result = None

    def number_clicked(self):
        sender = self.sender()
        digit = sender.text()
        self.current_number += digit
        self.update_display()

    def operation_clicked(self):
        sender = self.sender()
        operation = sender.text()
        if self.pending_operation is None:
            self.pending_operation = operation
            self.result = float(self.current_number)
            self.current_number = ''
        else:
            self.compute_result()
            self.pending_operation = operation

    def clear_display(self):
        self.current_number = ''
        self.pending_operation = None
        self.result = None
        self.update_display()

    def compute_result(self):
        if self.pending_operation and self.current_number:
            num = float(self.current_number)
            if self.pending_operation == '+':
                self.result += num
            elif self.pending_operation == '-':
                self.result -= num
            elif self.pending_operation == 'X':
                self.result *= num
            elif self.pending_operation == '/':
                if num == 0:
                    self.label.setText("Error: Division by zero")
                    return
                self.result /= num
            self.current_number = ''
            self.pending_operation = None
            self.update_display()

    def decimal_clicked(self):
        if '.' not in self.current_number:
            self.current_number += '.'
            self.update_display()

    def toggle_sign(self):
        if self.current_number:
            if self.current_number[0] == '-':
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
            self.update_display()

    def backspace_clicked(self):
        if self.current_number:
            self.current_number = self.current_number[:-1]
            self.update_display()

    def sqrt_clicked(self):
        if self.current_number:
            num = float(self.current_number)
            if num >= 0:
                self.current_number = str(math.sqrt(num))
                self.update_display()

    def squared_clicked(self):
        if self.current_number:
            num = float(self.current_number)
            squared_num = num ** 2  # Use exponentiation operator for squaring
            self.current_number = str(squared_num)
            self.update_display()

    def update_display(self):
        if self.current_number:
            self.label.setText(self.current_number)
        elif self.result is not None:
            self.label.setText(str(self.result))
        else:
            self.label.setText("0")

def main():
    app = QApplication(sys.argv)
    widget = Calculator()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

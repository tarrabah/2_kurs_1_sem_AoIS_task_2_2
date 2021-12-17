import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import time

import math


def sind(x):
    return math.sin(x * math.pi / 180)


def cosd(x):
    return math.cos(x * math.pi / 180)


def EqvualsZero(date):
    for i in range(0, len(date)):
        if not (date[i] <= 0.000001):
            return False
    return True


def addTointerp(x1, x2, y1, y2, my_x):
    k = (y1 - y2) / (x1 - x2)
    b = (x1 * y2 - y1 * x2) / (x1 - x2)
    return k * my_x + b


def interp1(X, Y, my_x):
    num = len(X)
    if num != len(Y):
        return 0.0

    r = -1

    for i in range(0, num + 1):
        if my_x > X[i]:
            r = i
        else:
            break

    if r < 0:
        return X[0]
    if r >= num - 1:
        return X[num - 1]
    return addTointerp(X[r], X[r + 1], Y[r], Y[r + 1], my_x)


def interp2(X, Y, Z, my_x, my_y):
    rows = len(X)
    columns = len(X[0])
    rowsY = len(Y)
    columnsY = len(Y[0])
    rowsZ = len(Z)
    columnsZ = len(Z[0])

    if not (rows == rowsY and rows == rowsZ and columns == columnsY and columns == columnsZ):
        return 0.0

    rx = -1
    ry = -1
    for x in range(0, columns):
        if (my_x > X[0][x]):
            rx = x
        else:
            break

    for y in range(0, rows):
        if (my_y > Y[y][0]):
            ry = y
        else:
            break

    if rx < 0 and ry < 0:
        return Z[0][0]
    if rx < 0 and ry >= rows - 1:
        return Z[rows - 1][0]
    if rx >= columns - 1 and ry < 0:
        return Z[0][columns - 1]
    if rx >= columns - 1 and ry >= rows - 1:
        return Z[rows - 1][columns - 1]

    if rx < 0 or rx >= columns - 1:
        xx = 0 if (rx < 0) else columns - 1
        Y1ud = Y[ry][0]
        Y2ud = Y[ry + 1][0]
        return addTointerp(Y1ud, Y2ud, Z[ry][xx], Z[ry + 1][xx], my_y)

    if (ry < 0 or ry >= rows - 1):
        yy = 0 if (ry < 0) else rows - 1
        X1rl = X[0][rx]
        X2rl = X[0][rx + 1]
        return addTointerp(X1rl, X2rl, Z[yy][rx], Z[yy][rx + 1], my_x)

    #  (X,Y)
    #  (ry, rx ) --- (ry+, rx )
    #     |             |
    #     |             |
    #     |             |
    #  (ry, rx+) --- (ry+, rx+)

    X1 = X[0][rx]
    X2 = X[0][rx + 1]
    Y1 = Y[ry][0]
    Y2 = Y[ry + 1][0]

    tempZ1 = addTointerp(X1, X2, Z[ry][rx], Z[ry][rx + 1], my_x)
    tempZ2 = addTointerp(X1, X2, Z[ry + 1][rx], Z[ry + 1][rx + 1], my_x)

    return addTointerp(Y1, Y2, tempZ1, tempZ2, my_y)


class application:


    def __init__(self):
        # Визуальные компоненты
        self.main = tk.Tk()
        self.main.title("Расчёт параметров электромобиля")
        self.main.geometry("800x400")

        self.label_login_text = tk.Label(master=self.main, text='Login')
        self.label_login_text.grid(row=1, column=1, sticky=tk.W, padx=2, pady=2)

        self.entry_login = tk.Entry(master=self.main, bg = "white", width = 30)
        self.entry_login.grid(row=2, column=1, padx=2, pady=2)

        self.label_password_text = tk.Label(master=self.main, text='Password')
        self.label_password_text.grid(row=3, column=1, sticky=tk.W, padx=2, pady=2)

        self.entry_password = tk.Entry(master=self.main, bg = "white", width = 30, show="*")
        self.entry_password.grid(row=4, column=1, padx=2, pady=2)

        self.button_confirm_login_pasword = tk.Button(master = self.main, text = "Confirm", command=self.button_cofirm_handler)
        self.button_confirm_login_pasword.grid(row=5, column=1, sticky=tk.E, padx=2, pady=2)

        self.label_login_error = tk.Label(master=self.main, text='')
        self.label_login_error.grid(row=2, column=2, sticky=tk.W, padx=2, pady=2)

        self.label_password_error = tk.Label(master=self.main, text='')
        self.label_password_error.grid(row=4, column=2, sticky=tk.W, padx=2, pady=2)


    def swith_to_calulations(self):#переход от режима ввода пароля к вычислению и показу графиков
        pass


    def login_get(self):
        login = self.entry_login.get()

        if login == "":
            self.label_login_error.configure(text = "login is not entered")
            return 1
        else:
            return login


    def password_get(self):
        password = self.entry_password.get()

        if password == "":
            self.label_password_error.configure(text = "password is not entered")
            return 1
        else:
            return password


    def button_cofirm_handler(self):
        self.label_login_error.configure(text = "")
        self.label_password_error.configure(text = "")

        if self.login_get() != 1:
            print(self.login_get())

        if self.password_get() != 1:
            print(self.password_get())


    def start_app(self):
        self.main.mainloop()


    def close_app(self):
        exit()


exemplar = application()
exemplar.start_app()

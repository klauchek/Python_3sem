from tkinter import *
import matplotlib.pyplot as plt
import sympy as sp
import numexpr as ne
import numpy as np
import common as cm


class my_calc():
    def __init__(self):

        self.root = Tk()

        self.root["bg"] = "#000"
        self.root.geometry(cm.calc_size)
        self.root.title("Калькулятор")
        self.root.resizable(False, False)

        self.btns = list()

        self.btns_init(self.btns)

        self.build()


    def calc(self):
        self.root.mainloop()

    
    def btns_init(self, btns_list):

        config_file = open("gui.config", 'r')

        rows = config_file.readlines()

        for row in rows:
            cur_btns = row.split(", ")

            for btn_it in cur_btns:
                btns_list.append(btn_it)

        config_file.close()

    def build(self):

        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), \
                                              bg="#000", foreground="#FFF")

        self.lbl.place(x=11, y=50)

        x = cm.BEG_X
        y = cm.BEG_Y

        for bt in self.btns:

            cur_com = lambda x = bt: self.logicalc(x)

            if bt != cm.empty:
                Button(text=bt, bg="#FFF", font=("Times New Roman", 15), \
                    command=cur_com).place(x=x, y=y, width=cm.BUT_WDTH, height=cm.BUT_HGHT)

            x += cm.X_OFFSET

            if x > cm.X_CAP:
                x = cm.BEG_X
                y += cm.Y_OFFSET


    def logicalc(self, op):

        alg_funcs = ["sin", "cos", "exp"]

        if op == "C":
            self.formula = cm.empty

        elif op == "DEL":
            self.formula = self.formula[0:-1]

        elif op == "sqr":
            self.formula = str((eval(self.formula))**2)

        elif op == "=":
            self.formula = str(ne.evaluate(self.formula))

        elif op == "PROG":
            self.formula = hex(eval(self.formula))

        elif op == "GRAPH":
            graph_builder(self.formula)

        elif op == "DERIV":
            self.formula = self.get_deriv(self.formula)

        elif op in alg_funcs:
            self.formula = str(op + "(")

        elif op == "x":
            if self.formula == '0':
                self.formula = "x"
            else:
                self.formula += "x"
        else:
            if self.formula == "0":
                self.formula = ""

            self.formula += op
            
        self.update()


    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


    def get_deriv(self, expr):
        x = sp.Symbol('x')
        return str(sp.diff(expr, x, 1))


def graph_builder(func):

    x = np.linspace(-5,5,100)
    y = ne.evaluate(func)
    
    fig = plt.figure()
    plt.plot(x,y, 'r')
    plt.xlim((-10,10))
    plt.grid()
    plt.show()





from tkinter import *


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


#calc window
class StandardCalculator:
    def press(self, num):
        self.input_field.insert(END, num)

    def equals(self):
        text = self.input_field.get()
        self.input_field.delete(0, END)
        self.input_field.insert(0, eval(text))

    def clear(self):
        self.input_field.delete(0, END)

    def delete(self):
        self.input_field.delete(len(self.input_field.get())-1)

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.iconbitmap('csuf-seal.ico')
        # Row 1
        self.input_field = Entry(master, justify=RIGHT, font = "Calibri 8 bold")
        self.input_field.grid(row=0, column=1, columnspan=4, ipady=10, ipadx=70)

        btn_mod = HoverButton(master, text="%", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                              command=lambda: self.press('%'))
        btn_mod.grid(column=1, row=1)

        btn_ce = HoverButton(master, text="CE", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                             command=lambda: self.clear())
        btn_ce.grid(column=2, row=1)

        btn_c = HoverButton(master, text="C", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.clear())
        btn_c.grid(column=3, row=1)

        btn_X = HoverButton(master, text="X", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.delete())
        btn_X.grid(column=4, row=1)

        # Row 2
        btn_fraction = HoverButton(master, text="1/x", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold")
        btn_fraction.grid(column=1, row=2)

        btn_exponent = HoverButton(master, text="x^2", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold")
        btn_exponent.grid(column=2, row=2)

        btn_root = HoverButton(master, text="x^1/2", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold")
        btn_root.grid(column=3, row=2)

        btn_div = HoverButton(master, text="/", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold")
        btn_div.grid(column=4, row=2)

        # Row 3
        btn_7 = HoverButton(master, text="7", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('7'))
        btn_7.grid(column=1, row=3)

        btn_8 = HoverButton(master, text="8", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('8'))
        btn_8.grid(column=2, row=3)

        btn_9 = HoverButton(master, text="9", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('9'))
        btn_9.grid(column=3, row=3)

        btn_multiply = HoverButton(master, text="X", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                                   command=lambda: self.press('*'))
        btn_multiply.grid(column=4, row=3)

        # Row 4
        btn_4 = HoverButton(master, text="4", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('4'))
        btn_4.grid(column=1, row=4)

        btn_5 = HoverButton(master, text="5", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('5'))
        btn_5.grid(column=2, row=4)

        btn_6 = HoverButton(master, text="6", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('6'))
        btn_6.grid(column=3, row=4)

        btn_subtract = HoverButton(master, text="-", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                                   command=lambda: self.press('-'))
        btn_subtract.grid(column=4, row=4)

        # Row 5
        btn_1 = HoverButton(master, text="1", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('1'))
        btn_1.grid(column=1, row=5)

        btn_2 = HoverButton(master, text="2", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('2'))
        btn_2.grid(column=2, row=5)

        btn_3 = HoverButton(master, text="3", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('3'))
        btn_3.grid(column=3, row=5)

        btn_addition = HoverButton(master, text="+", height=3, width=7, bg="gray80", activebackground='gray73', font = "Calibri 11 bold",
                                   command=lambda: self.press('+'))
        btn_addition.grid(column=4, row=5)

        # Row 6
        btn_sign = HoverButton(master, text="+/-", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold")
        btn_sign.grid(column=1, row=6)

        btn_0 = HoverButton(master, text="0", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                            command=lambda: self.press('0'))
        btn_0.grid(column=2, row=6)

        btn_decimal = HoverButton(master, text=".", height=3, width=7, activebackground='gray73', font = "Calibri 11 bold",
                                  command=lambda: self.press('.'))
        btn_decimal.grid(column=3, row=6)

        btn_equals = HoverButton(master, text="=", height=3, width=7, bg="azure3", activebackground='azure4', font = "Calibri 11 bold",
                                 command=lambda: self.equals())
        btn_equals.grid(column=4, row=6)


root = Tk()
calculator = StandardCalculator(root)
root.mainloop()

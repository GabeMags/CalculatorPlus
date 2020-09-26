from tkinter import *
import math


# Button wrapper class - tk buttons will change colors when hovered over.
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


# Main standard calculator window
class StandardCalculator:

    def press(self, num):
        if self.input_field.get() == "ERROR":
            self.input_field.delete(ANCHOR, END)
        elif self.AnswerMode == TRUE:
            self.AnswerMode = FALSE
            self.input_field.delete(ANCHOR, END)
        self.input_field.insert(END, num)

    def press_operator(self, operator):
        if self.input_field.get() == "ERROR":
            self.input_field.delete(ANCHOR, END)
        self.AnswerMode = FALSE
        self.input_field.insert(END, operator)

    def equals(self):
        try:
            answer = eval(self.input_field.get())
            if float(answer).is_integer():
                answer = int(answer)
        except:
            answer = "ERROR"
        self.input_field.delete(ANCHOR, END)
        self.input_field.insert(ANCHOR, answer)
        self.AnswerMode = TRUE

    def clear(self):
        self.input_field.delete(ANCHOR, END)

    def delete(self):
        self.input_field.delete(len(self.input_field.get()) - 1)

    def squared(self):
        answer = eval(self.input_field.get() + "**2")
        if float(answer).is_integer():
            answer = int(answer)
        self.input_field.delete(ANCHOR, END)
        self.input_field.insert(ANCHOR, answer)
        self.AnswerMode = TRUE

    def fraction(self):
        try:
            answer = eval("1/" + self.input_field.get())
            if float(answer).is_integer():
                answer = int(answer)
        except:
            answer = "ERROR"
        self.input_field.delete(ANCHOR, END)
        self.input_field.insert(ANCHOR, answer)
        self.AnswerMode = TRUE

    def sqrt(self):
        try:
            answer = math.sqrt(int(self.input_field.get()))
            if float(answer).is_integer():
                answer = int(answer)
        except:
            answer = "ERROR"
        self.input_field.delete(ANCHOR, END)
        self.input_field.insert(ANCHOR, answer)
        self.AnswerMode = TRUE

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.iconbitmap('csuf-seal.ico')
        frame = Frame(master)
        frame.grid(row=0, column=0, sticky="nsew")
        self.AnswerMode = TRUE

        # Row 1
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(4, weight=1)
        self.input_field = Entry(frame, justify=RIGHT, font="Calibri 40", width=6, borderwidth=7)
        self.input_field.grid(row=0, column=0, columnspan=30, ipady=5, ipadx=70)
        self.input_field.insert(ANCHOR, "0")

        btn_mod = HoverButton(frame, text="%", height=2, width=9, bg="gray80", activebackground='gray73',
                              font="Calibri 11 bold",
                              command=lambda: self.press('%'))
        btn_mod.grid(column=1, row=1)

        btn_ce = HoverButton(frame, text="CE", height=2, width=9, bg="gray80", activebackground='gray73',
                             font="Calibri 11 bold",
                             command=lambda: self.clear())
        btn_ce.grid(column=2, row=1)

        btn_c = HoverButton(frame, text="C", height=2, width=9, bg="gray80", activebackground='gray73',
                            font="Calibri 11 bold",
                            command=lambda: self.clear())
        btn_c.grid(column=3, row=1)

        btn_X = HoverButton(frame, text="X", height=2, width=9, bg="gray80", activebackground='gray73',
                            font="Calibri 11 bold",
                            command=lambda: self.delete())
        btn_X.grid(column=4, row=1)

        # Row 2
        btn_fraction = HoverButton(frame, text="1/x", height=2, width=9, bg="gray80", activebackground='gray73',
                                   font="Calibri 11 bold",
                                   command=lambda: self.fraction())
        btn_fraction.grid(column=1, row=2)

        btn_exponent = HoverButton(frame, text="x^2", height=2, width=9, bg="gray80", activebackground='gray73',
                                   font="Calibri 11 bold",
                                   command=lambda: self.squared())
        btn_exponent.grid(column=2, row=2)

        btn_root = HoverButton(frame, text="x^1/2", height=2, width=9, bg="gray80", activebackground='gray73',
                               font="Calibri 11 bold",
                               command=lambda: self.sqrt())
        btn_root.grid(column=3, row=2)

        btn_div = HoverButton(frame, text="/", height=2, width=9, bg="gray80", activebackground='gray73',
                              font="Calibri 11 bold",
                              command=lambda: self.press_operator('/'))
        btn_div.grid(column=4, row=2)

        # Row 3
        btn_7 = HoverButton(frame, text="7", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('7'))
        btn_7.grid(column=1, row=3)

        btn_8 = HoverButton(frame, text="8", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('8'))
        btn_8.grid(column=2, row=3)

        btn_9 = HoverButton(frame, text="9", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('9'))
        btn_9.grid(column=3, row=3)

        btn_multiply = HoverButton(frame, text="X", height=2, width=9, bg="gray80", activebackground='gray73',
                                   font="Calibri 11 bold",
                                   command=lambda: self.press_operator('*'))
        btn_multiply.grid(column=4, row=3)

        # Row 4
        btn_4 = HoverButton(frame, text="4", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('4'))
        btn_4.grid(column=1, row=4)

        btn_5 = HoverButton(frame, text="5", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('5'))
        btn_5.grid(column=2, row=4)

        btn_6 = HoverButton(frame, text="6", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('6'))
        btn_6.grid(column=3, row=4)

        btn_subtract = HoverButton(frame, text="-", height=2, width=9, bg="gray80", activebackground='gray73',
                                   font="Calibri 11 bold",
                                   command=lambda: self.press_operator('-'))
        btn_subtract.grid(column=4, row=4)

        # Row 5
        btn_1 = HoverButton(frame, text="1", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('1'))
        btn_1.grid(column=1, row=5)

        btn_2 = HoverButton(frame, text="2", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('2'))
        btn_2.grid(column=2, row=5)

        btn_3 = HoverButton(frame, text="3", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('3'))
        btn_3.grid(column=3, row=5)

        btn_addition = HoverButton(frame, text="+", height=2, width=9, bg="gray80", activebackground='gray73',
                                   font="Calibri 11 bold",
                                   command=lambda: self.press_operator('+'))
        btn_addition.grid(column=4, row=5)

        # Row 6
        btn_sign = HoverButton(frame, text="+/-", height=2, width=9, activebackground='gray73', font="Calibri 11 bold")
        btn_sign.grid(column=1, row=6)

        btn_0 = HoverButton(frame, text="0", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                            command=lambda: self.press('0'))
        btn_0.grid(column=2, row=6)

        btn_decimal = HoverButton(frame, text=".", height=2, width=9, activebackground='gray73', font="Calibri 11 bold",
                                  command=lambda: self.press('.'))
        btn_decimal.grid(column=3, row=6)

        btn_equals = HoverButton(frame, text="=", height=2, width=9, bg="azure3", activebackground='azure4',
                                 font="Calibri 11 bold",
                                 command=lambda: self.equals())
        btn_equals.grid(column=4, row=6)


root = Tk()
calculator = StandardCalculator(root)
root.mainloop()

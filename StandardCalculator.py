from tkinter import *

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

root = Tk()
root.title("CSUF Calculator")
root.configure(background = "black")
root.iconbitmap('C:/Users\Sean/PycharmProjects/Hello World/csuf-seal.ico')

#Row 1

btn_mod = HoverButton(root, text="%", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_mod.grid(column=1, row =1)

btn_CE = HoverButton(root, text="CE", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_CE.grid(column=2, row=1)

btn_C = HoverButton(root, text="C", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_C.grid(column=3, row=1)

btn_X = HoverButton(root, text="X", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_X.grid(column=4, row=1)

#Row 2
btn_fraction = HoverButton(root, text="1/x", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_fraction.grid(column=1, row=2)

btn_exponent = HoverButton(root, text="x^2", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_exponent.grid(column=2, row=2)

btn_root = HoverButton(root, text="x^1/2", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_root.grid(column=3, row=2)

btn_div = HoverButton(root, text="/", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_div.grid(column=4, row=2)

#Row 3
btn_7 = HoverButton(root, text="7", height=3, width=7, activebackground = 'gray73')
btn_7.grid(column=1, row=3)

btn_8 = HoverButton(root, text="8", height=3, width=7, activebackground = 'gray73')
btn_8.grid(column=2, row=3)

btn_9 = HoverButton(root, text="9", height=3, width=7, activebackground = 'gray73')
btn_9.grid(column=3, row=3)

btn_multiply = HoverButton(root, text="X", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_multiply.grid(column=4, row=3)

#Row 4
btn_4 = HoverButton(root, text="4", height=3, width=7, activebackground = 'gray73')
btn_4.grid(column=1, row=4)

btn_5 = HoverButton(root, text="5", height=3, width=7, activebackground = 'gray73')
btn_5.grid(column=2, row=4)

btn_6 = HoverButton(root, text="6", height=3, width=7, activebackground = 'gray73')
btn_6.grid(column=3, row=4)

btn_subtract = HoverButton(root, text="-", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_subtract.grid(column=4, row=4)

#Row 5
btn_1 = HoverButton(root, text="1", height=3, width=7, activebackground = 'gray73')
btn_1.grid(column=1, row=5)

btn_2 = HoverButton(root, text="2", height=3, width=7, activebackground = 'gray73')
btn_2.grid(column=2, row=5)

btn_3 = HoverButton(root, text="3", height=3, width=7, activebackground = 'gray73')
btn_3.grid(column=3, row=5)

btn_addition = HoverButton(root, text="+", height=3, width=7, bg = "gray80", activebackground = 'gray73')
btn_addition.grid(column=4, row=5)

#Row 6
btn_sign = HoverButton(root, text="+/-", height=3, width=7, activebackground = 'gray73')
btn_sign.grid(column=1, row=6)

btn_0 = HoverButton(root, text="0", height=3, width=7, activebackground = 'gray73')
btn_0.grid(column=2, row=6)

btn_decimal = HoverButton(root, text=".", height=3, width=7, activebackground = 'gray73')
btn_decimal.grid(column=3, row=6)

btn_equals = HoverButton(root, text="=", height=3, width=7, bg = "azure3", activebackground = 'azure4')
btn_equals.grid(column=4, row=6)


root.mainloop()
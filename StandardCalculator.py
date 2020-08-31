from tkinter import *
root = Tk()
root.title("CSUF Calculator")
root.configure(background = "black")
root.iconbitmap('C:/Users\Sean/PycharmProjects/Hello World/csuf-seal.ico')

#Row 1
btn_mod = Button(root, text="%", height=3, width=7, bg = "gray80")
btn_mod.grid(column=1, row =1)

btn_CE = Button(root, text="CE", height=3, width=7, bg = "gray80")
btn_CE.grid(column=2, row=1)

btn_C = Button(root, text="C", height=3, width=7, bg = "gray80")
btn_C.grid(column=3, row=1)

btn_X = Button(root, text="X", height=3, width=7, bg = "gray80")
btn_X.grid(column=4, row=1)

#Row 2
btn_fraction = Button(root, text="1/x", height=3, width=7, bg = "gray80")
btn_fraction.grid(column=1, row=2)

btn_exponent = Button(root, text="x^2", height=3, width=7, bg = "gray80")
btn_exponent.grid(column=2, row=2)

btn_root = Button(root, text="x^1/2", height=3, width=7, bg = "gray80")
btn_root.grid(column=3, row=2)

btn_div = Button(root, text="/", height=3, width=7, bg = "gray80")
btn_div.grid(column=4, row=2)

#Row 3
btn_7 = Button(root, text="7", height=3, width=7)
btn_7.grid(column=1, row=3)

btn_8 = Button(root, text="8", height=3, width=7)
btn_8.grid(column=2, row=3)

btn_9 = Button(root, text="9", height=3, width=7)
btn_9.grid(column=3, row=3)

btn_multiply = Button(root, text="X", height=3, width=7, bg = "gray80")
btn_multiply.grid(column=4, row=3)

#Row 4
btn_4 = Button(root, text="4", height=3, width=7)
btn_4.grid(column=1, row=4)

btn_5 = Button(root, text="5", height=3, width=7)
btn_5.grid(column=2, row=4)

btn_6 = Button(root, text="6", height=3, width=7)
btn_6.grid(column=3, row=4)

btn_subtract = Button(root, text="-", height=3, width=7, bg = "gray80")
btn_subtract.grid(column=4, row=4)

#Row 5
btn_1 = Button(root, text="1", height=3, width=7)
btn_1.grid(column=1, row=5)

btn_2 = Button(root, text="2", height=3, width=7)
btn_2.grid(column=2, row=5)

btn_3 = Button(root, text="3", height=3, width=7)
btn_3.grid(column=3, row=5)

btn_addition = Button(root, text="+", height=3, width=7, bg = "gray80")
btn_addition.grid(column=4, row=5)

#Row 6
btn_sign = Button(root, text="+/-", height=3, width=7)
btn_sign.grid(column=1, row=6)

btn_0 = Button(root, text="0", height=3, width=7)
btn_0.grid(column=2, row=6)

btn_decimal = Button(root, text=".", height=3, width=7)
btn_decimal.grid(column=3, row=6)

btn_equals = Button(root, text="=", height=3, width=7, bg = "azure3")
btn_equals.grid(column=4, row=6)

root.mainloop()
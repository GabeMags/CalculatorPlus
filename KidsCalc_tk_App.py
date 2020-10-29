import os
import random
import time
from tkinter import *
from PIL import ImageTk, Image

# FUNCTION

class Application(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.bttn_clicks = 0
        self.root = self
        image = Image.open("ball.gif")
        image2 = Image.open("ball.png")
        bgimg = Image.open("kids.png")
        width, height = image.size
        self.img = ImageTk.PhotoImage(image.convert("RGB").resize((round(20 / height * width), round(24))))
        self.img2 = ImageTk.PhotoImage(image2.convert("RGB").resize((round(20 / height * width), round(24))))
        self.background_image = ImageTk.PhotoImage(bgimg.convert("RGB").resize((round(2000 / height * width), round(300))))
        self.thisEntry = Entry(self.root, highlightbackground='#3E4149')
        # imgpanel = Label(self.root, image = img)

        # Initial GUI buttons
        self.maxlabel = Label(self.root,
                              text="\nMax number of tries reached. \nDo you want to try another question or quit?",
                              bg="white")
        self.nextButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366",
                                 fg="white", width=20, command=self.addFunc)
        self.nextMulButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366",
                                    fg="white", width=20, command=self.mulFunc)
        self.nextSubButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366",
                                    fg="white", width=20, command=self.subFunc)
        self.exitButton = Button(self.root, text=" Exit ", highlightbackground='#3E4149', bg="#003366", fg="white",
                                 width=20, command=self.exitFunc)

        # image array counters
        self.pa = 0
        self.pb = 0
        self.pl = []

        # User feedback
        self.addlabelx = Label(self.root, text="\nPerfect, the answer is correct... \n", bg="white", fg="blue")
        self.addlabely = Label(self.root, text="\nSorry, the answer is wrong... Please try again !\n", bg="white",
                               fg="red")

    def calc_For_Kids(self):
        # create the tk
        self.root.title("Kitty Calculator")
        self.root.geometry('540x720')
        self.root.config(bg="white")
        Label(self.root, image=self.background_image).place(x=0, y=0, anchor="nw")

        # menu
        message = f'\n\nIf you want to solve another question then press option button again.\n if not then press any other option \n\n\nPlease click on the options below : '

        label1 = Button(self.root, text="1. Add", bg="white", fg="blue", highlightbackground='#3E4149', width=20,
                        command=self.addFunc)
        label2 = Button(self.root, text="2. Subtract", bg="#003366", fg="white", width=20,
                        highlightbackground='#3E4149', command=self.subFunc)
        label3 = Button(self.root, text="3. Multiply", bg="#003366", fg="white", width=20,
                        highlightbackground='#3E4149', command=self.mulFunc)
        label4 = Button(self.root, text="0. Exit", bg="#003366", fg="white", width=20, highlightbackground='#3E4149',
                        command=self.exitFunc)
        label6 = Label(self.root, bg="white", highlightbackground='#3E4149')
        addlabel3 = Label(self.root, text=message, bg='grey', pady=5, padx=20, fg="#003366")

        addlabel3.grid(row=0, column=0, padx=20, columnspan=10)

        label1.grid(row=1, column=0, pady=(5, 5), padx=150, columnspan=10)
        label2.grid(row=2, column=0, pady=5, padx=20, columnspan=10)
        label3.grid(row=3, column=0, pady=5, padx=20, columnspan=10)
        label4.grid(row=4, column=0, pady=5, padx=20, columnspan=10)
        label6.grid(row=5, column=0, pady=5, padx=20, columnspan=10)

        self.root.mainloop()

    def checkAdd(self, a, b):
        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        print("Add:", self.thisEntry.get(), ">>>", str(a + b))

        if (self.thisEntry.get() == str(a + b)):
            self.addlabelx.grid(row=18, column=0, padx=20, columnspan=10)
            self.nextButton.grid(row=22, column=0, columnspan=10)
        else:
            self.addlabely.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            if self.bttn_clicks >= 3:
                self.addlabely.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def addFunc(self):
        self.bttn_clicks = 0
        self.maxlabel.grid_forget()
        self.nextSubButton.grid_forget()
        self.nextButton.grid_forget()
        self.nextMulButton.grid_forget()
        self.exitButton.grid_forget()

        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        photo_list = []

        addlabel1 = Label(self.root, text="what do you think the sum of these two numbers are? ", bg="white")
        num = f"{a} + {b}"

        if self.pa or self.pb:
            for i in range(0, self.pa):
                self.pl[i].grid_forget()
            for i in range(0, self.pb):
                self.pl[i + self.pa].grid_forget()

        if (a + b) > 0:
            imglabel = Label(self.root, text="This is how it looks visually", bg="white")
            imglabel.grid(row=8, column=0, pady=5, padx=20, columnspan=10)
            self.arrange_ball_images("+", a, b)

        addlabel2 = Label(self.root, text=num, bg="white", highlightbackground='#3E4149')

        addButton = Button(self.root, text=" Submit ", bg="white", highlightbackground='#3E4149',
                           command=lambda: self.checkAdd(a, b))
        addlabel1.grid(row=6, column=0, pady=5, padx=20, columnspan=10)
        addlabel2.grid(row=7, column=0, pady=5, padx=20, columnspan=10)
        self.thisEntry.grid(row=15, column=0, pady=5, padx=20, columnspan=10)
        addButton.grid(row=16, column=0, pady=5, padx=20, columnspan=10)

    def checkSub(self, a, b):
        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        print("Sub:", self.thisEntry.get(), ">>>", str(a - b))
        if (self.thisEntry.get() == str(a - b)):
            self.addlabelx.grid(row=18, column=0, padx=20, columnspan=10)
            self.nextSubButton.grid(row=22, column=0, columnspan=10)
        else:
            self.addlabely.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            if self.bttn_clicks >= 3:
                self.addlabely.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextSubButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def subFunc(self):
        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        self.bttn_clicks = 0
        self.maxlabel.grid_forget()
        self.nextSubButton.grid_forget()
        self.nextButton.grid_forget()
        self.nextMulButton.grid_forget()
        self.exitButton.grid_forget()
        photo_list = []
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        sublabel1 = Label(self.root, text="what do you think the difference of these two numbers are? ", bg="white")
        subnum = f"{a} - {b}"

        if self.pa or self.pb:
            for i in range(0, self.pa):
                self.pl[i].grid_forget()
            for i in range(0, self.pb):
                self.pl[i + self.pa].grid_forget()

        if (a + b) > 0:
            imglabel = Label(self.root, text="This is how it looks visually", bg="white")
            imglabel.grid(row=8, column=0, pady=5, padx=20, columnspan=10)
            self.arrange_ball_images("-", a, b)

        sublabel2 = Label(self.root, text=subnum, bg="white")
        subButton = Button(self.root, text=" Submit ", highlightbackground='#3E4149',
                           command=lambda: self.checkSub(a, b))
        sublabel1.grid(row=6, column=0, pady=5, padx=20, columnspan=10)
        sublabel2.grid(row=7, column=0, pady=5, padx=20, columnspan=10)
        self.thisEntry.grid(row=15, column=0, pady=5, padx=20, columnspan=10)
        subButton.grid(row=16, column=0, pady=5, padx=20, columnspan=10)

    def checkMul(self, a, b):
        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        print("Mul:", self.thisEntry.get(), ">>>", str(a * b))
        if (self.thisEntry.get() == str(a * b)):
            self.addlabelx.grid(row=18, column=0, padx=20, columnspan=10)
            self.nextMulButton.grid(row=22, column=0, columnspan=10)
        else:
            self.addlabely.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            if self.bttn_clicks >= 3:
                self.addlabely.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextMulButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def mulFunc(self):
        self.addlabelx.grid_forget()
        self.addlabely.grid_forget()
        self.bttn_clicks = 0
        self.maxlabel.grid_forget()
        self.nextSubButton.grid_forget()
        self.nextButton.grid_forget()
        self.nextMulButton.grid_forget()
        self.exitButton.grid_forget()

        a = random.randint(0, 9)
        b = random.randint(0, 9)
        mullabel1 = Label(self.root, text="what do you think the difference of these two numbers are? ", bg="white")
        mulnum = f"{a} * {b}"

        if a != 0 or b != 0:
            imglabel = Label(self.root, text="This is how it looks visually", bg="white")
            imglabel.grid(row=8, column=0, pady=5, padx=20, columnspan=10)
            self.arrange_ball_images("*", a, b)

        mullabel2 = Label(self.root, text=mulnum, bg="white")
        mulButton = Button(self.root, text=" Submit ", highlightbackground='#3E4149',
                           command=lambda: self.checkMul(a, b))

        mullabel1.grid(row=6, column=0, pady=5, padx=20, columnspan=10)
        mullabel2.grid(row=7, column=0, pady=5, padx=20, columnspan=10)
        self.thisEntry.grid(row=15, column=0, pady=5, padx=20, columnspan=10)
        mulButton.grid(row=16, column=0, pady=5, padx=20, columnspan=10)

    def exitFunc(self):
        quit()

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def arrange_ball_images(self, sign, a, b):
        if self.pa:
            for i in range(0, self.pa):
                self.pl[i].grid_forget()
        if self.pb:
            for i in range(0, self.pb):
                self.pl[i + self.pa].grid_forget()

        photo_list = []
        for i in range(0, a):
            photo_list.append(Label(self.root, image=self.img))
            photo_list[-1].grid(row=9, column=0 + i)

        labelplus = Label(self.root, text=sign, bg="white")
        labelplus.grid(row=10, column=0)

        for i in range(0, b):
            photo_list.append(Label(self.root, image=self.img2))
            photo_list[-1].grid(row=11, column=0 + i)
        self.pa = a
        self.pb = b
        self.pl = photo_list






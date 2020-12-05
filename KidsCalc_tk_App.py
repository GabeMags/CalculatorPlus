import os
import random
import time
from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import ImageLabelClass as gif_handler

class Application(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.bttn_clicks = 0
        self.root = self
        image = Image.open("question_sprite_images/ball.gif")
        image2 = Image.open("question_sprite_images/ball.png")
        #audio arrays
        self.victory_sound = ["audio/VO_Gen_Victory_01.wav", "audio/VO_Gen_Victory_02.wav", "audio/VO_Gen_Victory_03.wav",
                         "audio/VO_Gen_Victory_04.wav", "audio/VO_Gen_Victory_05.wav", "audio/VO_Gen_Victory_06.wav",
                         "audio/VO_Gen_Victory_07.wav", "audio/VO_Gen_Victory_08.wav"]
        self.elimination_sound = ["audio/VO_Gen_Elimination_01.wav", "audio/VO_Gen_Elimination_02.wav",
                             "audio/VO_Gen_Elimination_03.wav", "audio/VO_Gen_Elimination_05.wav",
                             "audio/VO_Gen_Elimination_05.wav", "audio/VO_Gen_Elimination_06.wav",
                             "audio/VO_Gen_Elimination_07.wav"]
        width, height = image.size
        self.img = ImageTk.PhotoImage(image.convert("RGB").resize((round(20 / height * width), round(24))))
        self.img2 = ImageTk.PhotoImage(image2.convert("RGB").resize((round(20 / height * width), round(24))))

        # Cool background
        self.star_gif_background = gif_handler.ImageLabel(self.root)

        # Cool fall guy
        self.fall_guy_gif = gif_handler.ImageLabel(self.root)

        # # Player hearts (num of lives)
        # self.life_heart_sprite_gif = gif_handler.ImageLabel(self.root)

        # Entry box
        self.answerEntry = Entry(self.root, highlightbackground='#3E4149')

        # Response GUI buttons
        self.maxlabel = Label(self.root, text="\nMax number of tries reached. \nDo you want to try another question or quit?", bg="black", fg="white")
        self.nextButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366", fg="white", width=20, command=self.addFunc)
        self.nextMulButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366", fg="white", width=20, command=self.mulFunc)
        self.nextSubButton = Button(self.root, text=" Next Question ", highlightbackground='#3E4149', bg="#003366", fg="white", width=20, command=self.subFunc)
        self.exitButton = Button(self.root, text=" Exit ", highlightbackground='#3E4149', bg="#003366", fg="white", width=20, command=self.exitFunc)

        # Image array counters
        self.pa = 0
        self.pb = 0
        self.pl = []

        # User feedback
        self.response_text_correct = Label(self.root, text="\nPerfect, the answer is correct... \n", bg="black", fg="blue")
        self.response_text_sorry_wrong = Label(self.root, text="\nSorry, the answer is wrong... Please try again !\n", bg="black", fg="red")

    def calc_For_Kids(self):
        # Window creation
        self.root.title("Kitty Calculator")
        self.root.geometry('1280x720')
        self.root.config(bg="white")

        # Animated background (uses a gif to fill the window)
        self.star_gif_background.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
        self.star_gif_background.load('backgrounds/beangif.gif', 1280, 720)

        # # Animated player lives
        # self.life_heart_sprite_gif.place(x=550, y=400, anchor="nw")
        # self.life_heart_sprite_gif.load('question_sprite_images/blueheart.gif', )

        # Mode select GUI buttons
        menu_title = f'\nMode Selection'
        menu_title_label = Label(self.root, text=menu_title, bg='black', fg="white")
        mode_btn_add = Button(self.root, text="Add", bg="#003366", fg="white", highlightbackground='#3E4149', width=20,
                              command=self.addFunc)
        mode_btn_subtract = Button(self.root, text="Subtract", bg="#003366", fg="white", width=20,
                                   highlightbackground='#3E4149', command=self.subFunc)
        # mode_btn_multiply = Button(self.root, text="Multiply", bg="#003366", fg="white", width=20,
        #                            highlightbackground='#3E4149', command=self.mulFunc)
        mode_btn_exit = Button(self.root, text="Exit", bg="#003366", fg="white", width=20,
                               highlightbackground='#3E4149', command=self.exitFunc)

        # Placing the buttons
        menu_title_label.grid(row=0, column=0, pady=5)
        mode_btn_add.grid(row=1, column=0, pady=5)
        mode_btn_subtract.grid(row=2, column=0, pady=5)
        # mode_btn_multiply.grid(row=3, column=0, pady=5)
        mode_btn_exit.grid(row=4, column=0, pady=5)

        self.root.mainloop()

    def checkAdd(self, a, b):
        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()
        print("Add:", self.answerEntry.get(), ">>>", str(a + b))

        if self.answerEntry.get() == str(a + b):
            self.response_text_correct.grid(row=18, column=1, padx=20, columnspan=10)
            rand_victor_sound = mixer.Sound(random.choice(self.victory_sound))
            mixer.Sound.play(rand_victor_sound)
            self.nextButton.grid(row=22, column=1, columnspan=10)
        else:
            self.response_text_sorry_wrong.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            rand_wrong_sound = mixer.Sound(random.choice(self.elimination_sound))
            mixer.Sound.play(rand_wrong_sound)
            if self.bttn_clicks >= 3:
                self.response_text_sorry_wrong.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def addFunc(self):
        self.bttn_clicks = 0

        # Hide buttons and text until we need them
        self.maxlabel.grid_forget()
        self.nextSubButton.grid_forget()
        self.nextButton.grid_forget()
        self.nextMulButton.grid_forget()
        self.exitButton.grid_forget()

        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()

        a = random.randint(0, 9)
        b = random.randint(0, 9)
        photo_list = []

        question_text = Label(self.root, font=(None, 18), text="What do you think the sum of these two numbers are? ", bg="black", fg="white", width=60)
        num = f"{a} + {b}"

        if self.pa or self.pb:
            for i in range(0, self.pa):
                self.pl[i].grid_forget()
            for i in range(0, self.pb):
                self.pl[i + self.pa].grid_forget()

        if (a + b) > 0:
            imglabel = Label(self.root, font=(None, 18), text="OR", bg="black", fg="white")
            imglabel.grid(row=2, column=2, pady=25, columnspan=10)
            self.arrange_ball_images("+", a, b)

        problem = Label(self.root, font=(None, 50), text=num, bg="black", fg="white")
        submit_button = Button(self.root, text=" Submit ", bg="white", highlightbackground='#3E4149', command=lambda: self.checkAdd(a, b))

        question_text.grid(row=0, column=2, pady=15, columnspan=10)
        problem.grid(row=1, column=2, pady=5, columnspan=10)
        self.answerEntry.grid(row=15, column=2, pady=(50, 5), columnspan=10)
        submit_button.grid(row=16, column=2, pady=5, columnspan=10)

    def checkSub(self, a, b):
        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()
        print("Sub:", self.answerEntry.get(), ">>>", str(a - b))
        if (self.answerEntry.get() == str(a - b)):
            rand_victor_sound = mixer.Sound(random.choice(self.victory_sound))
            mixer.Sound.play(rand_victor_sound)
            self.response_text_correct.grid(row=18, column=0, padx=20, columnspan=10)
            self.nextSubButton.grid(row=22, column=0, columnspan=10)
        else:
            rand_wrong_sound = mixer.Sound(random.choice(self.elimination_sound))
            mixer.Sound.play(rand_wrong_sound)
            self.response_text_sorry_wrong.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            if self.bttn_clicks >= 3:
                self.response_text_sorry_wrong.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextSubButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def subFunc(self):
        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()
        self.bttn_clicks = 0
        self.maxlabel.grid_forget()
        self.nextSubButton.grid_forget()
        self.nextButton.grid_forget()
        self.nextMulButton.grid_forget()
        self.exitButton.grid_forget()
        photo_list = []
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        question_text = Label(self.root, font=(None, 18), text="what do you think the difference of these two numbers are? ", bg="white")
        num = f"{a} - {b}"

        if self.pa or self.pb:
            for i in range(0, self.pa):
                self.pl[i].grid_forget()
            for i in range(0, self.pb):
                self.pl[i + self.pa].grid_forget()

        if (a + b) > 0:
            imglabel = Label(self.root, font=(None, 18), text="OR", bg="white")
            imglabel.grid(row=2, column=2, pady=25, columnspan=10)
            self.arrange_ball_images("-", a, b)

        problem = Label(self.root, font=(None, 50), text=num, bg="white")
        submit_button = Button(self.root, text=" Submit ", highlightbackground='#3E4149',
                           command=lambda: self.checkSub(a, b))

        question_text.grid(row=0, column=2, pady=15, columnspan=10)
        problem.grid(row=1, column=2, pady=5, columnspan=10)
        self.answerEntry.grid(row=15, column=2, pady=(50, 5), padx=20, columnspan=10)
        submit_button.grid(row=16, column=2, pady=5, columnspan=10)

    def checkMul(self, a, b):
        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()
        print("Mul:", self.answerEntry.get(), ">>>", str(a * b))
        if (self.answerEntry.get() == str(a * b)):
            self.response_text_correct.grid(row=18, column=0, padx=20, columnspan=10)
            self.nextMulButton.grid(row=22, column=0, columnspan=10)
        else:
            self.response_text_sorry_wrong.grid(row=18, column=0, padx=20, columnspan=10)
            self.bttn_clicks += 1
            if self.bttn_clicks >= 3:
                self.response_text_sorry_wrong.grid_forget()
                self.maxlabel.grid(row=20, column=0, padx=20, columnspan=10)
                self.nextMulButton.grid(row=22, column=0, columnspan=10)
                self.exitButton.grid(row=24, column=0, columnspan=10)

    def mulFunc(self):
        self.response_text_correct.grid_forget()
        self.response_text_sorry_wrong.grid_forget()
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
        self.answerEntry.grid(row=15, column=0, pady=5, padx=20, columnspan=10)
        mulButton.grid(row=16, column=0, pady=5, padx=20, columnspan=10)

    def exitFunc(self):
        quit()

    def restart_program(self):
        pass
        # python = sys.executable
        # os.execl(python, python, *sys.argv)

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
            photo_list[-1].grid(row=3, column=3 + i)

        labelplus = Label(self.root, font=(None, 40), text=sign, bg="black", fg="white")
        labelplus.grid(row=4, column=3)

        for i in range(0, b):
            photo_list.append(Label(self.root, image=self.img2))
            photo_list[-1].grid(row=5, column=3 + i)
        self.pa = a
        self.pb = b
        self.pl = photo_list






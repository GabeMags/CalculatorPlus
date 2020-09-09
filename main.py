# This app was created to be a calculator with fun and unexpected features. It is a 3-manned project overall.
# This is Gabriel Magallanes's contributions (for better or for worse)
# CSUF Fall 2020 - CPSC

import random
import tkinter as tk
import time
# Note: I had to manually install imagetk with the command:  sudo apt-get install python3-pil.imagetk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk


# Various settings that the whole app will use. Maybe I'll make a settings file?
window_width = 1280
window_height = 720
app_title = "Calculator Plus"


class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        # Basic window parameters
        self.title(app_title)
        self.geometry("%dx%d+0+0" % (window_width, window_height))

        # Create a frame to pack the widgets in
        canvas = Frame(self)
        canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Set the splash background image. ImageTk needs to be used for expanded image file compatibility
        input_image = Image.open("splash.jpg")
        background = ImageTk.PhotoImage(input_image)

        # Abandoned style code to make the progress bar have an image instead of a color
        # This code block goes before the splash_progress_bar is initialized
        #bar_style = Style(self)  # Style() uses ttk
        # add a label in the layout
        #bar_style.layout('Horizontal.TProgressbar',
        #             [('Horizontal.Progressbar.trough',
        #               {'children': [('Horizontal.Progressbar.splash_progress_bar',
        #                              {'side': 'left', 'sticky': 'ns'})],
        #                'sticky': 'nswe'}),
        #              ('Horizontal.Progressbar.label', {'sticky': ''})])
        #
        # set the label to have a background image that expands with the progress bar
        #bar_style.configure('Horizontal.TProgressbar.label', image=background, fill=X, expand=True)

        # Fake progress bar widget
        # (determinate mode animates it for us)
        splash_progress_bar = Progressbar(canvas, orient=HORIZONTAL, length=100, mode='determinate')
        splash_progress_bar.pack(side=BOTTOM, fill=X, padx=5, pady=5)

        # Pack the background with the splash text on top
        panel = tk.Label(canvas, image=background, text=app_title, font=("Arial", 25, "bold"), compound="center")
        panel.pack(side=BOTTOM, fill=X)
        panel.image = background

        # Function responsible for
        # the progress bar value.
        # The splash destructs after this bar is done
        def fake_loading():
            import time
            splash_progress_bar['value'] = 20
            self.update_idletasks()
            time.sleep(0.5)

            splash_progress_bar['value'] = 40
            self.update_idletasks()
            time.sleep(0.5)

            splash_progress_bar['value'] = 50
            self.update_idletasks()
            time.sleep(0.5)

            splash_progress_bar['value'] = 60
            self.update_idletasks()
            time.sleep(0.5)

            splash_progress_bar['value'] = 80
            self.update_idletasks()
            time.sleep(0.5)

            splash_progress_bar['value'] = 100
            self.update_idletasks()
            time.sleep(0.5)

        fake_loading()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = SplashScreen(self)

        # Basic window parameters
        self.title(app_title)
        self.geometry("%dx%d+0+0" % (window_width, window_height))

        # ----LOADING SCREEN-----
        # Simulate a loading delay in seconds
        # (this was removed since the loading bar now determines load duration)
        #time.sleep(2)

        # Finished loading so destroy splash
        splash.destroy()
        # Show window again
        self.deiconify()

        # -----MAIN APP-----
        # Create a frame to pack the widgets in
        canvas = Frame(self)
        canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()


#def calculator_plus_main():
#    # Create the tk window
#    main_window = Tk()
#    main_window.title("Calculator Plus")
#
#    # Position the question in the window
#    question_label = Label(main_window, text=new_question())
#
#
#def new_question():
#    # Generate two random numbers between 0 and 9
#    num1 = random.randint(0, 9)
#    num2 = random.randint(0, 9)
#
#    # Create a question for the user
#    question = num1 + "+" + num2
#
#    return question

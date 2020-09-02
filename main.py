import random
import tkinter as tk
import time
# Note: I had to manually install imagetk with the command:  sudo apt-get install python3-pil.imagetk
from PIL import Image, ImageTk

# Various settings. Maybe make a settings file?
window_width = 480
window_height = 720
app_title = "Calculator Plus"


class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        # Basic window parameters
        self.title(app_title)
        self.geometry("%dx%d+0+0" % (window_width, window_height))

        # Set the splash background image. ImageTk needs to be used for expanded image file compatibility
        input_image = Image.open("splash.jpg")
        background = ImageTk.PhotoImage(input_image)

        # Pack the background with the splash text on top
        panel = tk.Label(self, image=background, text=app_title, font=("Arial", 25, "bold"), compound="center")
        panel.pack(fill='both', expand='yes')
        panel.image = background

        # Implement the loading bar (extra- not implemented yet)
        # Nothing here!

        # This makes the window show before the mainloop
        self.update()


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
        time.sleep(3)
        # Finished loading so destroy splash
        splash.destroy()
        # Show window again
        self.deiconify()

        # -----MAIN APP-----





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

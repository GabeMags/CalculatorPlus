# This app was created to be a calculator with fun and unexpected features. It is a 3-manned project overall.
# This is Gabriel Magallanes's contributions (for better or for worse)
# CSUF Fall 2020 - CPSC

import pygame, sys
import os  # I'm using this to make sure that my external code is included
import random
import tkinter as tk
import time
# Note: I had to manually install imagetk with the command:  sudo apt-get install python3-pil.imagetk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()

# Application settings
app_title = 'Calculator Plus'
window_width = 1280
window_height = 720
# Just to make things easy
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_black = (0, 0, 0)
center_coordinates = (640, 360)  # (x, y)
center_top_coordinates = '640, 20'


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

        # Fake progress bar widget
        # (determinate mode animates it for us)
        splash_progress_bar = Progressbar(canvas, orient=HORIZONTAL, length=100, mode='determinate')
        splash_progress_bar.pack(side=BOTTOM, fill=X, padx=5, pady=5)

        # Pack the background with the splash text on top
        panel = tk.Label(canvas, image=background, text=app_title, font=("Arial", 25, "bold"), compound="center")
        panel.pack(side=TOP, fill=X)
        panel.image = background

        # Function responsible for
        # the progress bar value.
        # The splash destructs after this bar is done
        def fake_loading():
            import time
            for loadingProgress in range(1, 100):
                splash_progress_bar['value'] = loadingProgress
                self.update_idletasks()
                self.update()
                time.sleep(0.03)

        fake_loading()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = SplashScreen(self)

        # Basic window parameters
        self.title(app_title)
        self.geometry("%dx%d+0+0" % (window_width, window_height))

        # Finished loading so destroy splash
        splash.destroy()
        # Show window again
        # self.deiconify()

        # -----MAIN APP----- This is where pygame comes into play for main GUI
        # pygame.display.set_caption(app_title)
        self.screen = pygame.display.set_mode((window_width, window_height), 0, 32)

        screen = self.screen

        app_font_and_size = pygame.font.SysFont(None, 20)  # Size 20 font with default font type

        # Function to draw text wherever I need to
        # centered is a boolean- if false, then use x y
        # is_title_text is a boolean- if false, then use x y
        def draw_text(text, font, font_color, surface, x, y, true_centered, is_title_text):
            text_obj = font.render(text, 1, font_color)

            if not true_centered:
                if not is_title_text:
                    text_rect = text_obj.get_rect()  # Todo: get rect son lol
                    text_rect.top_left = (x, y)  # set the text rectangle to be the literal x,y passed to this func
                if is_title_text:
                    text_rect = text_obj.get_rect(center=(window_width / 2, 20))  # Special spot for the title only

            if true_centered:  # Todo: who knows if I'll actually use this
                text_rect = text_obj.get_rect(center=(window_width / 2, window_height / 2))  # Todo: Lol get rect son

            surface.blit(text_obj, text_rect)

        click = False

        def home_screen():
            while True:
                screen.fill((0, 0, 0))
                # Todo: I want to change this from just text to a graphic for the title? maybe?
                # Technically the x and y don't matter here so I made them 404 (arbitrary)
                draw_text(app_title, app_font_and_size, color_white, screen, 404, 404, False, True)

                # Mouse cursor location tracking
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Button objects [without text] and their locations
                button_kids_calc = pygame.Rect(280, 500, 200, 50)  # Rect(dist from left, dist from top, width, height)
                button_std_calc = pygame.Rect(560, 500, 200, 50)
                button_camera_calc = pygame.Rect(840, 500, 200, 50)
                button_options = pygame.Rect(1160, 500, 200, 50)

                # Logic for clicking on the buttons (maybe make this into a switch case? i know its not elegant)
                # Yes, buttons are basically collision-tracking rectangles.
                if button_kids_calc.collidepoint((mouse_x, mouse_y)):
                    if click:
                        kids_calculator()
                if button_std_calc.collidepoint((mouse_x, mouse_y)):
                    if click:
                        standard_calculator()
                if button_camera_calc.collidepoint((mouse_x, mouse_y)):
                    if click:
                        pass  # Todo: camera
                if button_options.collidepoint((mouse_x, mouse_y)):
                    if click:
                        pass  # Todo: options

                # Drawing buttons to the screen with their styles
                pygame.draw.rect(screen, color_red, button_kids_calc)
                pygame.draw.rect(screen, color_red, button_std_calc)
                pygame.draw.rect(screen, color_red, button_camera_calc)
                pygame.draw.rect(screen, color_red, button_options)

                click = False

                # Check for keypress/clicks
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        def kids_calculator():
            running = True
            while running:
                screen.fill(color_black)

                draw_text('Kids Calculator', app_font_and_size, color_white, screen, 20, 20, False, True)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        def standard_calculator():
            running = True
            while running:
                screen.fill(color_black)

                draw_text('Standard Calculator', app_font_and_size, color_white, screen, 20, 20, False, True)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        def camera_calculator():
            running = True
            while running:
                screen.fill(color_black)

                draw_text('Camera Calculator', app_font_and_size, color_white, screen, 20, 20)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        home_screen()


if __name__ == "__main__":
    app = App()
    app.mainloop()

# def calculator_plus_main():
#    # Create the tk window
#    main_window = Tk()
#    main_window.title("Calculator Plus")
#
#    # Position the question in the window
#    question_label = Label(main_window, text=new_question())
#
#
# def new_question():
#    # Generate two random numbers between 0 and 9
#    num1 = random.randint(0, 9)
#    num2 = random.randint(0, 9)
#
#    # Create a question for the user
#    question = num1 + "+" + num2
#
#    return question

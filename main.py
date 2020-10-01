# This app was created to be a calculator with fun and unexpected features. It is a 3-manned project overall.
# This is Gabriel Magallanes's contributions (for better or for worse)
# CSUF Fall 2020 - CPSC
import numpy
import pygame, sys
import os  # I'm using this to make sure that my external code is included
import random
import tkinter as tk
import time
import cv2
import pytesseract
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
WHITE_RGB = (255, 255, 255)
RED_RGB   = (255, 0, 0)
GREEN_RGB = (0, 255, 0)
BLUE_RGB  = (0, 0, 255)
BLACK_RGB = (0, 0, 0)
LGREY_RGB = (196, 196, 196)
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

        # -----MAIN APP----- This is where pygame comes into play for main GUI
        # pygame.display.set_caption(app_title)
        self.screen = pygame.display.set_mode((window_width, window_height), 0, 32)

        screen = self.screen

        font = pygame.font.SysFont(None, 20)  # Size 20 font with default font type

        # Function to draw text wherever I need to. NOTE:
        # true_centered is a boolean- if true, then center it in the middle of the screen
        #                               if false, use x, y
        # is_title_text is a boolean- if it's true, it is placed in the title area of the screen
        def draw_text(text, font, font_color, surface, x, y, true_centered, is_title_text):
            text_obj = font.render(text, 1, font_color)

            if not true_centered:
                if not is_title_text:
                    text_rect = text_obj.get_rect()  # Todo: get rect son lol
                    text_rect.center = (x, y)  # set the text rectangle to be the literal x,y passed to this func
                if is_title_text:
                    text_rect = text_obj.get_rect(center=(window_width / 2, 20))  # Special spot for the title only

            if true_centered:  # This puts text in the very center of the application window
                text_rect = text_obj.get_rect(center=(window_width / 2, window_height / 2))  # Todo: Lol get rect son

            surface.blit(text_obj, text_rect)

        click = False



        def home_screen():
            while True:
                screen.fill(WHITE_RGB)
                # Todo: I want to change this from just text to a graphic for the title? maybe?
                # Technically the x and y don't matter here so I made them 404 (arbitrary)
                draw_text(app_title, font, BLACK_RGB, screen, 404, 404, False, True)
                draw_text('HOME_SCREEN', font, BLACK_RGB, screen, window_width/2, 200, False, False)
                draw_text('Click on one of the buttons below to start a mode! Press ESC to quit program', font, BLACK_RGB, screen, 20, 20, True, False)

                # Mouse cursor location tracking
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Button objects [without text] and their locations
                button_kids_calc = pygame.Rect(280, 500, 200, 50)  # Rect(dist from left, dist from top, width, height)
                button_std_calc = pygame.Rect(560, 500, 200, 50)
                button_camera_calc = pygame.Rect(840, 500, 200, 50)
                button_options = pygame.Rect(1160, 500, 200, 50)

                # Drawing buttons to the screen with their styles
                pygame.draw.rect(screen, LGREY_RGB, button_kids_calc)
                pygame.draw.rect(screen, LGREY_RGB, button_std_calc)
                pygame.draw.rect(screen, LGREY_RGB, button_camera_calc)
                #pygame.draw.rect(screen, LGREY_RGB, button_options)
                
                #button_kids_calc.get_rect(center=())

                # Drawing the text labels onto the buttons
                draw_text('Kiddie Calculator', font, BLACK_RGB, screen, button_kids_calc.centerx, button_kids_calc.centery, False, False)
                draw_text('Standard Calculator', font, BLACK_RGB, screen, button_std_calc.centerx, button_std_calc.centery, False, False)
                draw_text('Camera Calculator', font, BLACK_RGB, screen, button_camera_calc.centerx, button_camera_calc.centery, False, False)

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
                        camera_calculator()
                if button_options.collidepoint((mouse_x, mouse_y)):
                    if click:
                        pass  # Todo: options mode needs to be written

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
                # Usual display visuals
                screen.fill(RED_RGB)
                draw_text('Kids Calculator', font, WHITE_RGB, screen, 20, 20, False, True)
                draw_text('PRESS ESCAPE TO RETURN TO MAIN MENU', font, WHITE_RGB, screen, 20, 20, True, False)

                # TODO: MIRWAIS'S CODE GOES HERE

                # Logic for returning to the main screen or quitting program
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
                screen.fill(GREEN_RGB)

                draw_text('Standard Calculator', font, BLACK_RGB, screen, 20, 20, False, True)
                draw_text('PRESS ESCAPE TO RETURN TO MAIN MENU', font, BLACK_RGB, screen, 20, 20, True, False)

                # Todo: add in code for the standard calc

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

            camera_index = 0
            camera = cv2.VideoCapture(camera_index)
            camera.set(3, 640)
            camera.set(4, 480)

            while running:
                screen.fill(BLUE_RGB)

                draw_text('Camera Calculator', font, WHITE_RGB, screen, 20, 20, False, True)
                draw_text('PRESS ESCAPE TO RETURN TO MAIN MENU', font, WHITE_RGB, screen, 20, 20, True, False)

                # Todo: code for the camera calc goes here

                #pytesseract.pytesseract.tesseract_cmd =

                #img = cv2.imread('6+9_irl.jpeg')
                retval, img = camera.read()
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                print(pytesseract.image_to_string(img))
                img = numpy.rot90(img)
                img = numpy.flip(img, axis=0)  # Flipped about the Y axis
                img = pygame.surfarray.make_surface(img)
                screen.blit(img, (0,100))
                #cv2.imshow('Result', img)
                cv2.waitKey(200)



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













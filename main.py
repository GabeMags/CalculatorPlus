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
from pygame import surfarray, mixer
import KidsCalc_tk_App as KidCalc

# Note: I had to manually install imagetk with the command:  sudo apt-get install python3-pil.imagetk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from pygame.locals import *
import ImageLabelClass as gif_handler


mainClock = pygame.time.Clock()

pygame.init()

# Application settings
app_title = 'Calculator Plus'
window_width = 1280
window_height = 720
# Just to make things easy
WHITE_RGB = (255, 255, 255)
RED_RGB = (255, 0, 0)
GREEN_RGB = (0, 255, 0)
BLUE_RGB = (0, 0, 255)
BLACK_RGB = (0, 0, 0)
LGREY_RGB = (206, 206, 206)
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
        input_image = Image.open("backgrounds/splash.jpg")
        background = ImageTk.PhotoImage(input_image)

        # The Devs!
        self.fall_guy_gif_GM = gif_handler.ImageLabel(self)
        self.fall_guy_gif_SM = gif_handler.ImageLabel(self)
        self.fall_guy_gif_MM = gif_handler.ImageLabel(self)

        self.fall_guy_gif_GM.place(x=300, y=400, anchor="nw")
        self.fall_guy_gif_GM.load('backgrounds/pixelfallguy_loading.gif', 155, 135)

        self.fall_guy_gif_SM.place(x=550, y=400, anchor="nw")
        self.fall_guy_gif_SM.load('backgrounds/pixelfallguy_loading.gif', 155, 135)

        self.fall_guy_gif_MM.place(x=800, y=400, anchor="nw")
        self.fall_guy_gif_MM.load('backgrounds/pixelfallguy_loading.gif', 155, 135)

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

        # Load kitty calc mode music
        mixer.init()
        mixer.music.load("audio/Everybody_Falls_(Fall_Guys_Theme).mp3")
        mixer.music.set_volume(0.5)

        # Finished loading so destroy splash
        splash.destroy()

        # -----MAIN APP----- This is where pygame comes into play for main GUI
        # pygame.display.set_caption(app_title)
        self.screen = pygame.display.set_mode((window_width, window_height), 0, 32)

        screen = self.screen

        font_sm = pygame.font.SysFont(None, 20)  # Size 20 small font
        font_med = pygame.font.SysFont(None, 35)  # Size 35 medium font

        click = False

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

        def home_screen():
            while True:
                click = False
                screen.fill(WHITE_RGB)
                # Todo: I want to change this from just text to a graphic for the title? maybe?
                # Technically the x and y don't matter here so I made them 404 (arbitrary)
                draw_text(app_title, font_med, BLACK_RGB, screen, 404, 404, False, True)
                draw_text('HOME_SCREEN', font_med, BLACK_RGB, screen, window_width / 2, 200, False, False)
                draw_text('Click on one of the buttons below to start a mode! Press ESC to quit program', font_sm,
                          BLACK_RGB, screen, 20, 20, True, False)

                # Mouse cursor location tracking
                mouse_x, mouse_y = pygame.mouse.get_pos()

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

                # Button objects [without text] and their locations
                button_kids_calc = pygame.Rect(280, 500, 200, 50)  # Rect(dist from left, dist from top, width, height)
                button_camera_calc = pygame.Rect(840, 500, 200, 50)

                # Drawing buttons to the screen with their styles
                pygame.draw.rect(screen, LGREY_RGB, button_kids_calc)
                pygame.draw.rect(screen, LGREY_RGB, button_camera_calc)

                # Drawing the text labels onto the buttons
                draw_text('Kiddie Calculator', font_sm, BLACK_RGB, screen, button_kids_calc.centerx,
                          button_kids_calc.centery, False, False)
                draw_text('Camera Calculator', font_sm, BLACK_RGB, screen, button_camera_calc.centerx,
                          button_camera_calc.centery, False, False)

                # Yes, buttons are basically collision-tracking rectangles.
                if button_kids_calc.collidepoint((mouse_x, mouse_y)):
                    if click:
                        # Play Fall Guys soundtrack
                        mixer.music.play(-1)

                        # Launch the module
                        subprocess = KidCalc.Application(self)
                        subprocess.calc_For_Kids()
                if button_camera_calc.collidepoint((mouse_x, mouse_y)):
                    if click:
                        camera_calculator()

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        # def kids_calculator():
        #     running = True
        #     click= False
        #     # question = math.gen_question()
        #
        #     # Process the picture in the given path and make a complete button surface object
        #     def make_button_surface(file, is_number_button=True):
        #         # Load a picture with its transparency alphas
        #         picture_to_process = pygame.image.load('button_images/' + str(file)).convert_alpha()
        #
        #         if is_number_button:
        #             # Transform picture as a number button
        #             picture = pygame.transform.scale(picture_to_process, (200, 180))
        #
        #             # Make a surface that will act as a button
        #             surface = pygame.Surface((80, 80))
        #             # surface.fill(LGREY_RGB)
        #
        #             # Put the picture onto the button surface
        #             surface.blit(picture, (-60, -50))
        #         else:
        #             # Transform picture as an action button
        #             picture = pygame.transform.scale(picture_to_process, (350, 280))
        #
        #             # Make a surface that will act as a button
        #             surface = pygame.Surface((160, 80))
        #             # surface.fill(LGREY_RGB)
        #
        #             # Put the picture onto the button surface
        #             surface.blit(picture, (-104, -104))
        #
        #         return surface
        #
        #     # Load up the images for the buttons (passive)
        #     b0_surface = make_button_surface('0 inactive.png')
        #     b1_surface = make_button_surface('1 inactive.png')
        #     b2_surface = make_button_surface('2 inactive.png')
        #     b3_surface = make_button_surface('3 inactive.png')
        #     b4_surface = make_button_surface('4 inactive.png')
        #     b5_surface = make_button_surface('5 inactive.png')
        #     b6_surface = make_button_surface('6 inactive.png')
        #     b7_surface = make_button_surface('7 inactive.png')
        #     b8_surface = make_button_surface('8 inactive.png')
        #     b9_surface = make_button_surface('9 inactive.png')
        #     bdelete_surface = make_button_surface('delete inactive.png', False)
        #     b0_active_surface = make_button_surface('0 active.png')
        #     b1_active_surface = make_button_surface('1 active.png')
        #     b2_active_surface = make_button_surface('2 active.png')
        #     b3_active_surface = make_button_surface('3 active.png')
        #     b4_active_surface = make_button_surface('4 active.png')
        #     b5_active_surface = make_button_surface('5 active.png')
        #     b6_active_surface = make_button_surface('6 active.png')
        #     b7_active_surface = make_button_surface('7 active.png')
        #     b8_active_surface = make_button_surface('8 active.png')
        #     b9_active_surface = make_button_surface('9 active.png')
        #     bdelete_active_surface = make_button_surface('delete active.png', False)
        #     # benter_surface = make_button_surface('enter inactive.png')
        #
        #     def start_from_gui():
        #         running = True
        #         app2 = KidCalc.Application()
        #         while running:
        #             # PROGRAM EXECUTION STARTS HERE
        #             app2.calc_For_Kids()
        #
        #     while running:
        #         # Usual display visuals
        #         screen.fill(LGREY_RGB)
        #
        #         draw_text('Kids Calculator', font_med, WHITE_RGB, screen, 20, 20, False, True)
        #         # draw_text('PRESS ESCAPE TO RETURN TO MAIN MENU', font, WHITE_RGB, screen, 20, 20, True, False)
        #         # draw_text(question, font_med, WHITE_RGB, screen, 20, 20, True, False)
        #
        #         # Mouse cursor location tracking
        #         mouse_x, mouse_y = pygame.mouse.get_pos()
        #
        #         # Active buttons
        #         # ROW 0
        #         screen.blit(b7_active_surface, (900, 200))
        #         screen.blit(b8_active_surface, (980, 200))
        #         screen.blit(b9_active_surface, (1060, 200))
        #         # ROW 1
        #         screen.blit(b4_active_surface, (900, 280))
        #         screen.blit(b5_active_surface, (980, 280))
        #         screen.blit(b6_active_surface, (1060, 280))
        #         # ROW 2
        #         screen.blit(b1_active_surface, (900, 360))
        #         screen.blit(b2_active_surface, (980, 360))
        #         screen.blit(b3_active_surface, (1060, 360))
        #         # ROW 3
        #         screen.blit(b0_active_surface, (900, 440))
        #         screen.blit(bdelete_active_surface, (980, 440))
        #
        #         # Inactive Buttons
        #         # ROW 0
        #         screen.blit(b7_surface, (900, 200))
        #         b7_rect = pygame.Rect(900, 200, 80, 80)
        #         screen.blit(b8_surface, (980, 200))
        #         b8_rect = pygame.Rect(980, 200, 80, 80)
        #         screen.blit(b9_surface, (1060, 200))
        #         b9_rect = pygame.Rect(1060, 200, 80, 80)
        #         # ROW 1
        #         screen.blit(b4_surface, (900, 280))
        #         b4_rect = pygame.Rect(900, 280, 80, 80)
        #         screen.blit(b5_surface, (980, 280))
        #         b5_rect = pygame.Rect(980, 280, 80, 80)
        #         screen.blit(b6_surface, (1060, 280))
        #         b6_rect = pygame.Rect(1060, 280, 80, 80)
        #         # ROW 2
        #         screen.blit(b1_surface, (900, 360))
        #         b1_rect = pygame.Rect(900, 360, 80, 80)
        #         screen.blit(b2_surface, (980, 360))
        #         b2_rect = pygame.Rect(980, 360, 80, 80)
        #         screen.blit(b3_surface, (1060, 360))
        #         b3_rect = pygame.Rect(1060, 360, 80, 80)
        #         # ROW 3
        #         screen.blit(b0_surface, (900, 440))
        #         b0_rect = pygame.Rect(900, 440, 80, 80)
        #         screen.blit(bdelete_surface, (980, 440))
        #         bdelete_rect = pygame.Rect(980, 440, 160, 80)
        #
        #         # Logic for having hover buttons through pygame
        #         if b7_rect.collidepoint(pygame.mouse.get_pos()):
        #             b7_surface.set_alpha(0)
        #         else:
        #             b7_surface.set_alpha(255)
        #         if b8_rect.collidepoint(pygame.mouse.get_pos()):
        #             b8_surface.set_alpha(0)
        #         else:
        #             b8_surface.set_alpha(255)
        #         if b9_rect.collidepoint(pygame.mouse.get_pos()):
        #             b9_surface.set_alpha(0)
        #         else:
        #             b9_surface.set_alpha(255)
        #         if b4_rect.collidepoint(pygame.mouse.get_pos()):
        #             b4_surface.set_alpha(0)
        #         else:
        #             b4_surface.set_alpha(255)
        #         if b5_rect.collidepoint(pygame.mouse.get_pos()):
        #             b5_surface.set_alpha(0)
        #         else:
        #             b5_surface.set_alpha(255)
        #         if b6_rect.collidepoint(pygame.mouse.get_pos()):
        #             b6_surface.set_alpha(0)
        #         else:
        #             b6_surface.set_alpha(255)
        #         if b1_rect.collidepoint(pygame.mouse.get_pos()):
        #             b1_surface.set_alpha(0)
        #         else:
        #             b1_surface.set_alpha(255)
        #         if b2_rect.collidepoint(pygame.mouse.get_pos()):
        #             b2_surface.set_alpha(0)
        #         else:
        #             b2_surface.set_alpha(255)
        #         if b3_rect.collidepoint(pygame.mouse.get_pos()):
        #             b3_surface.set_alpha(0)
        #         else:
        #             b3_surface.set_alpha(255)
        #         #Delete/0 buttons
        #         if b0_rect.collidepoint(pygame.mouse.get_pos()):
        #             b0_surface.set_alpha(0)
        #         else:
        #             b0_surface.set_alpha(255)
        #         if bdelete_rect.collidepoint(pygame.mouse.get_pos()):
        #             bdelete_surface.set_alpha(0)
        #             # TODO: make a dedicated button for launching kids calc
        #             subprocess = KidCalc.Application(self)
        #             subprocess.calc_For_Kids()
        #         else:
        #             bdelete_surface.set_alpha(255)
        #
        #         # Logic for returning to the main screen or quitting program
        #         for event in pygame.event.get():
        #             if event.type == QUIT:
        #                 pygame.quit()
        #                 sys.exit()
        #             if event.type == KEYDOWN:
        #                 if event.key == K_ESCAPE:
        #                     running = False
        #             if event.type == MOUSEBUTTONDOWN:
        #                 if event.button == 1:
        #                     click = True
        #
        #         pygame.display.update()
        #         mainClock.tick(60)  # Todo: Idk what this really does

        def camera_calculator():

            running = True

            camera_index = 0
            camera = cv2.VideoCapture(camera_index)
            camera.set(3, 640)
            camera.set(4, 480)

            while running:
                click = False
                screen.fill(BLUE_RGB)

                draw_text('Camera Calculator', font_sm, WHITE_RGB, screen, 20, 20, False, True)
                draw_text('PRESS ESCAPE TO RETURN TO MAIN MENU', font_sm, WHITE_RGB, screen, 20, 20, True, False)

                # Todo: code for the camera calc goes here

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True

                # pytesseract.pytesseract.tesseract_cmd =

                # Mouse cursor location tracking
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Button objects [without text] and their locations
                button_capture_frame = pygame.Rect(280, 600, 200,
                                                   50)  # Rect(dist from left, dist from top, width, height)

                # Drawing buttons to the screen with their styles
                pygame.draw.rect(screen, LGREY_RGB, button_capture_frame)

                # Drawing the text labels onto the buttons
                draw_text('Capture!', font_sm, BLACK_RGB, screen, button_capture_frame.centerx,
                          button_capture_frame.centery, False, False)

                retval, img = camera.read()
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = numpy.rot90(img)
                img = numpy.flip(img, axis=0)  # Flipped about the Y axis
                img = pygame.surfarray.make_surface(img)
                screen.blit(img, (0, 100))

                def number_crunch():
                    retval, img = camera.read()
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    problem = pytesseract.image_to_string(img)
                    try:
                        print(problem)
                        print(eval(problem))
                    except:
                        print("error")

                if button_capture_frame.collidepoint(mouse_x, mouse_y):
                    if click:
                        number_crunch()

                pygame.display.update()
                mainClock.tick(60)  # Todo: Idk what this really does

        home_screen()


if __name__ == "__main__":
    app = App()
    app.mainloop()

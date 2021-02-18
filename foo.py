import pygame
from tkinter import *

def haha():
        
    pygame.init()
    pygame.mixer.music.load("testSong.ogg")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pass

class mplay:

    win = Tk()

    b1 = Button(win, text="anupam")
    b1.configure(command=haha)

    b1.pack();

    win.mainloop()
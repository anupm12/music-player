from tkinter import *
import tkinter
import pygame
from PIL import ImageTk,Image 
import os

window = Tk()
window.geometry("1000x500+200+100")

class musicPlayer:
    pygame.init()

    def __init__(self, window):
        self.window = window
        self.tracker=FALSE
        self.userInteface()
    
    def userInteface(self):
        audioDetails = Frame(self.window)
        audioDetails.grid(row=0, column=0, sticky="nsew")

        self.canvas = Canvas(audioDetails)
        self.img = ImageTk.PhotoImage(Image.open("haha.png"))
        self.canvas.create_image(0, 0, image=self.img)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        audioDetails.grid_columnconfigure(0, weight=1)
        audioDetails.grid_rowconfigure(0, weight=1)

        playlist = Frame(self.window)
        playlist.grid(row=0, column=1, sticky="nsew")

        self.playlistList = Listbox(playlist, selectmode=SINGLE, background="bisque")
        self.playlistList.grid(row=0, column=0, sticky="nsew")

        os.chdir("/media/anupam/Local Disk1/Music/new/Music files/edm")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlistList.insert(END,track)

        playlist.grid_columnconfigure(0, weight=1)
        playlist.grid_rowconfigure(0, weight=1)

        # pause button
        self.pauseButton = Button(self.window, text="Pause", padx=40, pady=20)
        self.pauseButton.configure(command=self.pauseSong)
        self.pauseButton.grid(row=1, column=0)

        # stop button
        stopButton = Button(self.window, text="Stop", padx=40, pady=20)
        stopButton.configure(command=self.stopSong)
        stopButton.grid(row=1, column=1)

        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=4)
        self.window.grid_rowconfigure(1, weight=1)

        







        



    def playSong(self):
        pygame.mixer.music.load("testSong.ogg")
        pygame.mixer.music.set_volume(1.0)
        self.tracker=TRUE
        self.pauseButton.configure(text="Pause")
        pygame.mixer.music.play()
    
    def pauseSong(self):
        if(self.tracker):
            pygame.mixer.music.pause()
            self.pauseButton.configure(text="Play")
            self.tracker=FALSE
        else:
            pygame.mixer.music.unpause()
            self.pauseButton.configure(text="Pause")
            self.tracker=TRUE

    def stopSong(self):
        pygame.mixer.music.stop()
    

musicPlayer(window)
window.mainloop()
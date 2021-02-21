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
        self.window.title("MusicPlayer")
        self.window.configure(background='#4A4A4A')
        self.tracker=FALSE
        self.userInteface()
    
    def userInteface(self):
        self.playIcon = ImageTk.PhotoImage(Image.open("Resources/Icons/play.png"))
        self.pauseIcon = ImageTk.PhotoImage(Image.open("Resources/Icons/pause.png"))
        self.stopIcon = ImageTk.PhotoImage(Image.open("Resources/Icons/stop.png"))

        audioDetails = Frame(self.window, bg="#4A4A4A", bd=10)
        audioDetails.grid(row=0, column=0, sticky="nsew")

        self.canvas = Canvas(audioDetails, bd=0, highlightthickness=0)
        self.image = ImageTk.PhotoImage(Image.open("Resources/Images/bg.jpg"))
        self.canvas.create_image(0, 0, image=self.image)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.audioName = Label(audioDetails, text="Song Name", font=("Ubuntu Mono",30,""), bg="#4A4A4A", fg="white")
        self.audioName.grid(row=0, column=0)

        audioDetails.grid_columnconfigure(0, weight=1)
        audioDetails.grid_rowconfigure(0, weight=1)

        playlist = Frame(self.window, bg="#4A4A4A", bd=10)
        playlist.grid(row=0, column=1, sticky="nsew")

        self.playlistList = Listbox(playlist, selectmode=SINGLE, font=("Ubuntu Mono",11,""), bg="#4A4A4A", fg="white", bd=0, highlightthickness=0)
        self.playlistList.bind('<Double-1>', self.playSong) 
        self.playlistList.grid(row=0, column=0, sticky="nsew")

        # os.chdir("/media/anupam/Local Disk1/Music/new/Music files/edm")
        os.chdir("/media/anupam/Local Disk/Projects/Projects/music player")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlistList.insert(END,track)

        playlist.grid_columnconfigure(0, weight=1)
        playlist.grid_rowconfigure(0, weight=1)        

        # pause button
        self.pauseButton = Button(self.window, image=self.pauseIcon, bg="#4A4A4A", bd=0, highlightthickness=0)
        self.pauseButton.configure(command=self.pauseSong)
        self.pauseButton.grid(row=1, column=0)

        # stop button
        stopButton = Button(self.window, image=self.stopIcon, bg="#4A4A4A", bd=0, highlightthickness=0)
        stopButton.configure(command=self.stopSong)
        stopButton.grid(row=1, column=1)

        self.window.grid_columnconfigure(0, weight=2)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=4)
        self.window.grid_rowconfigure(1, weight=1)

    def playSong(self, event):
        self.audioName.config(text=self.playlistList.get(ACTIVE))
        pygame.mixer.music.load(self.playlistList.get(ACTIVE))
        pygame.mixer.music.set_volume(1.0)
        self.tracker=TRUE
        pygame.mixer.music.play()
    
    def pauseSong(self):
        if(self.tracker):
            pygame.mixer.music.pause()
            self.pauseButton.configure(image=self.playIcon)
            self.tracker=FALSE
        else:
            pygame.mixer.music.unpause()
            self.pauseButton.configure(image=self.pauseIcon)
            self.tracker=TRUE

    def stopSong(self):
        pygame.mixer.music.stop()
    

musicPlayer(window)
window.mainloop()
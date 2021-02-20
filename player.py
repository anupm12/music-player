from tkinter import *
import tkinter
import pygame
from PIL import ImageTk,Image 

window = Tk()
window.geometry("1000x500+200+100")

class musicPlayer:
    pygame.init()

    def __init__(self, window):
        self.window = window
        self.tracker=FALSE
        self.userInteface()
    
    def userInteface(self):
        mainFrame = Frame(self.window)




        # audioDetails = Frame(mainFrame, bd="10", bg='#000000')
        
        
        # img = PhotoImage(file = r"C:\Users\Admin\Pictures\capture1.png") 
        # img1 = img.subsample(2, 2) 
  
        # # setting image with the help of label 
        # Label(master, image = img1).grid(row = 0, column = 2,
        # columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

        # l1 = Label(audioDetails, text="song name")
        # l1.pack(side=LEFT)

        # audioDetails.pack(expand=TRUE, side=LEFT)



        # playlist = Frame(mainFrame, bd="10", bg='cyan')
        

        l2 = Label(mainFrame, text="playlist it is")
        l2.pack(side=LEFT, fill=)

        # playlist.pack(expand=TRUE, side=LEFT)

        mainFrame.pack(side=TOP, expand=TRUE)





        # audio controls frame
        audioControls = Frame(self.window)
        audioControls.pack(side=BOTTOM)

        # play button
        playButton = Button(audioControls , text="Play")
        playButton.configure(command=self.playSong)
        playButton.pack(side=LEFT)

        # pause button
        self.pauseButton = Button(audioControls , text="Pause")
        self.pauseButton.configure(command=self.pauseSong)
        self.pauseButton.pack(side=LEFT)

        # stop button
        stopButton = Button(audioControls , text="Stop")
        stopButton.configure(command=self.stopSong)
        stopButton.pack(side=LEFT)

    
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
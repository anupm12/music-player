from tkinter import *
import pygame

window = Tk()
window.geometry("1000x500+200+100")

class musicPlayer:
    pygame.init()

    def __init__(self, window):
        self.window = window
        self.tracker=FALSE
        self.userInteface()
    
    def userInteface(self):

        # audio controls frame
        audioControls  = Frame(self.window)

        # play button
        playButton = Button(audioControls , text="Play")
        playButton.configure(command=self.playSong)
        playButton.pack(side=LEFT)

        # pause button
        self.pauseButton = Button(audioControls , text="Pause")
        self.pauseButton.configure(command=self.pauseSong)
        self.pauseButton.pack(side=LEFT)

        # stop button
        b3 = Button(audioControls , text="Stop")
        b3.configure(command=self.stopSong)
        b3.pack(side=LEFT)

        audioControls.pack(side=BOTTOM)
    
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
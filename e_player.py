import pygame
from pygame import mixer
from tkinter import*
from tkinter import filedialog
import os

def __init__ ():
    trackframe = LabelFrame(root, text = " Tracks ", font = ('arial', 17, "bold"), bg = "purple", fg = "black", bd = 3, relief = GROOVE)
    trackframe.place(x = 0, y = 0, width = 20, height = 20)
    buttonframe = LabelFrame(root, text = "control panel", font = ('arial', 17, "bold"), bg = "grey", fg = " cyan", bd = 3, relief = GROOVE)
    buttonframe.place(x = 10, y = 10, width = 20, height = 20)
    
def play_song():
    current_song = playlist.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    songstatus.set("Song Playing")
    mixer.music.play()   
    
def song_pause():
    songstatus.set("song Paused!")
    mixer.music.pause()
    
def song_stop():
    songstatus.set("Song stopped!")
    mixer.music.stop()
    
def song_resume():
    songstatus.set("Song resuming")
    mixer.music.unpause()
    
root = Tk()
root.title('Enock music Player')

mixer.init()
songstatus = StringVar()
songstatus.set("Please Choose a Song")

#loading the playlist
playlist = Listbox(root, selectmode = SINGLE, bg = "purple", fg = "black", font = ('arial', 22), width = 40 )
playlist.grid(columnspan = 20)

os.chdir(r'directory/path to folder that contains your music files')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s) 
    
#working on button

playbtn = Button(root, text = "Play", command = play_song)
playbtn.config(font = ('arial', 17), bg="red", fg = "black", padx = 18, pady = 5)
playbtn.grid(row = 1, column = 0)


pausebtn = Button(root, text = "Pause", command = song_pause)
pausebtn.config(font = ('arial', 17), bg = "blue", fg = "black", padx = 5, pady = 5)
pausebtn.grid(row = 1, column = 1)

stopbtn = Button(root, text = "Stop", command = song_stop)
stopbtn.config(font = ('arial', 17), bg = "green", fg = "black", padx = 15, pady = 5)
stopbtn.grid(row = 1, column = 2)

resumebtn = Button(root, text = "Resume", command = song_resume)
resumebtn.config(font = ('arial', 17), bg = "orange", fg = "black", padx = 5, pady = 5)
resumebtn.grid(row = 1, column = 4)


mainloop()                  

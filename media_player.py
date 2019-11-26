from tkinter.filedialog import askopenfilename
from tkinter import *
import pygame
window = Tk()
window.geometry("400x150")
window.title("media player")
pygame.mixer.init()
n = 0
filename=['0']
playlist=[]
window.tk.call('encoding', 'system', 'unicode')
def start_stop():
    global n
    global filename

    n = n + 1
    if (n % 2) != 0:
        pygame.mixer.music.pause()
        print("paused "+str(n))
    elif (n % 2) == 0:
        pygame.mixer.music.unpause()
        print("unPaused"+str(n))
    print(filename)
def get_song_name():

    global filename
    filename[0] = askopenfilename()
    pygame.mixer.music.load(filename[0])
    pygame.mixer.music.play(0)
def makeplaylist():
    global playlist
    def make_playlist():
        global playlist
        playlist.append(askopenfilename())
    def display():


        for i in range(len(playlist) - 1):
            text1.delete(1.0, END)
            text1.update()
            text1.config(state="normal")
            song=playlist[i].partition("Desktop")[2]
            text1.insert(INSERT,song+'\n')
            text1.config(state="disabled")
        text1.pack()
    make_playlist()
    display()
    print(playlist)


l1 = Label(window, text="Media PLAYER", font="times 20").pack()
b2 = Button(window, text='⏯', width=20, command=start_stop).pack()
b3 = Button(window, text='Search ?', width=20,font="times 10", command=get_song_name).pack()
b4= Button(window, text=' ⇯  play list', width=20,font="times 10", command=makeplaylist).pack()

text1=Text(window,height=20,width=20)


window.mainloop()

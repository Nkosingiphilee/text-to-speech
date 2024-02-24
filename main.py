import pyttsx3
from tkinter import *

win = Tk()
win.title("text to speech")
win.geometry("200x200")
engin = pyttsx3.init()


def play():
    name = txt.get()
    engin.say(name)
    engin.runAndWait()
    txt.delete(0, END)


txt = Entry(text=0)
txt.pack()
Button(text="listen", command=play).pack()
win.mainloop()

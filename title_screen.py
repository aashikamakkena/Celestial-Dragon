from tkinter import *
# from tkinter import tkvideo
import tkinter as tk

import time
import sys
from PIL import Image, ImageTk
import os
from itertools import count, cycle

def run():
    os.system('python test.py')


class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 
#demo :
root = tk.Tk()
lbl = ImageLabel(root)

l = tk.Label(root, text = "Celestial Dragon", bg='black', fg='white', font=('Comic Sans MS', 25, 'bold'))
lbl.load('C:\\Users\\Sai Tejaswi\\OneDrive\\Desktop\\WISE_PROJECT\\Celestial_Dragon\\giff.gif')
btn = Button(root, text="Predict Transportation", bg='black', fg="white",font=('Comic Sans MS', 10, 'bold'), command=run)
btn.place(x=60, y=190)
l.place(x=200)
lbl.pack()
root.mainloop()
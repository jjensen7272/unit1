from tkinter import *
from tkinter import ttk
from tkinter import font
import calendar
import datetime
import time


def current_time():
    second = calendar.timegm(time.gmtime())
    current_seconds = second % 60
    minutes = second // 60
    current_minutes = minutes % 60
    hour = minutes // 60
    current_hour = hour % 24
    #set time zone
    current_hour = current_hour - 6
    if current_hour >=12:
        tag=" PM"
    else:
        tag=" AM"
    #set time zone
    
    #format the output
    timex = str(current_hour)+":"+ str(current_minutes)+":"+str(current_seconds) + tag
    #xreturn
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time = current_time()
    #show the time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000, show_time)

#use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Black')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family='helvetica', size = 60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="White", background="Black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()


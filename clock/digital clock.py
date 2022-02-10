from tkinter import *
import time
screen = Tk()
screen.title("Digital clock")
def get_time():
    timeVar=time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)
Label(screen, font=("Arial", 30), text="Digital Clock", fg="grey", bg="white").pack()
clock=Label(screen, font=("Calibri", 90), bg="grey", fg="white")
clock.pack()
get_time()
screen.mainloop()
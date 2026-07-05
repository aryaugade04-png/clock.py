from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, time)

label = Label(
    root,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="cyan"
)

label.pack(anchor="center")

time()

root.mainloop()

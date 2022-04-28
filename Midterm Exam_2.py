# ---Program 2: Create a program to produce the interface. Click the button to change its background to yellow. #
# (Hint: See the figures. - 50 points)--- #

from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("400x300+20+10")


i = 1
def change_color():
    global i
    i += 1
    if i % 2 == 0:
        btn.configure(bg="yellow")
    else:
        btn.configure(bg="white")


btn = Button(window, text="Click to Change color", bg="white", command=change_color)
btn.place(relx=.5, y=150, anchor="center")

window.mainloop()

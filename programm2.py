from tkinter import *
from PIL import ImageTk, Image
import threading

root = Tk()
root.geometry('600x600')
canvas = Canvas(root, width=600, height=600)
canvas.pack()


def load_image(name):
    img = Image.open(name)
    img.thumbnail((600, 600), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def set_image(image):
    canvas.delete("all")
    canvas.create_image(300, 300, image=image)


def f():
    threading.Timer(1, f).start()
    g = open('db.txt')
    number = g.read()
    if number == "swap0":
        set_image(image0)
    elif number == "swap1":
        set_image(image1)
    elif number == "swap2":
        set_image(image2)
    else:
        set_image(image3)


image0 = load_image("images/swap0.jpg")
image1 = load_image("images/swap1.jpg")
image2 = load_image("images/swap2.jpg")
image3 = load_image("images/swap3.jpg")

g = open('db.txt')
number = g.read()
if number == "swap0":
    set_image(image0)
elif number == "swap1":
    set_image(image1)
elif number == "swap2":
    set_image(image2)
else:
    set_image(image3)

f()

root.mainloop()

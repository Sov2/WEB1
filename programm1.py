from tkinter import *
from telethon import TelegramClient, sync
from tkinter import messagebox

api_id = 24494050
api_hash = '3b7c72fd9585df5100795e67e5772987'
client = TelegramClient('task', api_id, api_hash)
num = 0


def click_button():
    global num
    client.start()
    client.send_message(' @QWERTYWEBBOT', 'swap' + str(num))
    if num < 3:
        num += 1
    else:
        num = 0


root = Tk()
root.title("Кнопка")
root.geometry("300x250")

photo_1 = PhotoImage(file="images/button11.png").subsample(2, 2)

b = Button(root, image=photo_1, cursor="hand2", border="0", command=click_button)
b.place(x=150, y=150, anchor=CENTER)

root.resizable(width=False, height=False)
root.mainloop()

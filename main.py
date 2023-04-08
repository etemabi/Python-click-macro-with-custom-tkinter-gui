import pyautogui
import keyboard
import threading
import customtkinter
import tkinter
from tkinter.ttk import Separator
from tkinter import Button, Tk

#
#değişkenler
#

hiz = None
makrotus = None

#
#pencere
#
customtkinter.set_appearance_mode("Dark")

app = customtkinter.CTk()
app.geometry("400x250")
app.title("sipariş makro")
app.overrideredirect(1)

#
#KOMUTLAR
#
def tiklama():
    while True:
        if keyboard.is_pressed(makrotus): #buraya girdi tuşu girilecek
            pyautogui.rightClick()

def calistir():
    global makrotus
    makrotus = entry.get()
    if __name__ == "__main__":
        for i in range(int(hiz/9)): # buraya tekrar katsayısı girilecek
            threading.Thread(target=tiklama).start()

def slider_event(value):
    global hiz

    value = round(value*100)
    if value == 100:value = 99
    elif value > 88:value = 90
    elif value > 75:value = 81
    elif value > 65:value = 72
    elif value > 58:value = 63
    elif value > 48:value = 54
    elif value > 38:value = 45
    elif value > 32:value = 36
    elif value > 22:value = 27
    elif value > 12:value = 18
    elif value < 12:value = 9

    hiz = value
    hizgosterge.configure(text=value)

#
#ELEMENTLER
#

#title yazısı
customtkinter.CTkLabel(master=app,
                               text="Giga Makro",
                               width=120,
                               height=25,
                               corner_radius=8
                               ).place(
                                        relx=0.1,
                                        rely=0.06,
                                        anchor=tkinter.CENTER
                                        )

#çalıştırma butonu
calistirbutton = customtkinter.CTkButton(master=app,
                                text="Start",
                                width=120,
                                height=32,
                                border_width=0,
                                corner_radius=8,
                                command=calistir
                                )
calistirbutton.place(
                    relx=0.75,
                    rely=0.75,
                    anchor=tkinter.CENTER
                    )

#güzel dursun diye çizgi
separator = Separator(app, orient='horizontal')
separator.place(relwidth=1, rely=0.12)

#tuş entrysi
entry = customtkinter.CTkEntry(master=app,
                                width=80,
                                height=25,
                                corner_radius=5
                               )
entry.place(
            relx=0.2,
            rely=0.3,
            anchor=tkinter.CENTER
            )

#tuş yazısı
customtkinter.CTkLabel(master=app,
                        text="Enter the macro key",
                       width=120,
                       height=25,
                       corner_radius=8
                       ).place(
                                relx=0.2,
                                rely=0.2,
                                anchor=tkinter.CENTER
                                )

#kapatma butonu
Button(master=app,
       border=0,
       text="X",
       font=("Verdana", 12),
       background="#242424",
       foreground="White",
       command=app.destroy
                            ).place(
                                    rely=0,
                                    relx=0.95
                            )


#makro hızı seçme yeri
slider = customtkinter.CTkSlider(master=app,
                                width=120,
                                height=16,
                                border_width=5.5,
                                command=slider_event
                                )
slider.place(
            relx=0.75,
            rely=0.3,
            anchor=tkinter.CENTER
            )

#hız yazısı
customtkinter.CTkLabel(master=app,
                        text="Enter the macro speed",
                       width=120,
                       height=25,
                       corner_radius=8
                       ).place(
                                relx=0.75,
                                rely=0.2,
                                anchor=tkinter.CENTER
                                )

#hız göstergesi
hizgosterge = customtkinter.CTkLabel(master=app,
                        text="",
                       height=25,
                       corner_radius=8
                       )
hizgosterge.place(relx=0.56, rely=0.3, anchor=tkinter.CENTER)


app.mainloop()

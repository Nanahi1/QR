import cv2
from tkinter import *
import qrcode

def clicked():
    filename = txt1
    data = txt
    img = qrcode.make(data)
    img.save(filename)


window = Tk()
window.title("Приложение QR-code")
window.geometry('400x250') 


lbl = Label(window, text='Введите текст')
lbl.place(x=10, y=10)

lbl1 = Label(window, text='Введите название qr-кода')
lbl1.place(x=10, y=45)

lbl2 = Label(window, text='Введите название qr-кода, который хотите посмотреть')
lbl2.place(x=10, y=125)

lbl3 = Label(window, text='Текст qr-кода')
lbl3.place(x=10, y=165)

btn = Button(window, text="Конвертировать",command=clicked)
btn.place(x=60,y=90)

btn1 = Button(window, text="Конвертировать")
btn1.place(x=60,y=210)

txt = Entry(window,width=40)
txt.place(x=10,y=30)

txt1 = Entry(window,width=40)
txt1.place(x=10,y=65)
             
txt2 = Entry(window,width=40)
txt2.place(x=10,y=145)

txt3 = Entry(window,width=40)
txt3.place(x=10,y=185)

window.mainloop() 

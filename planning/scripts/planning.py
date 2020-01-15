#!/usr/bin/env python3
#coding:utf-8
from tkinter import *
from tkinter import messagebox
# splashscreen
def main():
    root = Tk()
    image = PhotoImage(file='/home/streinge/planning/planning/image/photo.png')
    button=Button(root, image=image)
    button.pack()
   
    #Возвращает разрешение экрана по ширине в пикселях.
    ws = root.winfo_screenwidth() 
    #Возвращает разрешение экрана по высоте в пикселях.
    hs = root.winfo_screenheight()
    w = 500 #root.winfo_width()
    h = 300 #root.winfo_height()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    root.overrideredirect(True)
    
    root.after(3000, lambda: root.destroy())
    root.mainloop()
    
    print(w)
    print(h)

   


    # root['bg'] = 'green' изменение фона окна на зеленый
if __name__ == '__main__':
    main()












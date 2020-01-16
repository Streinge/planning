#!/usr/bin/env python3
#coding:utf-8
from tkinter import *
    # функция принимает строку с путем к файлу заставки и  создает заставку к программе
def splashscreen(path_to_image):
    # класс Тк создаетс базовое окно заставки
    splashscreen = Tk()
    # класс PhotoImage позволяет использовать полноцветное изображение
    image = PhotoImage(file=path_to_image)
    # для создания фона с фото используем виджет "Кнопка" без указания размера, поэтому кнопка получилось со все окно и заполнила фон
    button=Button(splashscreen,text='Плани', image=image)
    lab=Label(splashscreen,text='Плани',fg='red',font='arial 14')
    # упаковываем кнопку упаковщиком pack
    button.pack()
    lab.pack()
    #Возвращает разрешение экрана по ширине в пикселях.
    ws = splashscreen.winfo_screenwidth() 
    #Возвращает разрешение экрана по высоте в пикселях.
    hs = splashscreen.winfo_screenheight()
    #Задаем ширину окна заставки
    width = 600
    #Задаем высоту окна заставки
    height = 500
    #Определяем координат для размещения заставки точно по центру экрана
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    #задаем положение и размеры окна заставки
    splashscreen.geometry('%dx%d+%d+%d' % (width, height, x, y))
    #этим методом игнорируем окно заголовка окна, чтобы заставка выглядела, как заставка.
    splashscreen.overrideredirect(True)
    splashscreen.after(3000, lambda: splashscreen.destroy())
    splashscreen.mainloop()



def main():
    splashscreen('/home/streinge/planning/planning/image/photo.png')
if __name__ == '__main__':
    main()

from tkinter import *
from time import sleep
# функция принимает строку с путем к файлу заставки и  создает заставку к программе
def move_char(x, y):
    print("move")
    splashscreen.move(text, x, y)
    main.after(50, move_char(x, y))

def splashscreen(path_to_image):
    # класс Тк создает базовое окно заставки
    main = Tk()
    # создаем холст внутри окна - это и будет заставка
    splashscreen = Canvas(main,height=250, width=300)
    # класс PhotoImage позволяет использовать полноцветное изображение
    filename = PhotoImage(file=path_to_image)
    # рисуем изображение из файла на холсте
    image = splashscreen.create_image(300, 0, anchor=NE, image=filename)
    text = splashscreen.create_text(20 , 150, text = 'П', font = 'Arial 72')
    splashscreen.pack()
    
    main.after(2000, lambda: main.destroy())

    # main.after(500, lambda: splashscreen.delete(text))
    # упаковываем кнопку упаковщиком pack
    move_char(1, 0)
    main.mainloop()


splashscreen('/home/streinge/planning/planning/image/photo.png')
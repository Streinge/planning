from tkinter import *

# функция принимает строку с путем к файлу заставки и  создает заставку к приложению
def move_char():
    global x
    if x <=0:
        return
    else:
        x += 0.1
        splashscreen.move(text, -5, 0)
        main.after(10, lambda: move_char())

def splashscreen(path_to_image):
    global main, splashscreen
    global text, x
    # класс Тк создает базовое окно заставки
    main = Tk()
    #Задаем ширину окна заставки
    width = 700
    #Задаем высоту окна заставки
    height = 467

    # создаем холст внутри окна - это и будет заставка
    splashscreen = Canvas(main,height=height, width=width)
    # класс PhotoImage позволяет использовать полноцветное изображение
    filename = PhotoImage(file=path_to_image)
    # рисуем изображение из файла на холсте, метод create_image принимает координаты точки отсчета для расположения
    # фотографиии - это первые два значения, потом еще разные аргументы но важный это achor - указатель куда 
    # привязать координаты точки отсчета, в моем случае поставил anchor=CENTER, то есть изображение будет центрированно
    # по точке отсчета. Дальше также метод принимает значение метода PhotoImage.
    image = splashscreen.create_image(width / 2, height / 2, anchor=CENTER, image=filename)
    x = 0
    text = splashscreen.create_text(width, 150, text = 'Планирование', anchor=NW,  font = 'Times 72', fill = '#2373d9')

    #Возвращает разрешение экрана по ширине в пикселях.
    ws = main.winfo_screenwidth() 
    #Возвращает разрешение экрана по высоте в пикселях.
    hs = main.winfo_screenheight()
    #Определяем координат для размещения заставки точно по центру экрана
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    #задаем положение и размеры окна заставки
    main.geometry('%dx%d+%d+%d' % (width, height, x, y))
    #этим методом игнорируем окно заголовка окна, чтобы заставка выглядела, как заставка.
    main.overrideredirect(True)
    main.after(5000, lambda: main.destroy())




     # упаковываем кнопку упаковщиком pack
    splashscreen.pack()
    move_char()
    main.mainloop()

splashscreen('/home/streinge/planning/planning/image/photo.png')
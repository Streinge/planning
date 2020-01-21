from tkinter import *


# функция принимает строку с путем к файлу заставки и  создает заставку к приложению
def move_char(text, x, left_margin):
    if x <=left_margin:
        return
    else:
        splashscreen.move(text, -10, 0)
        splashscreen.move(text, -5, 0)
        splashscreen.move(text, -5, 0)
        main.after(10, lambda: move_char(text, x-10, left_margin))

        

def splashscreen(path_to_image):
    global main, splashscreen
    global text1, text2, text3, width, height
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
    
    text1 = splashscreen.create_text(width, 100, text = 'Планирование', anchor=NW,  font = ('Times', 72, 'bold'), fill = 'black')
    text2 = splashscreen.create_text(width, 200, text = 'швейного', anchor=NW,  font = ('Times', 72, 'bold'), fill = 'black')
    text3 = splashscreen.create_text(width, 300, text = 'производства', anchor=NW,  font = ('Times', 72, 'bold'), fill = 'black')
    diapason = 0
    

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
    move_char(text1,width, 30)
    main.after(1000, lambda: move_char(text2, width, 130))
    main.after(2500, lambda: move_char(text3, width, 50))
    
    main.mainloop()

splashscreen('/home/streinge/planning/planning/image/photo.png')
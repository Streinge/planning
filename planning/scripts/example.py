from tkinter import *
from subprocess import run
import subprocess
# функция принимает виджет create_text.сanvas, начальную координату 
# по оси х,и значение левого отступа и перемещает слово до отступа 
# справа налево по холсту


def move_text(user_text, x, left_margin):
    # дельта перемещения (скорость) по оси х
    delta_x = 5
    # терминальное условие, чтобы слово смещалось только до левого отступа
    if x <= left_margin:
        return
    else:
        # пермещение виджет с помощью метода canvas.move
        splashscreen.move(user_text, -delta_x, 0)
        # рекурсивный вызов с задержкой (методом tk.after - 10-задержка)
        main.after(10, lambda: move_text(user_text, x - delta_x, left_margin))

# функция принимает начальные координаты виджета текст.канвас, строку текста,
# значение начала отсчета anchor=NW - это верхний левый угол, шрифт, и цвет шрифта
# возвращает виджет текст.канвас 
def text_creator(x0, y0, user_text, user_anchor, user_font, user_text_color):
    return splashscreen.create_text(x0, y0, text=user_text, anchor=user_anchor,  font=user_font, fill=user_text_color)
# функция принимает на вход значение инкремента и при каждом рекурсивном вызове
# вызове функции выводит строку текста с новым текстом из списка цветов
# терминальное условие - если список закончился, то выход
def changing_color(i):
    if i > len(colors_list) - 1:
        return
    else:
        #создание виджета текст.канвас с новым цветом 
        splashscreen.create_text(width / 2, height - 30, text='Разработано для личного использования', anchor=S,  font=('Times', 20), fill=colors_list[i])
        main.after(150, lambda: changing_color(i+1))



"""p = subprocess.Popen(['/mnt/c/Xming/Xming.exe', '-multiwindow', '-clipboard'])
code = p.wait()
print(code)"""

main = Tk()
width = 600
height = 320
splashscreen = Canvas(main, height=height, width=width, background='#f5f4f4')
filename = PhotoImage(file='/home/streinge/planning/planning/image/planning1.png')
image = splashscreen.create_image(20, 30, anchor=NW, image=filename)
line = splashscreen.create_line(10, 240, 590, 240, width = 2, fill = '#c4c3c2')
splashscreen.pack()
text_color = '#c4c3c2'
text_font = ('Times', 36)
text_anchor = NW
text1 = text_creator(width, 35, 'Планирование', text_anchor, text_font, text_color)
text2 = text_creator(width, 95, 'Швейного', text_anchor, text_font, text_color)
text3 = text_creator(width, 155, 'Производства', text_anchor, text_font, text_color)
# задаю список цветов градации серого от светло-серого, до черного.
colors_list = [
              '#f7f7f8', '#ededed', '#e3e3e3', '#d9d9d9', '#cfcfcf', '#c4c4c4', '#bababa', 
              '#b0b0b0', '#a6a6a6', '#9c9c9c', '#919191', '#878787', '#7d7d7d', '#737373', 
              '#696969', '#5e5e5e', '#545454', '#4a4a4a', '#404040', '#363636', '#2b2b2b',
              '#212121','#171717','#0d0d0d','#030303'
              ]
ws = main.winfo_screenwidth()
hs = main.winfo_screenheight()
x = (ws/2) - (width/2)
y = (hs/2) - (height/2)
main.geometry('%dx%d+%d+%d' % (width, height, x, y))
main.configure(borderwidth=1)
main.overrideredirect(True)
main.after(10000, lambda: main.destroy())
move_text(text1, width, 260)
main.after(1000, lambda: move_text(text2, width, 260))
main.after(2000, lambda: move_text(text3, width, 260))
main.after(3000, lambda: changing_color(0))

main.mainloop()

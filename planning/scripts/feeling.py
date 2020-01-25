# функция для заставки, которая заполняет окно мелкими кругами
# работать не будет потому что не заданы main  это ТК, и splashscreen это Canvas.
from random import *
def filling(diapason, i):
    if i == diapason:
        return
    else:
        x0 = randint(0, width)
        y0 = randint(0, height)
        splashscreen.create_oval(x0, y0, x0+20, y0+20, fill='grey', outline='grey')
        main.after(1, lambda: filling(diapason, i+1))
    

filling(20000, 0)
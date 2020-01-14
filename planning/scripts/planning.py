#!/usr/bin/env python3
#coding:utf-8
from tkinter import *
from tkinter import messagebox

def main():
    root = Tk()
    """c = Canvas(root, width=200, height=200, bg='white')
    c.pack()
 
    c.create_line(10, 10, 190, 50)
 
    c.create_line(100, 180, 100, 60, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")"""
    root.geometry('500x350+300+200')
    root['bg'] = 'green'
    root.overrideredirect(True)
    #Label(a, text="About this").pack(expand=1)
    root.after(3000, lambda: root.destroy())
    root.mainloop()
   



if __name__ == '__main__':
    main()












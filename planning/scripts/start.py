from tkinter import *

def leftclick(event):
    print ('Вы нажали левую кнопку мыши')
def rightclick(event):
    print ('Вы нажали правую кнопку мыши')
def destroy(event):
    root.destroy()
root=Tk()

canv = Canvas(root, height=300, width=300, background='red')
root.geometry("300x300+250+250")
canv.focus()
root.bind('<Key>', destroy)
canv.pack()
canv.grab_set()

root.mainloop()                                                     
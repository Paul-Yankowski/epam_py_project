from tkinter import *
from tkinter.ttk import Treeview
from bin import parser
from sqlite import sqlite_db

window = Tk()
window.geometry('800x600')
txt = Entry(window,width=20)
txt.grid(column=1, row=0)
tree = Treeview(window, selectmode='browse')


def load_into_db():
    res = f'{txt.get()}'
    sqlite_db.write_db(res,res,parser.parse(res))
    #parser.parse(res)

def load_from_db():
    for row in sqlite_db.read_db():
        tree.insert("",'end',text=row)

def wind():
    btn = Button(window, text="Загрузить в бд", command=load_into_db)
    btn.grid(column=2, row=0)
    btn1 = Button(window, text="Загрузить from бд", command=load_from_db)
    btn1.grid(column=2, row=0)
    tree.place(x=100, y=200, width=550, height=200)
    scroll = Scrollbar(window, orient="vertical", command=tree.yview)
    scroll.place(x=650, y=200, height=200)
    tree.configure(yscrollcommand=scroll.set)
    tree.insert("",'end',text="1")
    txt.place(x=200, y=100,width=350,height=30)
    btn.place(x=450,y=500)
    btn1.place(x=150, y=500)
    window.mainloop()

wind()

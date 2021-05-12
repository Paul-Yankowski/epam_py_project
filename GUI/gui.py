from tkinter import *
from tkinter.ttk import Treeview
from bin.parser import Parser
from sqlite.sqlite_db import Database


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x600')
        self.txt = Entry(self.window,width=20)
        self.txt.grid(column=1, row=0)
        self.tree = Treeview(self.window, selectmode='browse')
        self.db = Database()


    def load_into_db(self):
        res = f'{self.txt.get()}'
        print(res)
        self.db.write_db(Parser(res))

    def load_from_db(self):
        for row in self.db.read_db():
            self.tree.insert("",'end',text=row)

    def wind(self):
        btn = Button(self.window, text="Загрузить в бд", command=self.load_into_db)
        btn.grid(column=2, row=0)
        btn1 = Button(self.window, text="Загрузить from бд", command=self.load_from_db)
        btn1.grid(column=2, row=0)
        self.tree.place(x=100, y=200, width=550, height=200)
        scroll = Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        scroll.place(x=650, y=200, height=200)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.insert("",'end',text="1")
        self.txt.place(x=200, y=100,width=350,height=30)
        btn.place(x=450,y=500)
        btn1.place(x=150, y=500)
        self.window.mainloop()


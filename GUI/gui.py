from tkinter import *
from tkinter import messagebox
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
        self.lbl_url = Label(self.window, text="Введите URL")
        self.lbl_tab= Label(self.window, text="Данные из базы")

    def load_into_db(self):
        res = f'{self.txt.get()}'
        self.db.write_db(Parser(res))
        messagebox.showinfo('TAGS', str(Parser(res).tags()))

    def load_from_db(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.db.read_db():
            self.tree.insert("",'end',text=row)

    def wind(self):
        self.lbl_url.place(x=375,y=15)
        self.lbl_tab.place(x=360,y=120)
        btn = Button(self.window, text="Загрузить в базу", command=self.load_into_db)
        btn.grid(column=2, row=0)
        btn1 = Button(self.window, text="Показать из базы", command=self.load_from_db)
        btn1.grid(column=2, row=0)
        self.tree.place(x=25, y=150, width=750, height=300)
        scroll = Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        scroll.place(x=775, y=200, height=150)
        self.tree.configure(yscrollcommand=scroll.set)
        self.txt.place(x=150, y=50,width=500,height=35)
        btn.place(x=450,y=500)
        btn1.place(x=150, y=500)
        self.window.mainloop()


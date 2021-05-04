from tkinter import *
from tkinter.ttk import Treeview

window = Tk()
window.geometry('800x600')
txt = Entry(window,width=20)
txt.grid(column=1, row=0)



def click():
    res = f'{txt.get()}'
    print(res)

def wind():
    btn = Button(window, text="Загрузить в бд!", command=click)
    btn.grid(column=2, row=0)
    tree = Treeview(window, selectmode='browse')
    tree.place(x=100, y=200, width=550, height=200)
    scroll = Scrollbar(window, orient="vertical", command=tree.yview)
    scroll.place(x=650, y=200, height=200)
    tree.configure(yscrollcommand=scroll.set)
    tree.insert("",'end',text="1")
    txt.place(x=200, y=100,width=350,height=30)
    btn.place(x=450,y=500)
    window.mainloop()

wind()

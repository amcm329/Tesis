"""
from Tkinter import ttk

master = tkinter.Tk()

notebook = ttk.Notebook(master)
notebook.pack(fill='both', expand='yes')
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='Uno')
notebook.add(frame2, text='Dos')


master.geometry('200x200')
master.mainloop()
"""

from Tkinter import *
from ttk import *

root = Tk()
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
Button(tab1, text='Exit', command=root.destroy).pack(padx=300, pady=300)

note.add(tab1, text = "Tab One")
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.pack()
root.mainloop()
exit()

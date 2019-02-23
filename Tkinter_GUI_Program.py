from tkinter import*
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()


frame1 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One')
text1 =Text(frame1, width = 40, height = 10)
text1.pack()
text1.config(wrap = 'word')

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text = 'Two')
text2 =Text(frame2, width = 40, height = 10)
text2.pack()
text2.config(wrap = 'word')
ttk.Button(frame2, text = 'Click me').pack()

frame3 = ttk.Frame(notebook)
notebook.add(frame3, text = 'Three')
text3 =Text(frame3, width = 40, height = 10)
text3.pack()
text3.config(wrap = 'word')
ttk.Button(frame3, text = 'Click me').pack()





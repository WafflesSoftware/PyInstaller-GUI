from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import os
import sys


def compiling():
    os.chdir(os.path.dirname(file))
    os.system(f"pyinstaller -F {file.split('/')[-1]}")


file = filedialog.askopenfilename(title="Open file")

root = Tk()
root.geometry("400x100")
root.title("PyToExe")

lbl_1 = ttk.Label(root, text="Path to compile:")
lbl_1.place(x=0, y=0)

l_box_path = Listbox(root, width=70, height=1)
l_box_path.place(x=0, y=20)

path_list = [file]

for item in path_list:
    l_box_path.insert(END, item)

btn_compile = ttk.Button(root, text="COMPILE", width=65, command=compiling)
btn_compile.place(x=0, y=50)

btn_quit = ttk.Button(root, text="Quit", width=65, command=lambda: sys.exit())
btn_quit.place(x=0, y=75)

root.mainloop()

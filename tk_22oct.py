"""
import tkinter as tk
root = tk.Tk()
root.title("Form")
tk.Label(root, text="Name").pack()
tk.Entry(root).pack()
tk.Label(root, text="Subject").pack()
tk.Checkbutton(root, text="Python").pack()
tk.Checkbutton(root, text="Java").pack()
tk.Checkbutton(root, text="C++").pack()
tk.Button(root, text="Submit").pack()
root.mainloop()
"""

import tkinter as tk
root = tk.Tk()
root.title("Form")
tk.Label(root, text="Name").pack()
tk.Entry(root).pack()
tk.Label(root, text="Roll Number").pack()
tk.Entry(root).pack()
tk.Label(root, text="Branch").pack()
tk.Entry(root).pack()
tk.Label(root, text="Semester").pack()
tk.Entry(root).pack()
tk.Button(root, text="Submit").pack()
root.mainloop()

import tkinter as tk
from tkinter import ttk

from tkinter import font as tkfont
from PIL import Image, ImageTk

def Window(): 
    root = tk.Tk()
    return root

def Title(root, title = "New Window"):
    a = root.title(title)
    return a

def Label(parent, text="Default Text", font="Helvetica", size=12, color="black"):
    label = ttk.Label(parent, text=text,  font = (font, size), foreground = color); label.pack(); 
    return label

def Place(widget, x, y):
    widget.place(x=x, y=y)

def Font(name = 'arial', size = 20, weight = 10):
    font = tkfont.Font(family=name, size=size, weight=weight)
    return font


def BGImage(parent, bg_image_path = '', width=400 , height=300):
    # Load and set the background image
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    background_label = tk.Label(parent, image=bg_photo)
    background_label.image = bg_photo  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

def Button(parent, text="Button", command=None, font="Helvetica", size=12, bg="black", fg="black", width=20, height=20, padx = 10, pady = 10):
    button = tk.Button(parent, text=text, command=command, font=(font, size), bg=bg, fg=fg, width=width, height=height)
    button.pack(padx=padx, pady=pady)
    return button

def Entry(parent, width=20, font="Helvetica", size=12, bg="white", fg="black", padx = 10, pady = 10):
    entry = ttk.Entry(parent, width=width, font=(font, size), background=bg, foreground=fg)
    entry.pack(padx=padx, pady=pady)
    return entry

def GetEntry(entry):
    d = entry.get()
    return entry 

def Run(window):
    window.mainloop()
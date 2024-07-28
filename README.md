# FunctionGUI

FunctionGUI is a simple GUI library built using tkinter, designed to help you quickly create graphical user interfaces with ease.

## Installation

To install FunctionGUI, you can simply use pip:

```bash
pip install functiongui
```

```python
# FunctionGUI

FunctionGUI is a simple GUI library built using tkinter, designed to help you quickly create graphical user interfaces with ease. This library can currently complete the most basic tasks of Tkinter and does not contain much functionality, but will have more features in the future. 

## Installation

To install FunctionGUI, you can simply use pip:

```bash
pip install functiongui
```
## Usage
```python
import functiongui as fg

# Create a window
root = fg.Window()

# Set the title of the window
fg.Title(root, "New Window")

# Create a custom font
custom_font = fg.Font(name='Helvetica', size=16, weight='bold')

# Create a label with the custom font
label = fg.Label(root, text="Hello, World!", font='Helvetica', size=16, color="blue")


# Add/pack a widget
fg.add(widget, padx = 10, pady = 10)

# Create and p
ChexBox(parent, text = 'check me', variable=None, command =lambda: print("Check Box")):


# Create an entry field
entry = fg.Entry(root, width=20, font="Helvetica", size=12, bg="white", fg="black", padx = 10, pady = 10)

# Retrieve and print the text from the entry field on button click
def on_button_click():
    text = fg.GetEntry(entry)
    print(text.get())

# Change the design of the app
style = fg.Design(theme)

# Boolean Variable (Use in checkboxes)
Boolean_Variable = BulleanVar()

# Add a Button 
button = fg.Button(root, text="Print Entry", command=on_button_click)

# Set a background image
fg.BGImage(root, bg_image_path='path_to_image.jpg', width = 300, height = 600)

# Place a widget on a specific coordinate on the window
Place(button, 60, 100)

# Run the main loop
fg.Run(root)
```

## Bugs

If you are finding bugs in the code, please report them to me @aaroh.charne@gmail.com.
Please include a snippet of your code as well the problem. Thank You

## Please check out my other Library Calclab @https://pypi.org/project/Calclab/
```

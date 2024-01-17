import tkinter as tk

root = tk.Tk() #Initialise the GUI.

root.geometry("800x500") #Set the size of the window.
root.title("Testing GUI") #Sets title for window.

'''
The first parameter in .Label() is the parent node onto which the label which be displayed.
The next is the conent of this label (there are many different types to choose from).
Pack is a geometry manager that organises widgets in blocks before placing them in the parent widget.
You can add padding to pack with padx = $ and pady = $.
'''
label = tk.Label(root, text="Hello world", font=('Arial', 18))
label.pack(padx = 20, pady = 20)

#Textbox allows a user to type into a box.
textbox = tk.Text(root, height = 3 ,font=('Arial', 16))
textbox.pack(padx = 10)


root.mainloop() #Start the window.
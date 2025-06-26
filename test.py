import tkinter as tk

def say_hello():
    print("You clicked the button!")

root = tk.Tk()
button = tk.Button(root, text="Click me!", command=say_hello)
button.pack()

root.mainloop()

say_hello()
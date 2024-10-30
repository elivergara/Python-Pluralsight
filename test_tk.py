# import tkinter as tk
# root = tk.Tk()
# root.geometry("1280x720")
# root.title("My best Recipes!!")
# label = tk.Label(root, text="My label, how'bout that?")
# label.pack()




# tk.mainloop()

import tkinter as tk

# Create a root window
root = tk.Tk()

# Button without rowspan, in row 0, column 0
button1 = tk.Button(root, text="Button 1")
button1.grid(row=0, column=0)

# Button with rowspan, in row 0, column 1
button2 = tk.Button(root, text="Button 2 (rowspan=2)")
button2.grid(row=0, column=1, rowspan=2)

# Another button below button1 in row 1, column 0
button3 = tk.Button(root, text="Button 3")
button3.grid(row=1, column=0)

# Run the main event loop
root.mainloop()

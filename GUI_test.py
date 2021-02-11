import tkinter as tk

root = tk.Tk()

## container
HEIGHT = 700
WIDTH = 800
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

## frame
frame = tk.Frame(root, bg="#80c1ff")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


## button
button = tk.Button(frame, text="test button", activebackground="#000000", bg="gray")
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
# button.grid(row=0, column=0)
# button.pack(fill="both", side="left")

## label
label = tk.Label(frame, text="This is a label", bg="yellow")
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)
# label.grid(row=0, column=1)
# label.pack()

entry = tk.Entry(frame, bg="green")
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.25)
# entry.grid(row=0, column=2)
# entry.pack()

root.mainloop()
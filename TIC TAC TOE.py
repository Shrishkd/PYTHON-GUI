from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("TIC TAC TOE")

#Game Name: TIC TACT TOE

frame1 = Frame(root)
frame1.pack()
titlelabel1 = Label(frame1, text="Tic Tac Toe", font=("Comic sans ms", 30), bg="red")
titlelabel1.pack()

#GAME BOARD

turn ="x"

def play(event):
    global turn
    button = event.widget

    if turn== "x":
        button["text"] = "X"
        turn = "o"
    else:
        button["text"] ="O"
        turn = "x"
frame2 = Frame(root)
frame2.pack()

#First Row

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 0, column=0)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 0, column=1)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 0, column=2)
button.bind("<Button-1>", play)

#Second Row

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 1, column=0)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 1, column=1)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 1, column=2)
button.bind("<Button-1>", play)

#Third Row


button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 3, column=0)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 3, column=1)
button.bind("<Button-1>", play)

button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg ="yellow", relief=RAISED, borderwidth=5)
button.grid(row = 3, column=2)
button.bind("<Button-1>", play)

root.mainloop()
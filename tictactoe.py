from tkinter import messagebox
from tkinter import * 

root = Tk()
root.title("Tic Tac Toe Game")

menu = Menu(root)
item_game = Menu(menu)

item_game.add_command(label='New Game')
item_game.add_command(label='Surrender')

turn = True
count = 0

def reset_game():
    global count 
    count = 0
    b1.config(state=ACTIVE, text=" ")
    b2.config(state=ACTIVE, text=" ")
    b3.config(state=ACTIVE, text=" ")
    b4.config(state=ACTIVE, text=" ")
    b5.config(state=ACTIVE, text=" ")
    b6.config(state=ACTIVE, text=" ")
    b7.config(state=ACTIVE, text=" ")
    b8.config(state=ACTIVE, text=" ")
    b9.config(state=ACTIVE, text=" ")

item_game.add_command(label='Reset', command=reset_game)

def close_game():
    root.destroy()

item_game.add_command(label='Close Game', command= close_game)
menu.add_cascade(label='Game', menu = item_game)

root.config(menu = menu)

# True = X's turn, False = O's Turn


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def check_if_win():
    global winner
    winner = False
    if b1["text"] == b2["text"] == b3["text"] and b1["text"] != " ":
        messagebox.showinfo("Game Over", b1["text"] + " wins!!")
        disable_all_buttons()
    elif b1["text"] == b4["text"] == b7["text"] and b1["text"] != " ":
        messagebox.showinfo("Game Over", b1["text"] + " wins!!")
        disable_all_buttons()
    elif b1["text"] == b5["text"] == b9["text"] and b1["text"] != " ":
        messagebox.showinfo("Game Over", b1["text"] + " wins!!")
        disable_all_buttons()
    elif b4["text"] == b5["text"] == b6["text"] and b4["text"] != " ":
        messagebox.showinfo("Game Over", b4["text"] + " wins!!")
        disable_all_buttons()
    elif b2["text"] == b5["text"] == b8["text"] and b2["text"] != " ":
        messagebox.showinfo("Game Over", b2["text"] + " wins!!")
        disable_all_buttons()
    elif b7["text"] == b8["text"] == b9["text"] and b7["text"] != " ":
        messagebox.showinfo("Game Over", b7["text"] + " wins!!")
        disable_all_buttons()
    elif b3["text"] == b6["text"] == b9["text"] and b3["text"] != " ":
        messagebox.showinfo("Game Over", b3["text"] + " wins!!")
        disable_all_buttons()
    elif b3["text"] == b5["text"] == b7["text"] and b3["text"] != " ":
        messagebox.showinfo("Game Over", b3["text"] + " wins!!")
        disable_all_buttons()
    elif count == 9:
        messagebox.showinfo("Game Over", "Its a TIE!")

def make_move():
    pass

def button_clicked(b):
    global turn, count

    if b["text"] == " " and turn == True:
        b["text"] = "X"
        turn = False
        count += 1
        check_if_win()
    
    elif b["text"] == " " and turn == False:
        b["text"] = "O"
        turn = True
        count += 1
        check_if_win()
    
    else: 
        messagebox.showerror("Error!", "Invalid move\n Make another move...")

b1 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey" , command=lambda: button_clicked(b1))
b2 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b2))
b3 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b3))
b4 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b4))
b5 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b5))
b6 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b6))
b7 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b7))
b8 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b8))
b9 = Button(root, text=' ', font=('Helvetica', 20), height=3, width=6, bg="grey", command=lambda: button_clicked(b9))

b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=2, row=0)
b4.grid(column=0, row=1)
b5.grid(column=1, row=1)
b6.grid(column=2, row=1)
b7.grid(column=0, row=2)
b8.grid(column=1, row=2)
b9.grid(column=2, row=2)



root.mainloop()
from msvcrt import kbhit
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import BOLD
from random import randint
from tkinter import BOTTOM, LEFT, RIGHT, messagebox

#Set root window
root = tk.Tk()
root.title("GuessNumber")
root.geometry("500x500")
root.resizable(False,False)
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
favicon = ImageTk.PhotoImage(Image.open("img/favicon.png"))
root.iconphoto(False, favicon)
#Create variables
score = 0
k = 0
computer_number = randint(0,5)

#Create Functions

def switch_page(page):
    global player_nickname
    player_nickname = entry_nickname.get()
    if len(player_nickname) > 3:
        page.tkraise()
    else:
        wrong_nickname = tk.Label(start_page, text = "You entered the wrong nickname!More than 3 characters!", fg = "darkred", bg = "#05051e", font = ('Helvetica', 12, BOLD))
        wrong_nickname.pack(pady = 10, padx = 5)
        wrong_nickname.after(2000, lambda:wrong_nickname.pack_forget())
            
   
def guess():
    global computer_number
    global score
    player_number = int(entry_number.get())
    
    if computer_number == player_number:
        score += 20
        switch_page(last_page)
    else:
        wrong_number = tk.Label(main_page, text = "Whops!You entered the wrong number, try again![-5 score]", bg = "#05051e", fg = "darkred", font = ('Helvetica', 12, BOLD))
        wrong_number.pack(pady = 20, padx = 5)
        wrong_number.after(2000, lambda:wrong_number.pack_forget())
        score -= 5
        
def continue_playing():
    global computer_number
    entry_number.delete(0)
    switch_page(main_page)
    computer_number = randint(0,5)
    

def write_db():
    with open("data/DataBase.txt", "a") as f:
        f.write(f"{player_nickname} {score}\n")
        f.close()

def on_closing():
    if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?Progress will not be saved"):
            root.destroy()

#Pages Setup
start_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
main_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
diff_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
last_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
start_page.grid(row = 0, column = 0 , sticky = "nsew")
main_page.grid(row = 0, column = 0 , sticky = "nsew")
diff_page.grid(row = 0, column = 0 , sticky = "nsew")
last_page.grid(row = 0, column = 0 , sticky = "nsew")
root.protocol("WM_DELETE_WINDOW", lambda:on_closing())
start_page.tkraise()

# Start Page Setup
label_welcome = tk.Label(start_page, text = "Welcome to GuessNumber", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
frame_logo = tk.Frame(start_page, width = 250, height = 250)
central_logo = ImageTk.PhotoImage(Image.open("img/central_logo.png"))
start_logo = tk.Label(frame_logo, image = central_logo, bg = "#05051e")
frame_logo.pack()
start_logo.pack(fill = "both", expand = "yes")
label_nickname = tk.Label(start_page, text = "Please enter your nickname below:", font = ('Helvetica', 12, BOLD), bg = "#05051e", fg = "#a2a6c6")
label_nickname.pack(padx = 10, pady = (20, 5))
entry_nickname = tk.Entry(start_page, font = ('Helvetica', 12, BOLD), bd = 1)
entry_nickname.pack(padx = 10, pady = 5)
button_nickname = tk.Button(start_page, width = 20, text = "Play", cursor = "hand2", font = ('Helvetica', 12, BOLD), bg = "#01011a", fg = "white", command = lambda:switch_page(main_page), bd = 1, activeforeground = "#a2a6c6")
button_nickname.pack(padx = 10, pady = 5)

#Main Page Setup

label_welcome = tk.Label(main_page, text = "Welcome to GuessNumber", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
frame2_logo = tk.Frame(main_page, width = 250, height = 250)
frame2_logo.pack()
main_logo = tk.Label(frame2_logo, image = central_logo, bg = "#05051e")
main_logo.pack(fill = "both", expand = "yes")
label_guess = tk.Label(main_page, text = "Enter the number you are thinking of below", font = ('Helvetica', 12, BOLD), bg = "#05051e", fg = "#a2a6c6")
label_guess.pack()
entry_number = tk.Entry(main_page, width = 10, font = ('Helvetica', 12, BOLD), bd = 1)
entry_number.pack(padx = 10, pady = 5)
button_guess = tk.Button(main_page, text = "Guess", font = ('Helvetica', 12, BOLD), cursor = "hand2", width = 20,bg = "#01011a", fg = "white", command = lambda:guess(), bd = 1, activeforeground = "#a2a6c6")
button_guess.pack(padx = 10, pady = 10)

#Difficulty Page Setup


#Last Page Setup
frame_winlogo = tk.Frame(last_page, width = 300, height = 300)
frame_winlogo.pack(pady = 40)
crown_logo = ImageTk.PhotoImage(Image.open("img/crown_logo.png"))
win_logo = tk.Label(frame_winlogo, image = crown_logo, bg = "#05051e")
win_logo.pack(fill = "both", expand = "yes")
button_continue = tk.Button(last_page, width = 20, text = "Continue", command = lambda:continue_playing(), cursor = "hand2",font = ('Helvetica', 14, BOLD), bd = 1, bg = "#00b359", fg = "white")
button_continue.pack(padx = 10, pady = (40,0))
button_quit = tk.Button(last_page, width = 20, text = "Quit", command = lambda:[write_db(),root.destroy()], cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 1, bg = "#b30047", fg = "white")
button_quit.pack(padx = 10) 


#Run Window
root.mainloop()
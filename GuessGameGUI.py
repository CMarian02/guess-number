from ast import Pass
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import BOLD
from random import randint


#Set root window
root = tk.Tk()
root.title("GuessNumber")
root.geometry("500x500")
root.resizable(False,False)
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

#Create variables
score = 0
computer_number = randint(0,5)

#Create Functions

def switch_page(page):
    global player_nickname
    player_nickname = entry_nickname.get()
    if len(player_nickname) > 3:
        page.tkraise()
    else:
        wrong_nickname = tk.Label(start_page, text = "You enter a wrong nickname, you must have 3+ charachters!", fg = "darkred", bg = "#004d99", font = ('Arial', 12, BOLD))
        wrong_nickname.pack(padx = 10, pady = 10)
   
def guess():
    global computer_number
    global score
    global wrong_number
    player_number = int(entry_number.get())
    
    if computer_number == player_number:
        score += 20
        switch_page(last_page)
    else:
        wrong_number = tk.Label(main_page, text = "Whops! You enter wrong number! (Your score decrese with 5)", bg = "#004d99", fg = "darkred", font = ('Arial', 12, BOLD))
        wrong_number.pack(padx = 10, pady = 10)
        score -= 5
        
def continue_playing():
    global computer_number
    wrong_number.pack_forget()
    entry_number.delete(0)
    switch_page(main_page)
    computer_number = randint(0,5)

def write_db():
    with open("data/DataBase.txt", "a") as f:
        f.write(f"{player_nickname} {score}\n")
        f.close()

#Pages Setup
start_page = tk.Frame(root, height = 500, width = 500, bg = "#004d99")
main_page = tk.Frame(root, height = 500, width = 500, bg = "#004d99")
last_page = tk.Frame(root, height = 500, width = 500, bg = "#004d99")
start_page.grid(row = 0, column = 0 , sticky = "nsew")
main_page.grid(row = 0, column = 0 , sticky = "nsew")
last_page.grid(row = 0, column = 0 , sticky = "nsew")
start_page.tkraise()
# Start Page Setup
label_welcome = tk.Label(start_page, text = "Welcome to GuessNumber", bg = "#004d99", fg = "#b3b3ff", font = ('Arial', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
frame_logo = tk.Frame(start_page, width = 250, height = 250)
central_logo = ImageTk.PhotoImage(Image.open("img/central_logo.png"))
start_logo = tk.Label(frame_logo, image = central_logo, bg = "#004d99")
frame_logo.pack()
start_logo.pack(fill = "both", expand = "yes")
label_nickname = tk.Label(start_page, text = "Please insert your nickname bellow:", font = ('Arial', 12, BOLD), bg = "#004d99")
label_nickname.pack(padx = 10, pady = (20, 5))
entry_nickname = tk.Entry(start_page, font = ('Arial', 12, BOLD), bd = 1)
entry_nickname.pack(padx = 10, pady = 5)
button_nickname = tk.Button(start_page, width = 20, text = "Play", cursor = "hand2", font = ('Arial', 12, BOLD), bg = "#4747d1", fg = "white", command = lambda:switch_page(main_page))
button_nickname.pack(padx = 10, pady = 5)


#Main Page Setup

label_welcome = tk.Label(main_page, text = "Welcome to GuessNumber", bg = "#004d99", fg = "#b3b3ff", font = ('Arial', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
frame2_logo = tk.Frame(main_page, width = 250, height = 250)
frame2_logo.pack()
main_logo = tk.Label(frame2_logo, image = central_logo, bg = "#004d99")
main_logo.pack(fill = "both", expand = "yes")
label_guess = tk.Label(main_page, text = "Insert your number bellow:", font = ('Arial', 12, BOLD), bg = "#004d99")
label_guess.pack()
entry_number = tk.Entry(main_page, width = 10, font = ('Arial', 12, BOLD), bd = 1)
entry_number.pack(padx = 10, pady = 5)
button_guess = tk.Button(main_page, text = "Guess", font = ('Arial', 12, BOLD), cursor = "hand2", width = 20,bg = "#4747d1", fg = "white", command = lambda:guess())
button_guess.pack(padx = 10, pady = 5)

#Last Page Setup
frame_winlogo = tk.Frame(last_page, width = 300, height = 300)
frame_winlogo.pack(pady = 40)
crown_logo = ImageTk.PhotoImage(Image.open("img/crown_logo.png"))
win_logo = tk.Label(frame_winlogo, image = crown_logo, bg = "#004d99")
win_logo.pack(fill = "both", expand = "yes")
button_continue = tk.Button(last_page, width = 20, text = "Continue", command = lambda:continue_playing(), font = ('Arial', 14, BOLD), bd = 1, bg = "#00b359", fg = "white")
button_continue.pack(padx = 10, pady = (40,0))
button_quit = tk.Button(last_page, width = 20, text = "Quit", command = lambda:[write_db(),root.destroy()], font = ('Arial', 14, BOLD), bd = 1, bg = "#b30047", fg = "white")
button_quit.pack(padx = 10) 


#Run Window
root.mainloop()
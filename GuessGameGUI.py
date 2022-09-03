import sqlite3
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import BOLD
from random import randint
from tkinter import END, messagebox

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
difficulty = 0

#Create Functions
def randing_number(start, stop):
    global computer_number
    global validstop
    global validstart
    validstart = start
    validstop = stop
    computer_number = randint(start, stop)

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
    print(computer_number)
    def diff_settings(add,delete):
        global score
        global label_lscore
        if computer_number == player_number:
            score += add
            label_lscore = tk.Label(frame_winlogo, width = 40, text = "Your  score: " + str(score), bg = "#05051e", fg = "white", font = ('Helvetica', 12, BOLD))
            label_lscore.pack()
            root.unbind('<Return>')
            switch_page(last_page)
        else:
            score -= delete
            wrong_number = tk.Label(main_page, text = "Whops!You entered the wrong number, try again!", bg = "#05051e", fg = "darkred", font = ('Helvetica', 12, BOLD))
            wrong_number.pack(pady = (10,5), padx = 10)
            wrong_number.after(1500, lambda:wrong_number.pack_forget())
            label_score = tk.Label(main_page, text = "Actual score:" + str(score), font = ('Helvetica', 10, BOLD), fg = "#a2a6c6", bg ="#05051e")
            label_score.pack(padx = 10)
            label_score.after(1500, lambda:label_score.pack_forget())
    if difficulty == 0:
        diff_settings(20,5)
    elif difficulty == 1:
        diff_settings(100,20)
    elif difficulty == 2:
        diff_settings(300,11)
    elif difficulty == 3:
        diff_settings(scoreadd, scoredelete)

def continue_playing():
    global computer_number
    label_lscore.pack_forget()
    entry_number.delete(0, END)
    root.bind('<Return>', validating)
    switch_page(main_page)
    if difficulty == 0:
        randing_number(0,5)
    elif difficulty == 1:
        randing_number(0,50)
    elif difficulty == 2:
        randing_number(0,100)
    elif difficulty == 3:
        randing_number(startpool, stoppool)

def write_db():
    connection = sqlite3.connect('data/players.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS rankings
                        (nickname text, score integer)''')
    cursor.execute("INSERT INTO rankings (nickname, score) VALUES (?,?)", (player_nickname, score))
    connection.commit()
    connection.close()

def on_closing():
    if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?Progress will not be saved"):
            root.destroy()

def change_easy():
    global difficulty
    root.bind('<Return>', validating)
    switch_page(main_page)
    messagebox.showinfo("Easy Difficulty", "Pool number: 0 - 5\nWhen you win +20 score\nWhen you lose -5 score!")
    difficulty = 0   
    randing_number(0,5)

def change_medium():
    global difficulty
    root.bind('<Return>', validating)
    switch_page(main_page)
    messagebox.showinfo("Easy Difficulty", "Pool number: 0 - 50\nWhen you win +100 score\nWhen you lose -20 score!")
    difficulty = 1
    randing_number(0,50)
    
def change_hard():
    global difficulty
    root.bind('<Return>', validating)
    switch_page(main_page)
    messagebox.showinfo("Easy Difficulty", "Pool number: 0 - 100\nWhen you win +300 score\nWhen you lose -11 score!")
    difficulty = 2
    randing_number(0,100)

def change_custom():
    global difficulty
    difficulty = 3
    switch_page(custom_page)

def send_info():
    global scoreadd 
    scoreadd = int(entry_scoreadd.get())
    global scoredelete
    scoredelete = int(entry_scoredelete.get())
    global startpool 
    startpool = int(entry_startpool.get())
    global stoppool 
    stoppool = int(entry_stoppool.get())

def validating(event):
    if entry_number.get().isdigit() == True:
        if int(entry_number.get()) <= validstop and int(entry_number.get()) >= validstart:
            if difficulty == 2:
                check_gap()
                if gap > 25:
                    wrong_gap = tk.Label(main_page, text = "You are 25 position away!", bg = "#05051e", fg = "darkred", font = ('Helvetica', 12, BOLD))
                    wrong_gap.pack(pady = (10,5), padx = 10)
                    wrong_gap.after(1500, lambda:wrong_gap.pack_forget())
                else:
                    guess()
            else:
                guess()
        else:
            messagebox.showerror('Error', "You left the pool!")
    else:
        messagebox.showerror('Error', "enter a NUMBER!")

def validate_settings():
    if int(entry_startpool.get()) < int(entry_stoppool.get()):
        send_info()
        if difficulty == 3:
            randing_number(startpool,stoppool)
        root.bind('<Return>', validating)
        switch_page(main_page)
    else:
        messagebox.showerror('Error', "You enter a startpool higher number than stoppool!")

def check_gap():
    global gap
    if computer_number < int(entry_number.get()):
        gap = int(entry_number.get()) - computer_number
    else:
        gap = computer_number - int(entry_number.get())

def check_places():
    global first_scr, second_scr, third_scr
    global first_nickname, second_nickname, third_nickname
    global switch_case
    connection = sqlite3.connect('data/players.db')
    cursor = connection.cursor()
    players = []
    scores = []
    for player in cursor.execute('select nickname from rankings'):
        players.append(player)
    for scr in cursor.execute('select score from rankings'):
        scores.append(scr)
    #get maximum values
    first_scr = max(scores)
    first_ind = scores.index(first_scr)
    first_nickname = players[first_ind]
    players.pop(first_ind)
    scores.pop(first_ind)
    second_scr = max(scores)
    second_ind = scores.index(second_scr)
    second_nickname = players[second_ind]
    players.pop(second_ind)
    scores.pop(second_ind)
    third_scr = max(scores)
    third_ind = scores.index(third_scr)
    third_nickname = players[third_ind]
    players.pop(third_ind)
    scores.pop(third_ind)

def create_lead():
    first_place = tk.Label(lead_page, text = '1st Place', font = ('Helvetica', 18, BOLD), bg = "#05051e", fg = "#ff9900")
    first_place.pack(pady = 5)
    first_player = tk.Label(lead_page, text = f"{first_nickname[0]}  {first_scr[0]}", bg = "#05051e", fg = "#ff8000", font = ('Helvetica', 12, BOLD))
    first_player.pack(pady = 5)
    second_place = tk.Label(lead_page, text = '2nd Place', font = ('Helvetica', 18, BOLD), bg = "#05051e", fg = "#e68a00")
    second_place.pack(pady = 5)
    second_player = tk.Label(lead_page, text = f"{second_nickname[0]}  {second_scr[0]}", bg = "#05051e", fg = "#e67300", font = ('Helvetica', 12, BOLD))
    second_player.pack(pady = 5)
    third_place = tk.Label(lead_page, text = '3rd Place', font = ('Helvetica', 18, BOLD), bg = "#05051e", fg = "#cc7a00")
    third_place.pack(pady = 5)
    third_player = tk.Label(lead_page, text = f"{third_nickname[0]}  {third_scr[0]}", bg = "#05051e", fg = "#cc6600", font = ('Helvetica', 12, BOLD))
    third_player.pack(pady = 5)
    button_quit = tk.Button(lead_page, width = 20, text = "Quit", command = lambda:root.destroy(), cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 1, bg = "#b30047", fg = "white")
    button_quit.pack(pady = (20,0))
    root.protocol("WM_DELETE_WINDOW", lambda:root.destroy())
    
#Pages Setup
start_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
main_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
diff_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
custom_page = tk.Frame(root, height = 500, width = 500, bg ="#05051e")
last_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
lead_page = tk.Frame(root, height = 500, width = 500, bg = "#05051e")
start_page.grid(row = 0, column = 0 , sticky = "nsew")
main_page.grid(row = 0, column = 0 , sticky = "nsew")
diff_page.grid(row = 0, column = 0 , sticky = "nsew")
custom_page.grid(row = 0, column = 0 , sticky = "nsew")
last_page.grid(row = 0, column = 0 , sticky = "nsew")
lead_page.grid(row = 0, column = 0 , sticky = "nsew")
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
button_nickname = tk.Button(start_page, width = 20, text = "Play", cursor = "hand2", font = ('Helvetica', 12, BOLD), bg = "#01011a", fg = "white", command = lambda:switch_page(diff_page), bd = 1, activeforeground = "#a2a6c6")
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
button_guess = tk.Button(main_page, text = "Guess", font = ('Helvetica', 12, BOLD), cursor = "hand2", width = 20,bg = "#01011a", fg = "white", command = lambda:validating(event = None), bd = 1, activeforeground = "#a2a6c6")
button_guess.pack(padx = 10, pady = 10)

#Difficulty Page Setup
label_welcome = tk.Label(diff_page, text = "Welcome to GuessNumber", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
label_diff = tk.Label(diff_page, text = "Please choose difficulty", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 15, BOLD) )
label_diff.pack(padx = 10, pady = (10,30))
easy_diffbtn = tk.Button(diff_page, width = 25, height = 2, text = "Easy",command = lambda:change_easy(), cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 0, fg = "white", bg = "#86b300")
easy_diffbtn.pack(padx = 10, pady = (60,0))
medium_diffbtn = tk.Button(diff_page, width = 25, height = 2, text = "Medium", command = lambda:change_medium(), cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 0, fg = "white", bg = "#cc6600")
medium_diffbtn.pack(padx = 10)
hard_diffbtn = tk.Button(diff_page, width = 25, height = 2, text = "Hard", command = lambda:change_hard(), cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 0, fg = "white", bg = "#b30000")
hard_diffbtn.pack(padx = 10)
custom_diffbtn = tk.Button(diff_page, width = 25, height = 2, text = "Custom", font = ('Helvetica', 14, BOLD),command = lambda:[switch_page(custom_page), change_custom()], bd = 0, fg = "white", bg = "#2d2d86")
custom_diffbtn.pack(padx = 10, pady = (0,20))

#Custom Page Setup
label_welcome = tk.Label(custom_page, text = "Welcome to GuessNumber", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 18, BOLD))
label_welcome.pack(padx = 10, pady = 15)
label_difftext = tk.Label(custom_page, text = "Please complete bellow options", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 12, BOLD))
label_difftext.pack(padx = 10, pady = 5)
label_scoreadd = tk.Label(custom_page, text = "Please insert score added when you win a guess:", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 12, BOLD))
label_scoreadd.pack(padx = 3, pady = (3,0))
entry_scoreadd = tk.Entry(custom_page, width = 20, font = ('Helvetica', 12, BOLD), bd = 1)
entry_scoreadd.pack(padx = 3, pady = 3)
label_scoredelete = tk.Label(custom_page, text = "Please insert score deleted when you lose a guess:", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 12, BOLD))
label_scoredelete.pack(padx = 3, pady = (3,0))
entry_scoredelete = tk.Entry(custom_page, width = 20, font = ('Helvetica', 12, BOLD), bd = 1)
entry_scoredelete.pack(padx = 3, pady = 3)
label_startpool = tk.Label(custom_page, text = "Choose the number from where the generation starts:", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 12, BOLD))
label_startpool.pack(padx = 3, pady = (3,0))
entry_startpool = tk.Entry(custom_page, width = 20, font = ('Helvetica', 12, BOLD), bd = 1)
entry_startpool.pack(padx = 3, pady = 3)
label_stoppool = tk.Label(custom_page, text = "Choose the number up to where it is generated:", bg = "#05051e", fg = "#a2a6c6", font = ('Helvetica', 12, BOLD))
label_stoppool.pack(padx = 3, pady = (3,0))
entry_stoppool = tk.Entry(custom_page, width = 20, font = ('Helvetica', 12, BOLD), bd = 1)
entry_stoppool.pack(padx = 3, pady = 3)
send_customsettings = tk.Button(custom_page, text = "Play", width = 25, font = ('Helvetica', 14, BOLD), cursor = "hand2", bd = 0,fg = "white", bg = "#9D378C", command = lambda:[validate_settings()])
send_customsettings.pack(padx = 3, pady = 35)

#Last Page Setup
frame_winlogo = tk.Frame(last_page, width = 300, height = 300)
frame_winlogo.pack(pady = 40)
crown_logo = ImageTk.PhotoImage(Image.open("img/crown_logo.png"))
win_logo = tk.Label(frame_winlogo, image = crown_logo, bg = "#05051e")
win_logo.pack(fill = "both", expand = "yes")
button_continue = tk.Button(last_page, width = 20, text = "Continue", command = lambda:continue_playing(), cursor = "hand2",font = ('Helvetica', 14, BOLD), bd = 1, bg = "#00b359", fg = "white")
button_continue.pack(padx = 10, pady = (20,0))
button_quit = tk.Button(last_page, width = 20, text = "Quit", command = lambda:[write_db(),root.destroy()], cursor = "hand2", font = ('Helvetica', 14, BOLD), bd = 1, bg = "#b30047", fg = "white")
button_quit.pack(padx = 10)
button_lead = tk.Button(last_page, width = 20, text = "Leaderboard",  command = lambda:[write_db(), switch_page(lead_page), check_places(), create_lead()], cursor = "hand2", fg = "white", font = ('Helvetica', 14, BOLD), bd = 1, bg = "darkred")
button_lead.pack(padx = 10)

#LeaderBoard Page
label_up = tk.Label(lead_page, text = "GuessGame", font = ('Helvetica', 25, BOLD), bg = "#05051e", fg = "#a2a6c6")
label_up.pack()
frame_leadlogo = tk.Frame(lead_page, width = 250, height = 250)
frame_leadlogo.pack(pady = (20, 5))
lead_logo = ImageTk.PhotoImage(Image.open("img/lead_logo.png"))
label_logo = tk.Label(frame_leadlogo, image = lead_logo, bg = "#05051e")
label_logo.pack(fill = "both", expand = "yes")

#Run Window
root.mainloop()
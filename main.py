import tkinter as tk
import random
main_screen = tk.Tk()
main_screen.title("Rock, Paper & Scissor")
#Canvas is the window that gets created when we run the app
main_screen_canvas = tk.Canvas(main_screen, width = 400, height = 400, bg="SkyBlue4")
main_screen_canvas.pack()

#Label 1 is for naming the App
header = tk.Label(main_screen, text='Rock, Paper & Scissor')
header.config(font=('helvetica', 18, 'bold', 'underline'),bg='SkyBlue4',fg='white')

#Label 2 is for giving the text to entry field
sub_head_label = tk.Label(main_screen, text='Make your move!')
sub_head_label.config(font=('helvetica', 15, 'bold'),bg='SkyBlue4',fg='white')


result_variable = tk.StringVar()
player_choice_variable = tk.StringVar()
computer_choice_variable = tk.StringVar()

choice= ["rock", "paper", "scissor"]
def game(player):
    
    global player_choice, computer_choice
    computer=random.choice(choice)
    player_choice=player
    computer_choice=computer
    player_choice_variable.set(player)
    computer_choice_variable.set(computer)
    if(computer==player):
        result_variable.set("It's a Tie.")
    elif(computer=="scissor" and player=="rock"):
        result_variable.set("Player won")
    elif(computer=="scissor" and player=="paper"):
        result_variable.set("Computer won")
    elif(computer=="paper" and player=="rock"):
        result_variable.set("Computer won")
    elif(computer=="paper" and player=="scissor"):
        result_variable.set("Player won")
    elif(computer=="rock" and player=="paper"):
        result_variable.set("Player won")
    elif(computer=="rock" and player=="scissor"):
        result_variable.set("Computer won")

#buttons
rock_btn = tk.Button( text = 'Rock', command = lambda:game(choice[0]), font=('helvetica', 10, 'bold'),bg='Linen',fg='Black')
paper_btn = tk.Button(text = 'Paper', command = lambda:game(choice[1]), font=('helvetica', 10, 'bold'),bg='Linen',fg='black')
scissor_btn = tk.Button(text = 'Scissors', command = lambda:game(choice[2]), font=('helvetica', 10, 'bold'),bg='Linen',fg='black')

main_screen_canvas.create_window(200, 20, window=header)
main_screen_canvas.create_window(200, 100, window=sub_head_label)
main_screen_canvas.create_window(100, 150, window=rock_btn)
main_screen_canvas.create_window(200, 150, window=paper_btn)
main_screen_canvas.create_window(300, 150, window=scissor_btn)

player_label = tk.Label(main_screen, text='Player')
player_label.config(font=('helvetica', 15, 'bold'),bg='SkyBlue4',fg='white')
main_screen_canvas.create_window(90, 200, window=player_label)

computer_label = tk.Label(main_screen, text='Computer')
computer_label.config(font=('helvetica', 15, 'bold'),bg='SkyBlue4',fg='white')
main_screen_canvas.create_window(310, 200, window=computer_label)

vs_label = tk.Label(main_screen, text='VS')
vs_label.config(font=('helvetica', 20, 'bold'),bg='SkyBlue4',fg='white')
main_screen_canvas.create_window(200, 200, window=vs_label)


player_entry=tk.Entry(main_screen, textvariable = player_choice_variable, justify = 'center', width = 10, font=('helvetica', 10, 'bold'),bg='Orange2',fg='white')
main_screen_canvas.create_window(90, 250, window=player_entry)

computer_entry=tk.Entry(main_screen, textvariable = computer_choice_variable, justify = 'center', width = 10, font=('helvetica', 10, 'bold'),bg='Orange2',fg='white')
main_screen_canvas.create_window(310, 250, window=computer_entry)

result=tk.Label(main_screen, textvariable = result_variable, width = 20, font=('helvetica', 10, 'bold'),bg='Orange2',fg='white')
main_screen_canvas.create_window(200,350, window=result)

main_screen.mainloop()
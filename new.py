"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
# import random
# def get_computer_choice():
#     choices = ['rock', 'paper', 'scissors']
#     return random.choice(choices)

# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "It's a tie!"
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "paper" and computer_choice == "rock") or \
#          (player_choice == "scissors" and computer_choice == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"
# def main():
#     player_score = 0
#     computer_score = 0

#     while True:
#         player_input = input("Enter rock (r), paper (p), scissors (s) or quit to exit: ").lower()
        
#         # Map shortcuts to full names
#         choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
#         player_choice = choice_map.get(player_input, player_input)
        
#         if player_choice == 'quit':
#             print("Thanks for playing!")
#             break
        
#         if player_choice not in ['rock', 'paper', 'scissors']:
#             print("Invalid choice. Please try again.")
#             continue
        
#         computer_choice = get_computer_choice()
#         print(f"Computer chose: {computer_choice}")
        
#         result = determine_winner(player_choice, computer_choice)
#         print(result)
        
#         if result == "You win!":
#             player_score += 1
#         elif result == "Computer wins!":
#             computer_score += 1
        
#         print(f"Score - You: {player_score}, Computer: {computer_score}\n")
# if __name__ == "__main__":
#     main()  

import random
import tkinter as tk            
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
class RPSGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        
        self.player_score = 0
        self.computer_score = 0
        
        self.label = tk.Label(master, text="Choose your move:")
        self.label.pack()
        
        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack()
        
        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack()
        
        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0")
        self.score_label.pack()
    def play(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}")
if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()

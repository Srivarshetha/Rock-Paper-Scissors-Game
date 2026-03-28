import tkinter as tk
import random
import winsound  # For sound (Windows)

# Game choices
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0
rounds = 0
max_rounds = 5

# Sounds
def play_win_sound():
    winsound.Beep(1000, 300)

def play_lose_sound():
    winsound.Beep(400, 300)

def play_tie_sound():
    winsound.Beep(700, 300)

# Winner logic
def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Button click function
def play(user_choice):
    global user_score, computer_score, rounds

    if rounds >= max_rounds:
        result_label.config(text="Game Over! Click Restart")
        return

    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        result_text = "You Win! 🎉"
        play_win_sound()
    elif result == "computer":
        computer_score += 1
        result_text = "Computer Wins 😢"
        play_lose_sound()
    else:
        result_text = "It's a Tie 🤝"
        play_tie_sound()

    rounds += 1

    result_label.config(
        text=f"You: {user_choice} | Computer: {computer_choice}\n{result_text}"
    )

    score_label.config(
        text=f"Score -> You: {user_score} | Computer: {computer_score} | Round: {rounds}/5"
    )

    # End game after 5 rounds
    if rounds == max_rounds:
        if user_score > computer_score:
            final = "🏆 You Won the Game!"
        elif computer_score > user_score:
            final = "💻 Computer Won the Game!"
        else:
            final = "🤝 Game Tie!"

        result_label.config(text=result_label.cget("text") + "\n" + final)

# Restart game
def restart_game():
    global user_score, computer_score, rounds
    user_score = 0
    computer_score = 0
    rounds = 0

    result_label.config(text="Make your move!")
    score_label.config(text="Score -> You: 0 | Computer: 0 | Round: 0/5")

# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("400x400")
root.config(bg="#222")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), fg="white", bg="#222")
title.pack(pady=10)

# Buttons with emojis
btn_frame = tk.Frame(root, bg="#222")
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="🪨 Rock", width=12, command=lambda: play("rock"))
paper_btn = tk.Button(btn_frame, text="📄 Paper", width=12, command=lambda: play("paper"))
scissors_btn = tk.Button(btn_frame, text="✂ Scissors", width=12, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="Make your move!", font=("Arial", 12), fg="white", bg="#222")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="Score -> You: 0 | Computer: 0 | Round: 0/5",
                       font=("Arial", 10), fg="white", bg="#222")
score_label.pack()

# Restart button
restart_btn = tk.Button(root, text="🔄 Restart Game", command=restart_game)
restart_btn.pack(pady=20)

root.mainloop()
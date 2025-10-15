

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive word-guessing experience.

## 📝 Tasks

### 🛠️ Word Selection and Setup

#### Description
Create a list of words and randomly select one for the player to guess. Set up the game state to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a list of at least 5 words
- Randomly select one word for each game
- Initialize variables for guessed letters and attempts

### 🛠️ Gameplay Loop

#### Description
Implement the main game loop where the player guesses letters, and the game updates progress and tracks incorrect guesses.

#### Requirements
Completed program should:

- Prompt the player to guess a letter
- Show current progress (e.g., _ a _ _ m a n)
- Track and display remaining incorrect guesses
- Prevent repeated guesses from counting against the player

### 🛠️ Win/Lose Conditions

#### Description
End the game when the player either guesses the word or runs out of attempts. Display appropriate messages for winning or losing.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or attempts reach zero
- Display a congratulatory message if the player wins
- Display a message revealing the word if the player loses

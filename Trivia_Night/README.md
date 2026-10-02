# Python Trivia Game 🎮

A simple, interactive trivia game built in small steps using core Python concepts. This project was created as a hands-on learning activity to practice data structures, functions, control flow, and error handling.

## Features
- **Question Bank:** Stores questions, answers, and categories using a list of dictionaries.
- **Smart Validation:** Standardizes player input using `.strip()` and `.lower()` so extra spaces or capitalization don't affect the score.
- **Error & Edge-Case Handling:** Safely handles blank inputs and `EOFError` without crashing the program.
- **Score Tracking:** Uses a `for` loop to go through questions, tracks the running score, and displays the final result using an f-string.

## Project Structure
```text
my-trivia-project/
├── src/
│   └── game.py       # The main trivia game source code
├── README.md         # Project documentation
└── JOURNAL.md        # Learning journal and key takeaways
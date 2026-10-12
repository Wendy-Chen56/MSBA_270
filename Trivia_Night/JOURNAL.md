# Learning Journal: Key Takeaways

When I first started this activity, the goal seemed a bit overwhelming, so I broke it down into small steps:

1. **Organizing Data:** I learned how to structure data using a Python list of dictionaries. Each dictionary acts like a neat container holding three keys: `"question"`, `"answer"`, and `"category"`.
2. **Writing Functions & Handling Input:** I practiced writing my own function (`ask_question()`) to display the category and question, and used `input()` to get the player's response. 
3. **Cleaning and Comparing Text:** A big takeaway for me was realizing how strict Python is with text. I learned to use `.strip()` and `.lower()` together so that extra spaces or accidental capital letters won't make a correct answer wrong.
4. **Handling Errors Gracefully:** I discovered how important it is to think about user mistakes. I used an `if` statement to catch blank answers and a `try/except` block to handle an `EOFError` safely without crashing the whole program.
5. **Putting It All Together:** Finally, I used a `for` loop to go through the question bank, updated the score step by step, and displayed the final result using an f-string. Testing everything with correct, wrong, and blank inputs showed me why debugging and edge-case testing are so crucial.

## New Skills Developed
- Creating and navigating lists of dictionaries
- Writing and calling Python functions with return values
- Capturing user input safely using `input()`
- Standardizing and cleaning strings with `.strip()` and `.lower()`
- Implementing basic error handling (`try/except` and blank input checks)
- Tracking progress with `for` loops and running scores
- Displaying neat results using f-strings
- Step-by-step program testing and debugging
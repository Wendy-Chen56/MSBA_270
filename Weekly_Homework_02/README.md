# Weekly Homework 02: Data-Driven Programs

## Name
Wendy Chen

## Exercises Completed
- Exercise 12-2: Enhance the Movie List 2D Program
- Exercise 6-1: Test Scores Program
- Exercise 8-1: Future Value Program

## How to Run the Programs

Open a terminal in the Weekly_Homework_02 folder.

### Exercise 12-2
Run:

python movie_list_2d.py

This program allows the user to list, add, and delete movies. Each movie is stored as a dictionary with a name and year, and the movies are stored in a list.

### Exercise 6-1
Run:

python test_scores.py

This program allows the user to enter test scores. The scores are stored in a list and passed between functions. The program calculates the total, number of scores, and average score.

### Exercise 8-1
Run:

python future_value.py

This program calculates future value based on monthly investment, yearly interest rate, and number of years. It uses exception handling to prevent the program from crashing when invalid numeric input is entered.

## Problem and Fix

One problem I found was in Exercise 8-1. The original program crashed when I entered text such as "abc" where a number was expected.

I fixed this problem by adding try/except blocks to catch ValueError. After the change, the program displays an error message and asks the user to enter the value again instead of crashing. I also tested values outside the allowed range to make sure the original data validation still worked.

## AI-Use Note

I used ChatGPT as a learning and review tool for this homework. I asked ChatGPT to explain the assignment steps, help me understand lists, dictionaries, functions, and exception handling, and suggest test cases.

One suggestion I accepted was using try/except ValueError in Exercise 8-1 to handle invalid numeric input. I tested the programs myself with valid and invalid inputs and reviewed the code so I could understand and explain the changes.
# Chapter 3 Exercises Journal

## Exercise 3-1: Enhance the Miles Per Gallon Program

### Step 1
I created the `mpg.py` file in Visual Studio Code and entered the original Miles Per Gallon program from Figure 3-8.

### Step 2
I tested the original program with both valid and invalid values. With 150 miles driven and 30 gallons used, the program calculated 5.0 miles per gallon. I also tested 0 gallons, and the program displayed an error message because gallons used must be greater than zero.

### Step 3
I added a while loop so the user can calculate miles per gallon for more than one trip. After each calculation, the program asks whether the user wants to enter another trip. I tested the loop by entering two trips. When I entered "y", the program repeated, and when I entered "n", the loop ended.

### Step 4
I added an entry for the cost per gallon and added validation to make sure the value is greater than zero. I also added calculations for the total gas cost and cost per mile. I tested the program with valid values and confirmed that it displayed the miles per gallon, total gas cost, and cost per mile. I also tested an invalid cost of 0, and the program displayed an error message.


## Exercise 3-2: Enhance the Test Scores Program

### Step 1
I created the `test_scores.py` file in Visual Studio Code and entered the original Test Scores program from Figure 3-16.

### Step 2
I tested the original program with both valid and invalid values. With the valid scores 75, 85, and 95, the program calculated a total score of 255 and an average score of 85. I also entered -85 as an invalid score. The original program accepted the invalid score because it did not have validation for test scores.

### Step 3
I replaced the original for loop with nested while loops. The inner while loop allows the user to enter scores for one set, and the outer while loop allows the user to enter another set of test scores. I also kept the score validation so scores must be from 0 through 100. I tested two sets of scores, and entering "y" allowed the program to start another set.

### Step 4
I modified the inner while loop so the user can enter "end" to finish a set of test scores. I used an if statement to check for "end" and nested another if statement inside the else clause to validate each score. Invalid scores outside the range of 0 through 100 display an error message and are not included in the calculations. I tested the program with multiple scores, an invalid score, and "end".

### Step 5
I commented out the original inner while loop and created a new while loop using an assignment expression. The assignment expression gets the user's input, converts it to lowercase, assigns it to `score_entry`, and checks whether it is not equal to "end". I tested the program with valid scores, an invalid score, and "END". The program correctly ended the score entry when "END" was entered.


## Exercise 3-3: Enhance the Future Value Program

### Step 1
I created the `future_value.py` file in Visual Studio Code and added the basic Future Value Calculator program. The starting program accepts the monthly investment, yearly interest rate, and number of years and calculates the future value.

### Step 2
I tested the Future Value program using valid values because the starting program did not have data validation. I entered a monthly investment of 100, a yearly interest rate of 12, and 10 years. The program calculated a future value of 23233.91.

### Step 3
I added a while loop to validate the monthly investment. The monthly investment must be greater than zero. I tested the program by entering 0, and the program displayed an error message and asked for the monthly investment again. After I entered 100, the program accepted the value and continued.

### Step 4
I added validation for the yearly interest rate and number of years. The yearly interest rate must be greater than 0 and less than or equal to 15, and the number of years must be greater than 0 and less than or equal to 50. I tested an invalid value of 16 for the interest rate and an invalid value of 100 for the number of years. The program displayed the appropriate error messages and asked me to enter the values again.

### Step 5
I modified the calculation so the program displays the future value after each year. I used the integer returned by the `range()` function as the year number. I tested the program with a monthly investment of 100, a yearly interest rate of 12, and 10 years. The program displayed the future value for Years 1 through 10, and the final future value was 23233.91.

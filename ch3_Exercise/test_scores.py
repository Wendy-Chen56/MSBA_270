# display a welcome message
print("The Test Scores program")
print()

another_set = "y"

while another_set.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

    # initialize variables
    total_score = 0
    score_count = 0

    # Original while loop from Step 4
    # while True:
    #     score_entry = input("Enter test score: ")
    #
    #     if score_entry.lower() == "end":
    #         break
    #     else:
    #         score = int(score_entry)
    #
    #         if score < 0 or score > 100:
    #             print("Test score must be from 0 through 100. Try again.")
    #         else:
    #             total_score += score
    #             score_count += 1

    # New while loop using an assignment expression
    while (score_entry := input("Enter test score: ").lower()) != "end":
        score = int(score_entry)

        if score < 0 or score > 100:
            print("Test score must be from 0 through 100. Try again.")
        else:
            total_score += score
            score_count += 1

    # calculate and display results
    if score_count > 0:
        average_score = round(total_score / score_count)

        print("======================")
        print("Total Score:  ", total_score)
        print("Average Score:", average_score)
        print()

    another_set = input("Enter another set of test scores (y/n)? ")
    print()

print("Bye!")
QUESTIONS = [
    {
        "question": "What is the largest ocean on Earth?",
        "answer": "Pacific Ocean",
        "category": "Geography",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars",
        "category": "Space",
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10",
        "category": "Math",
    },
    {
        "question": "What color do you get by mixing red and blue?",
        "answer": "Purple",
        "category": "General",
    },
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "category": "Geography",
    },
]

def ask_question(question):
    print(f"\n[{question['category']}]")
    print(question["question"])

    try:
        answer = input("Your answer: ")
    except EOFError:
        print("No answer was received.")
        return False

    if not answer.strip():
        print("Please enter an answer.")
        return False

    return answer.strip().lower() == question["answer"].strip().lower()

score = 0

for question in QUESTIONS:
    if ask_question(question):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer is {question['answer']}.")

print(f"\nYou earned {score} out of {len(QUESTIONS)} points.")



questions = [
    {
        "question": "What is the capital of Ethiopia?",
        "options": ["A. Addis Ababa", "B. Nairobi", "C. Cairo", "D. London"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 5?",
        "options": ["A. 8", "B. 9", "C. 10", "D. 11"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. return", "D. class"],
        "answer": "B"
    }
]


def display_question(question):
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)


def validate_answer():
    while True:
        answer = input("Enter your answer (A, B, C, D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Invalid option. Please choose A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def update_score(score, is_correct):
    if is_correct:
        score += 1

    return score


def display_results(score, total):
    incorrect = total - score
    percentage = (score / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {score}")
    print(f"Incorrect Answers: {incorrect}")
    print(f"Final Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Category: Excellent")
    elif percentage >= 60:
        print("Category: Good")
    elif percentage >= 40:
        print("Category: Fair")
    else:
        print("Category: Needs Improvement")


def play_quiz():
    score = 0

    for question in questions:
        display_question(question)

        user_answer = validate_answer()
        correct_answer = question["answer"]

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            score = update_score(score, True)
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")

    display_results(score, len(questions))


def main():
    while True:
        print("\n===== PYTHON QUIZ =====")
        play_quiz()

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thank you for playing!")
            break


main()
import json

with open("questions.json", 'r') as file_questions:
    questions_string = file_questions.read()

questions = json.loads(questions_string)

score = 0
for question in questions:
    print(question["question_text"])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question['user_choice'] = user_choice

for index, question in enumerate(questions):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong answer"

    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"

    print(message)

print(score, "/", len(questions))
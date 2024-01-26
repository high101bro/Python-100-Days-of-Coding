from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

QUESTION_AMOUNT = 25
response = requests.get(
    url=f"https://opentdb.com/api.php?amount={QUESTION_AMOUNT}&type=boolean"
)
# url = f"https://opentdb.com/api.php?amount={QUESTION_AMOUNT}&category=18&type=boolean"
response.raise_for_status()

question_bank = []
question_data = response.json()['results']

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank, QUESTION_AMOUNT)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

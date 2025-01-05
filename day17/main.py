from data import question_data as question_data
from question_model import Question as Question
from quiz_brain import Quizbrain as Quizbrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'you got {quiz.score} out of {len(quiz.question_list)} correct')
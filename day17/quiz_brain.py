class Quizbrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        this_q = self.question_list[self.question_number]
        text, answer = this_q.text, this_q.answer
        self.question_number += 1
        resp = input(f"Q.{self.question_number}: {text} (True/False)? :")
        if self.check_answer(resp):
            self.score += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, response):
        ans = self.question_list[self.question_number-1].answer.lower()  # don't care about case
        response = response.lower()
        if ans == response or ans[0] == response:  # response matches whole word or is equal to first letter of answer
            print("that's correct")
            return True
        else:
            print(f"that's wrong.  the right answer was {ans}")
            return False


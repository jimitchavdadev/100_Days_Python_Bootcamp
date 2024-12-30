class QuizBrain:
    def __init__(self, q_list, score=0):
        self.question_num = 0
        self.question_list = q_list
        self.score = score

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        ans = input(f"Q.{self.question_num}: {current_question.text} (True/False): ")
        if ans.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_num}\n")

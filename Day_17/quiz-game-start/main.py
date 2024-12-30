from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    temp=Question(question_text, question_answer)
    question_bank.append(temp)
    
quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    
print(f"you have scored {quiz.score}/12")
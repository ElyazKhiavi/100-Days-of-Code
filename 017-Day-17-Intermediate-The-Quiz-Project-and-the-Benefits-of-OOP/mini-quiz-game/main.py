from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question_bank.append(Question(question_text, answer))


quiz = QuizBrain(question_bank)

def main():
    while quiz.has_question():
        quiz.ask_question()
    print("You've completed the quiz")
    print(f'Your final score was: {quiz.score}/{quiz.question_number}')

if __name__ == "__main__":
    main()


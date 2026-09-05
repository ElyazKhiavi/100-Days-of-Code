import html


class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_list = q_list
        self.current_question_number = 0

    def quiz_finished(self) -> bool:
        return self.current_question_number == len(self.question_list)

    def show_question(self) -> str:
        current_question = self.question_list[self.current_question_number]
        q_text = html.unescape(current_question.text)
        return f"Q.{self.current_question_number+1}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        current_question = self.question_list[self.current_question_number]
        correct_answer = current_question.answer
        is_correct = user_answer.lower() == correct_answer.lower()
        if is_correct:
            self.score += 1
        self.current_question_number += 1
        return is_correct

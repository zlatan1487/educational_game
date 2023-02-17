class Question:

    def __init__(self, question_text, difficulty_level, correct_answer):
        self.question_text = question_text
        self.difficulty_level = difficulty_level
        self.correct_answer = correct_answer

        self.user_response = None
        self.score = self.difficulty_level * 10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.correct_answer == self.user_response

    def build_question(self):
        return f'Вопрос: {self.question_text}' '\n'\
               f'Сложность: {self.difficulty_level}/5'

    def build_feedback(self):
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        else:
            return f'Ответ неверный. Верный ответ - "{self.correct_answer}"'


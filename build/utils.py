
from build.question import Question


def load_question(data):
    """
    функция загружает список всех вопросов из модуля "requests_questions.py"
    :param data: 
    :return: возвращает сформированый список - "questions" экземпляров класса "Question" - "question"
    """
    questions = []

    for item in data:
        question_text = item['q']
        difficulty_level = int(item['d'])
        correct_answer = item['a']
        question = Question(question_text, difficulty_level, correct_answer)
        questions.append(question)

    return questions


def print_statistics(questions):
    """
    функция распечатки статистики игры
    :param questions:
    :return: возвращает f-строку с результатом
    """
    # количество набранных баллов
    score = 0
    # количество правильных ответов
    count = 0
    # количество возможных вопросов
    questions_length = len(questions)

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1

    return f'Вот и всё!' '\n'\
           f'Отвечено {count} вопроса из {questions_length}' '\n'\
           f'Набрано баллов: {score}'

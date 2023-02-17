from build.utils import load_question, print_statistics
from build.requests_questions import list_questions
import random

if __name__ == '__main__':
    print('Игра начинается!')

    # вызов функции "load_question" с параметром "list_questions" в котором лежат список вопров,
    # через request. см. "requests_questions.py"
    questions = load_question(list_questions)

    # выбор рандомного элемента из списка возможных вопросов
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())

        user_response = input('Ваш ответ...  ')

        question.user_response = user_response
        print(question.build_feedback())

    print('')
    print(30 * '*')
    # вызов функции статистики игры
    print(print_statistics(questions))


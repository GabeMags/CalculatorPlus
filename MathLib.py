import random


# Generates a random math question with numbers including 0-9 and operators plus or minus. Returns a string.
def gen_question(difficulty: int = 1):
    if difficulty < 1:
        print("Invalid argument, exiting function.")
        return
    difficulty = (difficulty * 2) + 1
    operator = "+-"
    numbers = "0123456789"
    question_list = []
    for x in range(difficulty):
        if x % 2 == 0:
            question_list.insert(x, random.choice(numbers))
        else:
            question_list.insert(x, " " + random.choice(operator) + " ")

    return ''.join(question_list)


# Evaluates a math question. Returns the answer in a string.
def evaluate_question(equation):
    try:
        answer = eval(equation)
    except:
        answer = "ERROR"
    return answer


# Compares the user the inputted answer with the actual answer, returns a boolean.
def compare_answers(actual_answer, user_input_answer):
    return str(actual_answer) == str(user_input_answer)



import random


# Generates a random math question with numbers including 0-9 and operators plus or minus. Returns a string.
def gen_question():
    operator = "+-"
    numbers = "0123456789"
    return random.choice(numbers) + " " + random.choice(operator) + " " + random.choice(numbers)


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


count = 3
while count != 0:
    question = gen_question()
    actual_answer = evaluate_question(question)
    print(question)
    try:
        user_input = int(input("Answer is: "))
        print(compare_answers(actual_answer, user_input))
        if not compare_answers(actual_answer, user_input):
            count = count - 1
    except:
        print("invalid input")
        count = count - 1

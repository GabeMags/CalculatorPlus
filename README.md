# CalculatorPlus
CPSC 362 Group 8's Calculator but with additional fun features



import random
def calc_For_Kids():
    numb1 = random.randint(1, 9)
    numb2 = random.randint(1, 9)
    print(" what do you think the sum of these two number is : ", numb1, " + ", numb2, "\n")
    while True:
        sum = numb1 + numb2
        sum1 = input()
        miro = int(sum1)
        if miro == sum:
            print(" Perfect, the answer is correct:")
            break
        elif miro != sum:
            print("i am so sorry , your answer is wrong kitto:")
            print(" Try again : ", numb1, " + ", numb2, "\n")
calc_For_Kids()

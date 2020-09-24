import random
a = random.randint(0, 9)
b = random.randint(0, 9)

class cal():
    def init(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

print("0. Exit")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter choice: "))

obj = cal(a, b)
while choice != 0:

    if choice == 1:
        print(" what do you think the sum of these two numbers are? ", a, " + ", b)
        while True:
            sum = obj.add()
            sum = input()
            answer = int(sum)
            if answer == obj.add():
                print("Perfect, the answer is correct:")
                break
            elif answer != sum:
                print("I am sorry, your answer is wrong kitto,Please Try again:")
                break
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()

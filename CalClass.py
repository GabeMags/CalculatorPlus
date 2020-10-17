# import random
#
# image = 'w'
#
#
# class cal():
#     def init(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# a = random.randint(0, 9)
# b = random.randint(0, 9)
#
# obj = cal(a, b)
# print("0. Exit")
# print("1. Add")
# choice = int(input("Enter choice: "))
# cnt = 0  # To hold number of tries
# if choice == 1:
#     while True:
#         print(" what do you think the sum of these two numbers are? ", a, " + ", b)
#         print("This is how it looks viually", a * image, "+ ", b * image)
#
#         answer= int(input())
#
#         if answer == obj.add():
#             print("Perfect, the answer is correct...")
#             cont = input("\nIf you want to solve another question then press 1. If not then any other key ")
#             if cont == "1":
#                 a = random.randint(0, 9)
#                 b = random.randint(0, 9)
#                 obj = cal(a, b)
#                 cnt = 0
#                 continue
#             else:
#                 break
#
#         elif answer != obj.add():
#             print("I am sorry, your answer is wrong Sean,Please Try again:")
#             # Incrementing count
#             cnt = cnt + 1
#             # Checking count
#             if cnt == 3:
#                 # Prompting for next try
#                 ans = input(
#                     "\nMax number of tries reached. Do you want to try another question or quit? (T/Q): ")
#                 # Checking answer
#                 if ans.upper() == "T":
#                     a = random.randint(0, 9)
#                     b = random.randint(0, 9)
#                     obj = cal(a, b)
#                     continue
#                 else:
#                     break
#
#             else:
#                 continue
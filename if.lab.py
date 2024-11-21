# Задание 1
# Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность. Если число четное требуется вывести на экран число и надпись Even number. Если число нечетное выведите на экран число и надпись Odd number.

input_one = int(input("Odd or even check; Enter a number: "))
if input_one % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Задание 2
# Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. Если число кратно требуется вывести на экран число и надпись Number is a multiple of 7. Если число не кратно выведите на экран число и надпись Number is not a multiple of 7.

input_two = int(input("Multiple of 7 check; Enter a number:"))
if input_two % 7 == 0:
    print("Number is a multiple of 7")
else:
    print("Number is not a multiple of 7")

# Задание 3
# Пользователь вводит с клавиатуры два числа. Необходимо найти максимум из двух чисел и показать его на экран.

input_three = int(input("Max input check; Enter the first number:"))
input_four = int(input("Max input check; Enter the second number:"))
if input_three > input_four:
    print(input_three, "is greater")
else:
    print(input_four, 'is greater')

# Задание 4
# Пользователь вводит с клавиатуры два числа. Необходимо найти минимум из двух чисел и показать его на экран.

input_five = int(input("Lesser input check; Enter the first number:"))
input_six = int(input("Lesser input check; Enter the second number:"))
if input_five < input_six:
    print(input_five, "is lesser")
else:
    print(input_six, 'is lesser')

# Задание 5
# Пользователь вводит с клавиатуры два числа. В зависимости от выбора пользователя нужно показать сумму двух чисел, разницу двух чисел, среднеарифметическое или произведение двух чисел.

input_seven = int(input("Calculator; Enter the first number: "))
input_eight = int(input("Calculator; Enter the second number: "))
action = input("Enter action, +, -, *, or anything else for arithmetic mean: ")
if action == "+":
    print("Sum is", input_seven + input_eight)
elif action == "-":
    print("Subtraction is", input_seven - input_eight)
elif action == "*":
    print("Multiplication is", input_seven * input_eight)
else:
    print("Arithmetic mean is", (input_seven + input_eight) / 2)
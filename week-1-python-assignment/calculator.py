# declaration of variables that will assign user inputs
num1 = input("Enter an integer of your choosing: ")
num2 = input("Enter another integer of your choosing: ")
operator = input("Enter a mathematical operation (+, -, /, *): ")

#
results = eval(num1 + operator + num2)

print("The results are: ", num1, operator, num2, " = ", results)

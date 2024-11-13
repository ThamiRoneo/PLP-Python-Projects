# declaration of variables that will assign user inputs
num1 = input("Enter a number of your choosing: ")
num2 = input("Enter another number of your choosing: ")
operator = input("Enter a mathematical operation (+, -, /, *): ")

# converting user inputs to integers
results = eval(num1 + operator + num2)

# printing the result of the operation
print("The results are: ", num1, operator, num2, " = ", results)

def calculator():
  user_operation = input("What is the operation you want to do? Type 'add', 'subtract', 'multiply', or 'divide'. '\n")
  user_number = float(input("What is your first number ?: "))
  user_number_2 = float(input("What is your second number?: "))
  if user_operation == "add":
    print(f"Your result is : {user_number + user_number_2}")
  elif user_operation == "subtract":
    print(f"Your result is : {user_number - user_number_2}")
  elif user_operation == "multiply":
    print(f"Your result is : {user_number * user_number_2}")
  elif user_operation == "divide":
    print(f"Your result is : {user_number / user_number_2}")
  else:
    print("Please type which is defined!\n")
    
user_continue = True

while user_continue == True:
  calculator()
  user_continue = input("Do you want to continue? Type 'yes' or 'no'.")
  if user_continue == "no":
    user_continue = False
  else:
    print("Please type just 'yes' or 'no'.")
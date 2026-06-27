# ============ - - -  Simple Calculator - - - - ==============

print("======= Simple Calculator =========")


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number : " ))

print("\nChoose Operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter Your Choice (1/2/3/4): ")


if choice == "1":
    print("Answer =", num1 + num2)

elif choice == "2":
    print("Answer =", num1 - num2)

elif choice == "3" :
    print("Answer =", num1 * num2)

elif choice == "4":
    if num2  != 0:
        print("Answer =", num1 / num2)
    else:
        print("Error ! Division by zero is not allowed.")
else:
    print("Invalid Choice!")        


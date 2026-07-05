# SIMPLE CALCULATOR

print("""
========== SIMPLE CALCULATOR ==========

Available Operations
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
^   Power

Type C to clear
Type OFF to exit
""")

while True:

    first_number = float(input("\nEnter First Number: "))

    while True:

        operator = input("Enter Operator: ").upper()

        if operator == "OFF":
            print("Thank you for using the calculator.")
            exit()

        elif operator == "C":
            print("Calculator Cleared.")
            break

        elif operator == "+":
            second_number = float(input("Enter Second Number: "))
            answer = first_number + second_number
            print("Answer =", answer)
            first_number = answer

        elif operator == "-":
            second_number = float(input("Enter Second Number: "))
            answer = first_number - second_number
            print("Answer =", answer)
            first_number = answer

        elif operator == "*":
            second_number = float(input("Enter Second Number: "))
            answer = first_number * second_number
            print("Answer =", answer)
            first_number = answer

        elif operator == "/":
            second_number = float(input("Enter Second Number: "))

            if second_number == 0:
                print("Cannot divide by zero.")
            else:
                answer = first_number / second_number
                print("Answer =", answer)
                first_number = answer

        elif operator == "//":
            second_number = float(input("Enter Second Number: "))

            if second_number == 0:
                print("Cannot divide by zero.")
            else:
                answer = first_number // second_number
                print("Answer =", answer)
                first_number = answer

        elif operator == "%":
            second_number = float(input("Enter Second Number: "))

            if second_number == 0:
                print("Cannot divide by zero.")
            else:
                answer = first_number % second_number
                print("Answer =", answer)
                first_number = answer

        elif operator == "^":
            second_number = float(input("Enter Second Number: "))
            answer = first_number ** second_number
            print("Answer =", answer)
            first_number = answer

        else:
            print("Invalid Operator.")
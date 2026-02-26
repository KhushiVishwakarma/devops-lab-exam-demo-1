def factorial(n):
    if n < 0:
        return None
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    print("      FACTORIAL CALCULATOR       ")
    while True:
        try:
            num = int(input("\nEnter a non-negative integer: "))

            if num < 0:
                print("Factorial not defined for negative numbers.")
            else:
                result = factorial(num)
                print(f"Factorial of {num} = {result}")

        except ValueError:
            print("Invalid input. Please enter an integer.")

        choice = input("\nDo you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("\nThank you for using Factorial Calculator")
            break

if __name__ == "__main__":
    main()

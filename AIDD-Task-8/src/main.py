import argparse
from src.calculator.operations import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")
    parser.add_argument("--num1", type=float, help="The first number")
    parser.add_argument("--operator", type=str, help="The operator (+, -, *, /)")
    parser.add_argument("--num2", type=float, help="The second number")

    args = parser.parse_args()

    # Basic validation for now, will be expanded
    if args.num1 is None or args.operator is None or args.num2 is None:
        parser.print_help()
        return

    # Placeholder for calculation logic
    result = None
    try:
        if args.operator == '+':
            result = add(args.num1, args.num2)
        elif args.operator == '-':
            result = subtract(args.num1, args.num2)
        elif args.operator == '*':
            result = multiply(args.num1, args.num2)
        elif args.operator == '/':
            result = divide(args.num1, args.num2)
        else:
            print(f"Error: Invalid operator '{args.operator}'. Supported operators are +, -, *, /")
            return
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(result)

if __name__ == "__main__":
    main()

import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple calculator script!")

# Add arguments
parser.add_argument("operation", help="The operation to perform: add, subtract, multiply, divide")
parser.add_argument("num1", type=float, help="The first number")
parser.add_argument("num2", type=float, help="The second number")

# Parse the arguments
args = parser.parse_args()

# Perform the operation
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    result = args.num1 / args.num2
else:
    print("Unknown operation!")
    exit(1)

print(f"The result is: {result}")

print(f"Operation received: {args.operation}")

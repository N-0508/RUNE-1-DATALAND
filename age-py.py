from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.today()

    # Calculate the age
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    # Adjust if birthday hasn't occurred yet this year
    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximate correction
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

# 👇 Welcome to Dataland! Input your birthdate in DD-MM-YYYY format
user_birthdate = input("🧭 Welcome to Dataland! Enter your birthdate (DD-MM-YYYY): ")
years, months, days = calculate_age(user_birthdate)

print(f"🎂 You are {years} years, {months} months, and {days} days old in Dataland! 🧠")













def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "🚫 Cannot divide by zero!"
    return x / y

print("🧠 Welcome to Mathsmith's Tool 🧮")
print("Choose your operation:")
print("1 ➕ Add")
print("2 ➖ Subtract")
print("3 ✖ Multiply")
print("4 ➗ Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"✨ Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"✨ Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"✨ Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"✨ Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("❌ Invalid input — please try again with Mathsmith’s Tool!")


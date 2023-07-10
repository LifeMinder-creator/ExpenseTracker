import csv

def display_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

def add_expense():
    date = input("Enter the date (DD/MM/YYYY): ")
    description = input("Enter a description: ")
    amount = float(input("Enter the amount: "))
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    
    print("Expense added successfully!")

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        total = 0
        
        for row in reader:
            print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}")
            total += float(row[2])
        
        print("Total Expenses:", total)

def calculate_total_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        total = 0
        
        for row in reader:
            total += float(row[2])
        
        print("Total Expenses:", total)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total_expenses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},     
    {"description": "Taxi", "category": "Transport", "amount": 120},     
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]
threshold = 200
def add_expenses(expenses,description,category,amount):
    if amount <= 0:
        print("Invalid Amount")
    else:
        if not description.strip():
            print("Description can't be empty.")
        else:
            if not category.strip():
                print("Category can't be empty.")
            else: 
                description = description.strip()
                category = category.strip()  

                expenses.append({
                    "description": description,
                    "category": category,
                    "amount" : amount
                })
    return expenses

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total



def calculate_by_category(expenses):
    category_total ={}
    for expense in expenses:      

        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount
    return category_total



def find_largest_expense(expenses):
    if not expenses:
        return None
    
    largest_expense = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest_expense["amount"]:
            largest_expense = expense

    return largest_expense



def above_threshold_expenses(expenses, threshold):
    above_threshold = []

    for expense in expenses:
        if expense["amount"] > threshold:
            above_threshold.append(expense)

    return above_threshold

def generate_report(expenses, threshold):

    total = calculate_total(expenses)
    category_total = calculate_by_category(expenses)
    largest = find_largest_expense(expenses)
    above_threshold  = above_threshold_expenses(expenses, threshold)


    print("=================================================")
    print("                  REPORT EXPENSE                 ")
    print("=================================================")

    print("\nTotal Expenses: ", total)
    print("\nSpending by category: ")

    for category in category_total:     
        amount = category_total[category]
        if total > 0:
            percentage = (amount / total ) * 100
        else:
            percentage = 0

        print(category,":", amount, "(", round(percentage,2), "%",")" )

    if category_total:
        highest_category = max(category_total,key=category_total.get)

        print("\nHighest Spending Category:")
        print(highest_category, "-", category_total[highest_category])
    else:
        print("\nNo spending categories available.")
    


    print("\nLargest Expense: ")
    if largest is None:
        print("No Expenses Available")
    else:
        print(largest["description"], "-", largest["amount"])


    print("\nExpense above threshold: ")
    for expense in above_threshold:
        print("-------------------------------------------------------")
        print("Description:", expense["description"] , "|", "Category:", expense["category"], "|", "Amount", expense["amount"])


print()
generate_report(expenses, threshold)

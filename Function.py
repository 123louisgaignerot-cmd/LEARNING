def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"you are {age} years old")
    print("Happy birthday")
    print()

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of R{amount:.2f} is due:{due_date}")

def create_name(first, last):
    first = first.capitalize()  
    last = last.capitalize()
    return first + " " + last

full_name = create_name("SHAdow", "walker")
print(full_name)
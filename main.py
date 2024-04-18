import pandas as pd

def app_border(text):
    border = "#" * (len(text) + 4)

    print(border)
    print(f"# {text} #")
    print(border)

def hello():
    app_border("Welcome to TrueFix")
    print("Please select an option")
    print("1. Login")
    print("2. Exit")
    
    if input("Enter your choice: ") == "1":
        login()
    elif input("Enter your choice: ") == "2":
        exit_func()
        

def login():
    print("Login")
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "admin" and password == "TrueFix123":
        print("Login successful✅\n\nWelcome Temur 🤖 \n\n")
        logged_in_app()
    else:
        print("Login failed❌")
        login()
    

def exit_func():
    print("Goodbye👋")
    exit()

def logged_in_app():
    app_border("TrueFix CRM")
    print("Please select an option")
    print("1. Sales")
    print("2. Customers")
    print("3. Parts")
    print("4. Add New Record")
    print("5. Logout")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view("sales")
    elif choice == "2":
        view("customers")
    elif choice == "3":
        view("parts")
    elif choice == "4":
        print("Add New Record")
        new_record_query = input("Choose the table to add a new record to: \n 1. Sales \n 2. Customers \n 3. Parts \n Your choice:")
        if new_record_query == "1":
            add_new_record(1)
        elif new_record_query == "2":
            add_new_record(2)
        elif new_record_query == "3":
            add_new_record(3)
        else:
            print("Invalid choice")
            logged_in_app()
            return            
    elif choice == "5":
        exit_func()
    else:
        print("Invalid choice")
        logged_in_app()
        return
    


def view(type):
    if type == "sales":
        app_border("Sales")
        data = pd.read_csv("./database/Sales.csv")
        print(data)
        logged_in_app()
    elif type == "customers":
        app_border("Customers")
        data = pd.read_csv("./database/Customers.csv")
        print(data)
        logged_in_app()
    elif type == "parts":
        app_border("Parts")
        data = pd.read_csv("./database/Parts.csv")
        print(data)
        logged_in_app()
        

def add_new_record(option):
    if option == 1:
        # open sales.csv and append new record
        app_border("Add New Sale Record")
        new_record = {
            "customer_email": input("Customer Email: "),
            "part_cost": input("Part Cost: "),
            "lead_cost": input("Lead Cost: "),
            "sales_cost": input("Sales Cost: "),
            "profit": input("Profit: ")
        }
        
        # append to csv
        sales = pd.read_csv("./database/Sales.csv")
        customers = pd.read_csv("./database/Customers.csv")
        if new_record["customer_email"] not in customers["email"].values:
            print("Customer not found")
            sales = sales.append(new_record, ignore_index=True)
            sales.to_csv("./database/Sales.csv", index=False)
            app_border("Sale record added successfully")
            add_new_record(2)
            logged_in_app()
        else:
            sales = sales.append(new_record, ignore_index=True)
            sales.to_csv("./database/Sales.csv", index=False)
            app_border("Sale record added successfully")
            logged_in_app()
        
    elif option == 2:
        # open customers.csv and append new record: 
        # full_name,email,phone_number,unit,part_purchased,part_id
        app_border("Add New Customer")
        new_record = {
            "full_name": input("Full Name: "),
            "email": input("Email: "),
            "phone_number": input("Phone: "),
            "unit": input("Unit: "),
            "part_purchased": input("Part Purchased: "),
            "part_id": input("Part ID: ")
        }
        
        parts = pd.read_csv("./database/Parts.csv")
        
        if new_record["part_id"] not in parts["part_id"].values:
            print("Part not in database")
            # append to csv
            customers = pd.read_csv("./database/Customers.csv")
            customers = customers.append(new_record, ignore_index=True)
            customers.to_csv("./database/Customers.csv", index=False)
            app_border("Customer added successfully")
            add_new_record(3)
            logged_in_app()
        else:
            # append to csv
            customers = pd.read_csv("./database/Customers.csv")
            customers = customers.append(new_record, ignore_index=True)
            customers.to_csv("./database/Customers.csv", index=False)
            app_border("Customer added successfully")
            logged_in_app()
            
        
        
    elif option == 3:
        # open parts.csv and append new record
        app_border("Add New Part")
        new_record = {
            "part_id": input("Part ID: "),
            "name": input("Part Name: "),
            "source": input("Part Source: "),
            "brand": input("Part Brand: "),
            "cost": input("Cost: ")
        }
        
        
        # append to csv
        parts = pd.read_csv("./database/Parts.csv")
        parts = parts.append(new_record, ignore_index=True)
        parts.to_csv("./database/Parts.csv", index=False)
        app_border("Part added successfully")
        logged_in_app()
        
    else:
        print("Invalid option")
        logged_in_app()
        
        
hello()

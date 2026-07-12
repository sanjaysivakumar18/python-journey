def welcome():
    print("\n🍽️ Welcome to Sanjay's Restaurant")
def menu():
    print("\n------ MENU ------")
    print("1. Burger  - ₹120")
    print("2. Pizza   - ₹250")
    print("3. Pasta   - ₹180")
    print("4. Juice   - ₹80")
    print("------------------")
    
def special():
    print("\n Todays special")
    print("Paneer tikka pizza-₹299")

def about():
    print("\n----- ABOUT -----")
    print("Owner   : Sanjay")
    print("Location: Coimbatore")
    print("Open    : 9:00 AM - 10:00 PM")

def exit():
    print("\n🙏 Thank you for visiting!")
    print("Have a great day!")
    
welcome()
while True:
    print("\n==Main Menu==")
    print("1.Menu")
    print("2.Special")
    print("3.About")
    print("4.Exit")
    
    choice=int(input("Enter your choice : "))
    if choice==1:
        menu()
    elif choice==2:
        special()
    elif choice==3:
        about()
    elif choice==4:
        exit()
    else:
        print("Invalid Choice")
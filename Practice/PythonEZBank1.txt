#Aden Davis
#EZBank1
import basics

app = basics.newProgram()

user = basics.newUser

app.currentBalance = 1000

while app.running:
    user.choice = input("1 (deposit), 2 (withdraw), 3 (quit), or 4 (check balance)")
    if user.choice == "1":
        user.deposit = input("How much to deposit?")
        user.deposit = int(user.deposit)
        app.currentBalance = app.currentBalance + user.deposit
                
    elif user.choice == "2":
        user.withdraw = input("How much to withdraw?")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.currentBalance:
            print("You don't have enough money.")
        else:
            app.currentBalance = app.currentBalance - user.withdraw
            
    elif user.choice == "3":
        app.running = False

    elif user.choice == "4":
        print(app.currentBalance)

    else:
        print("Invalid choice!")

import sys
from colorama import Fore
import entities.order as orderent
import entities.user as userent
import entities.part as partent
import services.authenticationhandler as authenticationserv
import services.partshandler as partsserv
import services.deletehandler as deleterserv

print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep="")

authentication = authenticationserv.Authentication()
partshandler = partsserv.PartsHandler()
cart = []
total_price = 0

while(True):
    action = input("What would you like to do? ")
    if(action != "login" and action != "register" and action != "exit"):
        print(Fore.RED, "Invalid option entered. Please try again.", Fore.RESET)
        continue
    elif(action == "exit"): sys.exit()
    else: break

if(action == "login"):
    current_user = authentication.login()
    while(current_user == None): 
        print(Fore.RED, "Invalid credentials. Please try again.", Fore.RESET)
        current_user = authentication.login()
    print(Fore.GREEN,"Credentials authenticated. Login successful!" + Fore.RESET,"")
elif(action == "register"):
    username, password, admin = authentication.register()
    current_user = userent.User(username, password, admin)

print("\n----------------------------------------\nWelcome to the computer store, " + Fore.YELLOW,current_user.name + Fore.RESET,"!\n----------------------------------------\n", sep="")

while(True):
    print("\nHere are your options:\n-" + Fore.CYAN,"add" + Fore.RESET, "to add a part to your cart.\n-" +
      Fore.CYAN,"delete" + Fore.RESET,"to remove an item from your cart.\n-" +
      Fore.CYAN,"cart" + Fore.RESET,"to view your current cart.\n-" +
      Fore.CYAN,"orders" + Fore.RESET,"to view your order history.\n-" +
      Fore.CYAN,"admin" + Fore.RESET,"to access the admin dashboard.\n-" +
      Fore.CYAN,"exit" + Fore.RESET,"to cancel and exit the store.")
    action = input("What would you like to do? ")
    if(action == "add"): 
        part = partshandler.add()
        cart.append(part)
        total_price += part['price']
    elif(action == "delete"):
        print(Fore.YELLOW,current_user.name + Fore.RESET,"'s cart:\n", sep="")
        for part in cart:
            print("Brand: " + part['brand'] + " | " + "Model:" + Fore.CYAN,part['model'] + Fore.RESET,"| " + "Type: " + part['type'] + " | " + "Price: " + str(part['price']))
        cart = deleterserv.delete(cart)
        total_price -= part['price']
    elif(action == "cart"):
        print(Fore.YELLOW,current_user.name + Fore.RESET,"'s cart:\n", sep="")
        if(len(cart) == 0):
            print(Fore.RED,"Cart is currently empty." + Fore.RESET,"")
        else:
            for part in cart:
                print("Brand: " + part['brand'] + " | " + "Model: " + part['model'] + " | " + "Type: " + part['type'] + " | " + "Price: " + str(part['price']))
            print("\nYour total price is: " + str(total_price))
    elif(action == "orders"):
        print(Fore.YELLOW,current_user.name + Fore.RESET,"'s order history:\n", sep="")
    elif(action == "admin"):
        print("admin")
    elif(action == "exit"):
        sys.exit()
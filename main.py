import sys
from colorama import Fore
import entities.order as orderent
import entities.user as userent
import entities.part as partent
import services.authenticationhandler as authenticationserv
import services.partshandler as partsserv
import services.deletehandler as deleterserv
import services.ordershandler as ordersserv
import services.checkouthandler as checkoutserv
import services.adminhandler as adminsserv

def main():

    print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep="")

    authentication = authenticationserv.Authentication()
    partshandler = partsserv.PartsHandler()
    ordershandler = ordersserv.OrdersHandler()
    checkouthandler = checkoutserv.CheckoutHandler()
    cart = []
    total_price = 0

    while(True):
        action = input("What would you like to do? ")
        if(action != "login" and action != "register" and action != "exit"):
            print(Fore.RED, "Invalid option entered. Please try again.", Fore.RESET)
            continue
        elif(action == "exit"): 
            print(Fore.GREEN,"Goodbye!" + Fore.RESET,"")
            sys.exit()
        else: break

    if(action == "login"):
        current_user = authentication.login()
        while(current_user == None): 
            print(Fore.RED, "Invalid credentials. Please try again.", Fore.RESET)
            current_user = authentication.login()
        print(Fore.GREEN,"Credentials authenticated. Login successful!" + Fore.RESET,"")
    elif(action == "register"):
        username, password, admin = authentication.register()
        current_user = userent.User(username, password, int(admin))

    print("\n----------------------------------------\nWelcome to the computer store, " + Fore.YELLOW,current_user.name + Fore.RESET,"!\n----------------------------------------\n", sep="")

    while(True):
        print("\nHere are your options:\n-" + Fore.CYAN,"add" + Fore.RESET, "to add a part to your cart.\n-" +
        Fore.CYAN,"delete" + Fore.RESET,"to remove an item from your cart.\n-" +
        Fore.CYAN,"cart" + Fore.RESET,"to view your current cart.\n-" +
        Fore.CYAN,"checkout" + Fore.RESET,"to finalize and checkout your order.\n-" +
        Fore.CYAN,"orders" + Fore.RESET,"to view your order history.\n-" +
        Fore.CYAN,"admin" + Fore.RESET,"to access the admin dashboard.\n-" +
        Fore.CYAN,"exit" + Fore.RESET,"to cancel and exit the store.\n")
        action = input("What would you like to do? ")

        if(action == "add"): 
            part = partshandler.add()
            cart.append(part)
            total_price += part['price']

        elif(action == "delete"):
            print(Fore.YELLOW,current_user.name + Fore.RESET,"'s cart:\n", sep="")
            if(len(cart) == 0):
                print(Fore.RED,"Cart is already empty!", Fore.RESET,"")
            else:
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

        elif(action == "checkout"):
            if(len(cart) == 0):
                print(Fore.RED,"You can't checkout with an empty cart!" + Fore.RESET,"")
            else:
                checkouthandler.checkout(cart, current_user.name, total_price)
                cart = []
                total_price = 0


        elif(action == "orders"):
            print(Fore.YELLOW,current_user.name + Fore.RESET,"'s order history:\n", sep="")
            ordershandler.history(current_user.name)

        elif(action == "admin"):
            if(current_user.admin == 0):
                print(Fore.RED,"You do not have administrator privileges." + Fore.RESET,"")
            elif(current_user.admin == 1):
                print("\n----------------------------------------\nWelcome to admin dashboard, " + Fore.YELLOW,current_user.name + Fore.RESET,"!\n----------------------------------------\n", sep="")
                while(True):
                    print("\nAdmin options:\n-" + Fore.CYAN,"modify" + Fore.RESET, "to change the price of an item in the store's inventory.\n-" +
                    Fore.CYAN,"remove" + Fore.RESET,"to remove a user and their associated orders from the database.\n-" +
                    Fore.CYAN,"close" + Fore.RESET,"to close the admin dashboard and return to the main menu.\n")
                    action = input("What would you like to do? ")

                    if(action == "modify"):
                        print("hi")
            
        elif(action == "exit"):
            print(Fore.GREEN,"Goodbye, thanks for shopping with us." + Fore.RESET,"")
            sys.exit()

        else: print(Fore.RED,"Invalid option entered. Please try again.", Fore.RESET,"")

if __name__ == "__main__":
    main()
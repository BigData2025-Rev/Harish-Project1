from colorama import Fore
import entities.order as orderent
import entities.user as userent
import entities.part as partent
import services.authentication as authenticationserv
import services.partshandler as partsserv

print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep="")

authentication = authenticationserv.Authentication()
partshandler = partsserv.PartsHandler()

while(True):
    action = input("What would you like to do? ")
    if(action != "login" and action != "register"):
        print(Fore.RED, "Invalid option entered. Please try again.", Fore.RESET)
        continue
    else: break

if(action == "login"):
    result = authentication.login()
    while(result == None): 
        print(Fore.RED, "Invalid credentials. Please try again.", Fore.RESET)
        result = authentication.login()
    current_user = userent.User(result['name'], result['password'], result['admin'])
    print(Fore.GREEN,"Credentials authenticated. Login successful!" + Fore.RESET,"")
elif(action == "register"):
    username, password, admin = authentication.register()
    current_user = userent.User(username, password, admin)

print("\n----------------------------------------\nWelcome to the computer store, " + Fore.YELLOW,current_user.name + Fore.RESET,"!\n----------------------------------------\n", sep="")
print("Here are your options:\n-" + Fore.CYAN,"add" + Fore.RESET, "to add a part to your order.\n-" +
      Fore.CYAN,"delete" + Fore.RESET,"to delete an item from your order.\n-" +
      Fore.CYAN,"orders" + Fore.RESET,"to view your order history.\n-" +
      Fore.CYAN,"admin" + Fore.RESET,"to access the admin dashboard.")

action = input("What would you like to do? ")

if(action == "add"): 
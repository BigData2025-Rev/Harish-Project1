from colorama import Fore
import entities.order as orderent
import entities.user as userent
import entities.part as partent
import services.authentication as authenticationserv

print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep="")

authentication = authenticationserv.Authentication()

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
elif(action == "register"):
    username, password, admin = authentication.register()
    current_user = userent.User(username, password, admin)

print("The user's name is " + current_user.name + " and their password is " + current_user.password + " and admin " + str(current_user.admin))




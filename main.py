from colorama import Fore
import entities.user as User
import entities.order as Order
import entities.part as Part
import services.authentication as authentication

print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep='')

while(True):
    action = input("What would you like to do? ")
    if(action != "login" and action != "register"):
        print(Fore.RED, "Invalid option entered. Please try again.", Fore.RESET)
        continue
    else: break

if(action == "login"): user = authentication.login()
elif(action == "register"): user = authentication.register()




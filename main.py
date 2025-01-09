from colorama import Fore
import authentication

print("\n\nWelcome to the Computer Store!\nFirst, you'll need to" + Fore.CYAN," login " + Fore.RESET,"or" + Fore.CYAN," register" + Fore.RESET,".", sep='')

while(True):
    action = input("What would you like to do? ")
    if(action != "login" and action != "register"):
        print(Fore.RED, "Invalid option entered. Please try again.", Fore.RESET)
        continue
    else: break

if(action == "login"): username = Authentication.login()
elif(action == "register"): username = Authentication.register()




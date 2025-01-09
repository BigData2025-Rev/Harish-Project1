from colorama import Fore

def delete(cart):
    if(len(cart) == 0):
        print(Fore.RED,"Cart is already empty!", Fore.RESET,"")
        return cart
    model = input("\nWhich part would you like to remove? ")
    flag = True
    while(flag):
        for part in cart:
            if(part['model'] == model):
                cart.remove(part)
                flag = False
        if flag:
            print(Fore.RED,"Invalid model specified. Please try again." + Fore.RESET,"")
            model = input("Which part would you like to remove? ")
    print(Fore.GREEN,"Part successfully removed!" + Fore.RESET,"")
    return cart
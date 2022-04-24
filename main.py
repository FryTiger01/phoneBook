import pyfiglet
from colorama import Fore

book = {}
print(pyfiglet.figlet_format("Phone Book"))
print("choose a option")
while True:
    print(Fore.WHITE + "1) Add Contact\n2) Delete Contact\n3) view\n4) Help\n5) Exit")
    inputi = input("Choose :  ")
    if inputi == "1":
        name = input(Fore.MAGENTA + "Enter a name : ")
        phone = input(Fore.MAGENTA + "Enter a PHone : ")  # no handle string input
        book[name] = phone
    elif inputi == "2":
        named = input(Fore.YELLOW + "Enter a name : ")
        del book[named]
    elif inputi == "3":
        for k, v in book.items():
            print(Fore.BLUE + k, ":", v)
    elif inputi == "4":
        print(Fore.CYAN + "1) To add Contact\n2) delete Contact\n3) view Contact\n)5 Exit app")
    elif inputi == "5":
        break
    else:
        print(Fore.RED + "Invalid Choose!")

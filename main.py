from PIL import Image as img
from colorama import Fore, Back, init

init() # init with colorama


try:
    print(Fore.GREEN + Back.MAGENTA, end="")
    ico = img.open(input(
        "Enter filename: "
    ))

    print(Fore.MAGENTA + Back.CYAN, end="")
    ico.save(input(
        "Enter new name: "
    ))
    input()

except Exception as ex:
    print(Fore.BLACK + Back.RED, end="")
    print(f"Oops, error: \"{ex}\"")
    input()

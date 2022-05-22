from PIL import Image as img
from colorama import Fore, Back, init

init()


try:
    ico = img.open(input(f"{Fore.GREEN}{Back.MAGENTA}Enter filename: "))

    ico.save(input(f"{Fore.MAGENTA}{Back.CYAN}Enter new name: "))

except Exception as ex:
    print(f"{Fore.BLACK}{Back.RED}Oops, error: \"{ex}\"")

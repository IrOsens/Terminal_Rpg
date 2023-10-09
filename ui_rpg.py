from attributes import *
from colorama import Fore, Back, Style, init
init()

def progression(max, rmn):
    max_split = max / 20
    bar_lost = int(rmn / max_split)
    bar = "█"
    progress = bar * (20 - bar_lost)
    bar_value_rmn = max - rmn
    progress_lost = progress + Style.BRIGHT + Fore.RED + bar * bar_lost + Fore.RESET + Style.RESET_ALL + f' {bar_value_rmn}/{max}'
    return progress_lost

#Skeleton.visual().idle()
#Slime.visual().idle()
#print(progression(Skeleton.hp,0))
#input1 = int(input('Serang= '))
#print(progression(Slime.hp, input1))

   















# Inisialisasi colorama 


# Mencetak teks berwarna
#print(Style.BRIGHT+Fore.RED + '███████████████' + Fore.RESET+Style.RESET_ALL)
#print(Back.GREEN + 'Latar Belakang Hijau' + Back.RESET)
#print(Style.BRIGHT + 'Teks Terang' + Style.RESET_ALL)

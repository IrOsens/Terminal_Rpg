import inspect
from attributes import *
import random
'''
attributes_module = inspect.getmodule(attributes)
atribut_modul = inspect.getmembers(attributes_module, inspect.isclass)

list_of_class_names = []

for nama, kelas in atribut_modul:
    list_of_class_names.append(nama)

print(list_of_class_names)

import inspect

# Mendapatkan modul atribut
attributes_module = inspect.getmodule(inspect.currentframe())

# Mendapatkan daftar kelas dari modul (misalnya, Anda ingin menghindari kelas "player")
class_list = [cls for name, cls in inspect.getmembers(attributes_module, inspect.isclass) if name != "player"]

# Memilih dan membuat objek dari kelas yang dipilih
monster_instance = random.choice(class_list)()

# Mengakses atribut hp dari objek
x = monster_instance.hp

print(f"Nama kelas monster yang dipilih: {monster_instance.__class__.__name__}")
print(f"HP monster yang dipilih: {x}")'''

def get_random_monster_instance():
    # Mendapatkan modul atribut
    attributes_module = inspect.getmodule(inspect.currentframe())

    # Mendapatkan daftar kelas dari modul (misalnya, Anda ingin menghindari kelas "player")
    class_list = [cls for name, cls in inspect.getmembers(attributes_module, inspect.isclass) if name != "player"]

    # Memilih dan membuat objek dari kelas yang dipilih
    monster_picker = random.choice(class_list)()
    
    return monster_picker
monster = get_random_monster_instance()
print(monster.__class__.__name__)
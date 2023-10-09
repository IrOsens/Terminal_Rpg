import os
import random
import keyboard
import inspect
from ui_rpg import progression
from attributes import *
from colorama import Fore, Back, Style, init
init()

# Fungsi untuk membersihkan terminal
def clear_terminal():
    os.system('cls')

def get_random_monster_instance():
    # Mendapatkan modul atribut
    attributes_module = inspect.getmodule(inspect.currentframe())

    # Mendapatkan daftar kelas dari modul (misalnya, Anda ingin menghindari kelas "player")
    class_list = [cls for name, cls in inspect.getmembers(attributes_module, inspect.isclass) if name != "player"]

    # Memilih dan membuat objek dari kelas yang dipilih
    monster_picker = random.choice(class_list)()
    
    return monster_picker

# Contoh penggunaan fungsi
monster_picker = get_random_monster_instance()

class RPGGame:
    def __init__(self):
        self.player_hp = Player.hp
        self.monster = monster_picker
        self.is_player_alive = True
        self.monster_name = self.monster.__class__.__name__

    def attack(self):
        if self.is_player_alive:
            damage = Player.attack()
            self.monster.hp -= damage
            print(f"Kamu menyerang {self.monster_name} dan menyebabkan {damage} kerusakan pada {self.monster_name}.")

            if self.monster.hp <= 0:
                self.monster.hp = monster_picker.hp
                print(f"{self.monster_name} mati! {self.monster_name} baru muncul.")
        else:
            print("Kamu sudah mati! Game Over.")

    def take_damage(self):
        if self.is_player_alive:
            damage = self.monster.damage
            self.player_hp -= damage
            print(f"{self.monster_name} menyerang kamu dan menyebabkan {damage} kerusakan pada kamu.")

            if self.player_hp <= 0:
                self.is_player_alive = False
                print("Kamu mati! Game Over.")
        else:
            print("Kamu sudah mati! Game Over.")

    def play(self):
        while self.is_player_alive:
            keyboard.wait("enter")  # Menunggu tombol Enter ditekan
            self.attack()
            self.take_damage()

if __name__ == "__main__":
    game = RPGGame()
    print(f"Selamat datang di Game RPG !")
    game.play()
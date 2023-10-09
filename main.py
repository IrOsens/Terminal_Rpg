import os
def clear_terminal():
    os.system('cls')
clear_terminal()
import keyboard
import inspect
from ui_rpg import progression
from attributes import *
from colorama import Fore, Back, Style, init
init()

#list monster
# Mendapatkan modul atribut
attributes_module = inspect.getmodule(inspect.currentframe())
# Mendapatkan daftar kelas dari modul (misalnya, Anda ingin menghindari kelas "player")
class_list = [cls for name, cls in inspect.getmembers(attributes_module, inspect.isclass) if name != "player"]
# Memilih dan membuat objek dari kelas yang dipilih
monster_picker = random.choice(class_list)()
# Mengakses atribut hp dari objek
x = monster_picker.hp

class RPGGame:
    def __init__(self):
        self.player_hp = Player.hp
        self.slime_hp = Slime.hp
        self.is_player_alive = True

    def attack(self):
        if self.is_player_alive:
            damage = Player.attack()
            self.slime_hp -= damage
            print(f"Kamu menyerang Slime dan menyebabkan {damage} kerusakan pada Slime.")
            
            if self.slime_hp <= 0:
                self.slime_hp = Slime.hp
                print("Slime mati! Slime baru muncul.")
        else:
            print("Kamu sudah mati! Game Over.")

    def take_damage(self):
        if self.is_player_alive:
            damage = Slime.damage
            self.player_hp -= damage
            print(f"Slime menyerang kamu dan menyebabkan {damage} kerusakan pada kamu.")
            
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
    print("Selamat datang di Game RPG Slime!")
    game.play()


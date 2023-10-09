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
    class_list = [cls for name, cls in inspect.getmembers(attributes_module, inspect.isclass) if name != "player" and name != "RPGGame" ]

    # Memilih dan membuat objek dari kelas yang dipilih
    monster_picker = random.choice(class_list)()
    
    return monster_picker

# Contoh penggunaan fungsi
monster_picker = get_random_monster_instance()

class RPGGame:
    def __init__(self):
        self.player_hp = Player.hp
        self.is_player_alive = True
        self.monster_class = None  # Awalnya belum memilih kelas monster
        self.monster = None
        self.monster_name = None


    def choose_monster(self):
        self.monster_class = get_random_monster_instance()  # Memilih kelas monster
        self.monster_name = self.monster_class.__class__.__name__
        self.monster = self.monster_class
        self.full_hp = self.monster.hp
    def attack(self):
        if self.is_player_alive:
            #self.monster = self.monster_class  # Membuat instance dari kelas monster yang dipilih
            damage = Player.attack()
            self.monster.hp = self.monster.hp -  damage
            clear_terminal()  # Membersihkan terminal sebelum mencetak pesan baru
            rmn = self.full_hp - self.monster.hp  # Menghitung berapa banyak HP yang telah dikurangi
            max_hp = self.full_hp  # HP awal monster
            self.monster.visual().idle()
            print(progression(max_hp, rmn))  # Menampilkan progres
            print(f"Kamu menyerang {self.monster_name} dan menyebabkan {damage} kerusakan pada {self.monster_name}.")

            if self.monster.hp <= 0:
                print(f"{self.monster_name} mati! {self.monster_name} baru muncul.")
                self.choose_monster()  # Memilih kelas monster baru setelah yang lama mati
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
        self.choose_monster()  # Memilih monster pertama kali
        while self.is_player_alive:
            keyboard.wait("enter")  # Menunggu tombol Enter ditekan
            self.attack()
            self.take_damage()

if __name__ == "__main__":
    game = RPGGame()
    print(f"Selamat datang di Game RPG !")
    game.play()


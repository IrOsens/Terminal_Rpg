import random
class player:
    def __init__(self):
        self.hp = 90000
        self.damage= 15
        self.crit_rate= 20
        self.crit_damage= 200
    def attack(self):
        result_cdm= int(self.damage * (self.crit_damage/100))
        damage_list = [self.damage,result_cdm]
        result_cr= float(self.crit_rate/100)
        result_ncr= 1- result_cr
        chance = [result_ncr,result_cr]
        return random.choices(damage_list,weights=chance)[0]

class slime:
    def __init__(self):
        self.hp=70
        self.damage= 10
    class visual:
        def idle(self):
            return print("""
       ****           / \\
   **        **      |  |
 *              *  _|  |
*     █      █   * \\ \\|
*                * /\\_\\
 * ___________  *
""")
        

class skeleton:
    def __init__(self):
        self.hp= 150
        self.damage= 30
    class visual:
        def idle(self):
            return print('''
                      ______
                   .-"      "-.
                  /            \\
                 |              |
                 |,  .-.  .-.  ,|
                 | )(__/  \\__)( |
                 |/     /\\     \\|
       (@_       (_     ^^     _)
  _     ) \\_______\\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>
        )_/        \\          /
       (@           `--------`
''')

Player = player()
Plyr_att = Player.attack
Slime = slime()
Skeleton = skeleton()
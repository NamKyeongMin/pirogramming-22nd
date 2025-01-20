class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def slash(self):
        print("베기")

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        self.ability_power = (self.ability_power*0.65) + 400
        print("티버: 피해량 {0}".format(self.ability_power))

health, mana, ability_power = map(float, input().split())
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
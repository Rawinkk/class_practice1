class StatusMonster:
    def __init__(self,atk,defense,HP,CRI,status = 'Normal'):
        self.atk = atk
        self.defense = defense
        self.HP = HP
        self.CRI = CRI
        self.status = status
    def attack(self,enemy):
        ResistCRI = 50
        if enemy.HP > 0 and self.HP > 0:
            if self.CRI > ResistCRI:
                enemy.HP = max(0,enemy.HP - max(0,(self.atk*1.5) - enemy.defense))
                print('Critical Hit!')
            else:
                enemy.HP = max(0,enemy.HP - max(0, self.atk - enemy.defense))
        if enemy.HP == 0:                   
            print("Enemy died")
    def effect(self):
        import random
        if random.random() > 0.75:
            self.status = 'Freeze'
            print(self.status)
        elif random.random() > 0.65:
            self.status = 'Stun'
            print(self.status)
        elif random.random() > 0.55:
            self.status = 'Knock Back'
            print(self.status)

Mage = StatusMonster(100,50,80,52)
Poring = StatusMonster(60,80,100,20)
print('=== Before Attack ===')
print('Mage HP =', Mage.HP)  
print('Poring HP =', Poring.HP)
print('===Effect status===')
Poring.effect()
Mage.effect()
Mage.attack(Poring)
Poring.attack(Mage)
print('=== After Attack ===')
print('Mage HP =', Mage.HP)  
print('Poring HP =', Poring.HP)
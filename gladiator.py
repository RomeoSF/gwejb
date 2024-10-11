import random

# Olika karaktärer i spelet

class Karaktärer:
    def __init__(self, namn, hälsa):
        self.namn = namn
        self.hälsa = hälsa
        
karaktär1 = Karaktärer("Jöns", 100)

# Olika attacker i spelet

attack = []

class Attacker:
    def __init__(self, namn, skada):
        self.skada = skada
        self.namn = namn
        attack.append(self)

jabb = Attacker("jabb", 10)
spark = Attacker("spark", 15)

# Fiendens hälsa

fie_hälsa = 100

# Funktion för spelarens attack
def din_att():
    global fie_hälsa
    while True:
        att_val = input("Välj din attack: ")
        giltig_attack = None
        # Kollar så att svaret är gitligt
        for att in attack:
            if att_val.lower() == att.namn.lower():
                giltig_attack = att
                break
        if giltig_attack:
            attack_namn = giltig_attack.namn
            attack_skada = giltig_attack.skada
            break
        else:
            print("Ogitligt svar, försök igen")
    if karaktär1.hälsa and fie_hälsa > 0:
        fie_hälsa -= attack_skada

    
    
        

    
    


#   Funktion för fiendens attack

def fiende_att():
    fie_att = random.choice(attack)
  


#fiende_att()
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

# Svårighetsgrader

lätt = 0.75

normal = 1

svår = 1.25

vedervärdigt = 1.5

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
            pl_attack_namn = giltig_attack.namn
            pl_attack_skada = giltig_attack.skada
            break
        else:
            print("Ogitligt svar, försök igen")
    if karaktär1.hälsa and fie_hälsa > 0:
        fie_hälsa -= pl_attack_skada
        print(f"Du valde: {pl_attack_namn}")
        
#   Funktion för fiendens attack

def fiende_att():
    while True:
        fie_att = random.choice(attack)
        fie_attack_namn = fie_att.namn
        fie_attack_skada = fie_att.skada
        break
    if karaktär1.hälsa and fie_hälsa > 0:
         karaktär1.hälsa -= fie_attack_skada
         print(f"Fienden valde: {fie_attack_namn}")
    

# Funktion för att köra spelet

def spela():
    while karaktär1.hälsa and fie_hälsa > 0:
        print("-----------------------")
        print(f"Fiendens hälsa: {fie_hälsa}HP")
        print(f"Din hälsa: {karaktär1.hälsa}HP")
        din_att()
        fiende_att()
        if karaktär1.hälsa < 0:
            print("-----------------------")
            print("Du förlora!")
            exit()
        elif fie_hälsa < 0:
            print("-----------------------")
            print("Du vann!")
            exit()
        
# Spelare väljer svårighetsgrad

while True:
    print("-----------------------")
    svårhetsgrad = input("Vilken svårighetsgrad vill du använda?\nLätt\nNormal\nSvår\nVedervärdigt\n")
    if svårhetsgrad.lower() == "lätt":
        fie_hälsa *= lätt
        break
    elif svårhetsgrad.lower() == "normal":
        fie_hälsa *= normal
        break
    elif svårhetsgrad.lower() == "svår":
        fie_hälsa *= svår
        break
    elif svårhetsgrad.lower() == "vedervärdigt":
        fie_hälsa *= vedervärdigt
        break
    else:
        print("-----------------------")
        print("Ogitligt svar")

spela()
class Karaktärer:
    def __init__(self, namn, hälsa):
        self.namn = namn
        self.hälsa = hälsa
        
karaktär1 = Karaktärer("Jöns", 100)

attack = []

class Attacker:
    def __init__(self, namn, skada):
        self.skada = skada
        self.namn = namn
        attack.append(self)

jabb = Attacker("jabb", 10)
spark = Attacker("spark", 15)


# Spel funktion för att spelare ska attackera

def din_att():
    att_val = input("Välj din attack: ")
    giltig_attack = None
    # Kolla attacker i attack lista
    for att in attack:
        if att_val.lower() == att.namn.lower():
            giltig_attack = att
            break
    if giltig_attack:
        print(f"Du valde {att.namn}")

din_att()
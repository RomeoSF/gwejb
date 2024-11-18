import random

# Olika karaktärer i spelet

class Karaktärer:
    def __init__(self, namn, hälsa):
        self.namn = namn
        self.hälsa = hälsa
        
karaktär1 = Karaktärer("Jöns", 100,)

# Antalet mod poäng spelaren har

kar_modP = 0

# Olika attacker i spelet

attack = []

class Attacker: 
    def __init__(self, namn, skada, träff_chans, besk):
        self.skada = skada
        self.namn = namn
        self.träff_chans = träff_chans
        self.besk = besk
        attack.append(self)

jabb = Attacker("jabb", 10, 85, "En snabb och pålitlig attack som är lätt att träffa med. Ger 5 modighetspoäng.")

spark = Attacker("spark", 15, 70, "En kraftfullare attack med medelhög träffchans. Ger 8 modighetspoäng.")

tung_spark = Attacker ("tung spark", 20, 55, "Den mest kraftfulla attacken, men svårare att träffa med. Ger 12 modighetspoäng.")


# Maximal tid för matchen (antal rundor) och Nuvarande tid/rundor

max_tid = 10  

tid = 0  

# Fiendens hälsa

fie_hälsa = 100

# Antalet mod poäng fienden har

fie_modP = 0

# Svårighetsgrader

lätt = 0.75

normal = 1

svår = 1.25

vedervärdigt = 1.5

# Funktion för spelarens attack
def din_att():
    global fie_hälsa
    global kar_modP
    global tid

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
            pl_attack_träffCH = giltig_attack.träff_chans
            break
        else:
            print("Ogitligt svar, försök igen")
    if karaktär1.hälsa and fie_hälsa > 0:
        if random.randint(1, 100) < pl_attack_träffCH:
            fie_hälsa -= pl_attack_skada
            print(f"Du valde: {pl_attack_namn}")
            if pl_attack_namn == "jabb":
                kar_modP = kar_modP + 5
            elif pl_attack_namn == "spark":
                kar_modP = kar_modP + 8
            elif pl_attack_namn == "tung spark":
                kar_modP = kar_modP + 12
        else:
            print("Du missade!")
    # Öka tiden efter varje attack
    tid += 1  
    
#   Funktion för fiendens attack

def fiende_att():
    global fie_modP
    global karaktär1

    while True:
        fie_att = random.choice(attack)
        fie_attack_namn = fie_att.namn
        fie_attack_skada = fie_att.skada
        fie_attack_träffCH = fie_att.träff_chans
        break
    if karaktär1.hälsa and fie_hälsa > 0:
        if random.randint(1, 100) < fie_attack_träffCH:
            karaktär1.hälsa -= fie_attack_skada
            print(f"Fienden valde: {fie_attack_namn}")
            if fie_attack_namn == "jabb":
                fie_modP = fie_modP + 5
            elif fie_attack_namn == "spark":
                fie_modP = fie_modP + 8
            elif fie_attack_namn == "tung spark":
                fie_modP = fie_modP + 12
        else:
            print("Fienden missade!")


# Funktion för att visa attackbeskrivningar
def visa_attacker():
    print("\nTillgängliga attacker:")
    print("-----------------------")
    for att in attack:
        print(f"{att.namn.title()}:")
        print(f"Skada: {att.skada}")
        print(f"Träffchans: {att.träff_chans}%")
        print(f"Beskrivning: {att.besk}")
        print("-----------------------")
    

# Funktion för att avgöra vinnare vid oavgjort
def avgör_vinnare():
    print("-----------------------")
    print("Matchen är slut!")
    print(f"Din modighet: {kar_modP}")
    print(f"Fiendens modighet: {fie_modP}")
    
    if kar_modP > fie_modP:
        print("Du vinner på modighet!")
    elif fie_modP > kar_modP:
        print("Fienden vinner på modighet!")
    else:
        print("Fullständigt oavgjort!")

# Funktion för att köra spelet

def spela():
    visa_attacker()
    global tid
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
        # Om tiden är slut eller båda fortfarande lever
        elif tid >= max_tid:
            avgör_vinnare()
            break



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

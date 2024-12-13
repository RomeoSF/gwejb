# Rymdfängelseflykten

def cell_room():
    """Startrum - fängelcellen."""
    print("\n--- FÄNGELSECELL ---")
    print("Du vaknar upp i en trång, metallisk cell ombord på rymdstationen Blackstar.")
    print("Väggarna är täckta av elektroniska lås och säkerhetsskärmar.")
    print("Du vet att du måste fly innan nästa säkerhetskontroll.")
    
    while True:
        print("\nVad vill du göra?")
        print("1. Undersök sängbädden")
        print("2. Kontrollera celldörren")
        print("3. Se dig omkring i cellen")
        
        val = input("Ange ditt val (1-3): ")
        
        # Lägg till skit till valen


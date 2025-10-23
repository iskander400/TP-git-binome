def calculer_moyenne(notes):
   
    return sum(notes) / len(notes)

def afficher_resultat(moyenne):
  
    print(f"Moyenne = {moyenne:.2f}")

# Programme principal
notes = [12, 15, 18, 10, 14]
print("Notes:", notes)
moyenne = calculer_moyenne(notes)
afficher_resultat(moyenne)
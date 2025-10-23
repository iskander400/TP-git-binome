def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total = total + note
    return total / len(notes)

def afficher_resultat(moyenne):
  
    print("La moyenne est:", moyenne)

Programme principal
notes = [12, 15, 18, 10, 14]
print("Notes:", notes)
moyenne = calculer_moyenne(notes)
afficher_resultat(moyenne)
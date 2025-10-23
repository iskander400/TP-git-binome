def calculer_moyenne(notes):
    # On garde la version d'Iskander
    return sum(notes) / len(notes)

def afficher_resultat(moyenne):
    # On garde la version de Bayane
    print("La moyenne est:", moyenne)

Programme principal
notes = [12, 15, 18, 10, 14]
print("Notes:", notes)
moyenne = calculer_moyenne(notes)
afficher_resultat(moyenne)
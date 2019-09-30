# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

mot_list = texte.split()
mot_a_trouver = "exemple"
index_Test = mot_list.index("exemple")
nbr_occurence = 0

#Nombre d'occurences
nbr_occurence = texte.count(mot_a_trouver)
print("nombre d'occurences = ",nbr_occurence)

#Remplacer "est"
new_text = texte.replace("est", "représente")
print(new_text)
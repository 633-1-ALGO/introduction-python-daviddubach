# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for i in range(1, len(B)):
    key = B[i]
    previous = i -1
    while previous >= 0 and key < B[previous]:
        B[previous+1] = B[previous]
        previous -=1
    B[previous+1] = key

print(B)



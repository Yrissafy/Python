def recherche(caractere,chaine):
    occurence=0
    for i in range(0,len(caractere)):
        occurence+=chaine.count(caractere[i])
    return occurence


print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))
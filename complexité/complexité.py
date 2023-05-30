# Créé par yasser.rissafy, le 30/03/2023 en Python 3.7
"""
from PIL import Image
import time

img=Image.open("phare3.jpg")
largeur,hauteur=img.size
debut = time.time()
#début du traitement

for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        moyenne=(r+v+b)//3
        r = moyenne
        v = moyenne
        b = moyenne
        img.putpixel((x,y),(r,v,b))

#fin du traitement
fin = time.time()
print("taille img \t durée de traitement")
print(largeur*hauteur,"\t",fin-debut)
img.show()
"""

"""
from random import randint

Tableau = [randint(0, 1000) for i in range(1000)]
Tableau.sort(reverse=True)

nb_affectation = 0

for i in range(1,len(Tableau)):

    j=i

    encours=Tableau[i]
    nb_affectation += 1

    while (j>0) and encours<Tableau[j-1]:
        Tableau[j] = Tableau[j-1]
        nb_affectation += 1

        j-=1

    Tableau[j]=encours

print('taille n=',len(Tableau)," nb affectation =",nb_affectation)
"""
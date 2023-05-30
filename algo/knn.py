# Créé par yasser.rissafy, le 28/02/2023 en Python 3.7
def predireClasse(L,classes,k,x):
    voisins=Kvoisins(L,k,x)
    classespossibles = ['C','T','R']
    decompte=[0,0]
    for v in voisins:
        if classes[v]=='C':
            decompte[0] +=1
        else:
            decompte[1] +=1
    if decompte[1]>decompte[0]:
        classeChoisie=classespossibles[1]
    else:
        classeChoisie=classespossibles[0]
    return  classeChoisie
L=[0,1,2,4,6,7,8,]
classes=['R','T','C','C','C','R','R','R']
x=3
k=3
print('classe du nouvel element',predireClasse(L,classes,k,x))


# Créé par YASSER.RISSAFY, le 17/01/2023 en Python 3.7
tableOrigine=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tableCodee=  ['@','8','[','0','3','{','6','#','1','}',':','7','W','Z','*','?','O','%','$','-','V','^','M','+','/','N']
"""

def codage(phraseClair,cle):
    phraseCodee=''



def decodage(phraseCodee):
    phraseCodee=''


cle=3
menu=''
while menu!='q':
    print("------------------------------------------------------------")
    print("1 : Codage d'une phrase")
    print("2 : Décodage d'une phrase")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    if menu=='1':
        phrase=input("votre phrase en clair?")
        print('la phrase code est', codage(phrase,cle))
    elif menu=='2':
        phrase=input("votre phrase codee?")
        print('la phrase decodee est', decodage(phrase,-cle))
"""

def dist_hamming(lapin,satin):
    if max(len(lapin), len(satin)) <=2 or min(len(lapin), len(satin))<=1:
        return dist_hamming(lapin,satin)
    else:
        collect=[]
        for i in range(1,len(lapin)):
            for c in range(1,len(satin)):
                d1=distance(lapin[:i], satin[:c])
                d2=distance(lapin[i:], satin[c:])
                collect.append(d1+d2)
        return min(collect)
print(dist_hamming("lapin","satin"))



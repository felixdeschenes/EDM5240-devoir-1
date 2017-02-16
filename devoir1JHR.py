#coding: utf-8

# 1) Je crée d'abord une liste qui recense les numéros de permis possibles pour les médecins admis entre 1930 et 1999.

liste1 = list(range(30000,100000))
liste1 = [1,2,3] ### Substitution suggérée pour faire un test

# 2) Je crée ensuite une seconde liste qui regroupe les numéros de permis possibles pour les médecins admis entre 2000 et aujourd'hui (2017).
    #2.1) La dernière personne s'étant vue octroyer un permis par le Collège des médecins est Philippe Cossette, le 11 février dernier, mais son numéro (17068) n'est pas le plus élevé.
    # C'est en effet celui de Gabrielle Chabot (17077), obtenu le 9 février, qui est le plus élevé (source: http://www.cmq.org/bottin/nouveaux-membres.aspx?lang=fr&a=6).
    # Puisque ces numéros de permis ne se suivent pas toujours en ordre chronologique, et puisque le présent mandat consiste à trouver «tous les numéros de permis possibles»
    # qui auraient pu être attribués jusqu'à aujourd'hui, alors on considèrera tous les numéros (de 0 à 999), qui auraient pu être attribués en l'an 2017 (17xxx).
    
#liste2 = list(range(0,18000))
#print(liste1,liste2)

# 3) Après avoir essayé cette impression simple, il semble qu'une difficulté survienne: les occurences du chiffre 0 précédant les autres chiffres ne s'affichent pas.
# 4) Je crée donc une boucle qui me permettra de régler ce problème en appliquant individuellement une opération de formatage à chaque donnée de la seconde liste.
    # 4.1) J'ai trouvé l'opération de formatage à appliquer en boucle juste ici, dans ce forum de discussions: http://stackoverflow.com/questions/134934/display-number-with-leading-zeros
# 5) J'imprime la première liste, puis la seconde, formatée correctement.

for liste2 in range(0,18000):
   print(liste1, "{:0>5}".format(liste2))

### Mes commentaires, pour les différencier des tiens, sont précédés de trois «#».

### Script formidablement bien documenté!
### Il ne produit cependant pas le résultat attendu.
### La ligne 23, ci-dessus, affiche tout le contenu de la liste1 (70000 nombres) suivi du numéro de permis auquel on est rendu dans la liste2
### C'est ainsi que ton script affiche 1 260 000 000 nombres, ce qui prend un temps fou!
### Pour vérifier, change le contenu de la liste1 par [1,2,3] comme je le fais dans la ligne 6, ci-dessus.

### En outre, ton script est rigoureusement identique, sauf un caractère, à celui proposé par Jean Balthazard...
### Vos variables ont les mêmes noms, alors que tous les autres étudiants ont des noms différents.
### Tu comprends que j'aie pu avoir une impression de plagiat. J'ai cependant été satisfait par tes explications, en classe.
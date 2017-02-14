#coding: utf-8

# 1) Je crée d'abord une liste qui recense les numéros de permis possibles pour les médecins admis entre 1930 et 1999.

liste1 = list(range(30000,100000))

# 2) Je crée ensuite une seconde liste qui regroupe les numéros de permis possibles pour les médecins admis entre 2000 et aujourd'hui (2017).
    #2.1) La dernière personne s'étant vue octroyer un permis par le Collège des médecins est Philippe Cossette, le 11 février dernier, mais son numéro (17068) n'est pas le plus élevé.
    # C'est en effet celui de Gabrielle Chabot (17077), obtenu le 9 février, qui est le plus élevé (source: http://www.cmq.org/bottin/nouveaux-membres.aspx?lang=fr&a=6).
    # Puisque ces numéros de permis ne se suivent pas toujours en ordre chronologique, et puisque le présent mandat consiste à trouver «tous les numéros de permis possibles»
    # qui auraient pu être attribués jusqu'à aujourd'hui, alors on considèrera tous les numéros (de 0 à 999), qui auraient pu être attribués en l'an 2017 (17xxx).
    
#liste2 = list(range(0,18000))
#print(liste1,liste2)

# 3) Après avoir essayé cette impression simple, il semble qu'une difficulté survienne: les occurances du chiffre 0 précédant les autres chiffres ne s'affichent pas.
# 4) Je crée donc une boucle qui me permettra de régler ce problème en appliquant individuellement une opération de formatage à chaque donnée de la seconde liste.
    # 4.1) J'ai trouvé l'opération de formatage à appliquer en boucle juste ici, dans ce forum de discussions: http://stackoverflow.com/questions/134934/display-number-with-leading-zeros
# 5) J'imprime la première liste, puis la seconde, formatée correctement.

for liste2 in range(0,18000):
   print(liste1, "{:0>5}".format(liste2)) 

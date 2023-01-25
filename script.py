# On utilise donc la fonction sorted avec en paramètre la liste des données (clé + valeurs) de l'objet dict (la fonction items() de l'objet dict) et en clé de tri, une fonction lambda indiquant l'indice à utiliser pour le tri.
# reverse = true pour l'orde décroissant
# L'indice '0' (zéro) indique la clé de l'objet dict.
# Pour un tri suivant les valeurs, il suffit d'indiquer l'indice '1' (un)
# >>> sorted(d1.items(), key=lambda t: t[1])
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('a1', 5), ('d1', 6), ('c1', 8), ('b1', 10)]
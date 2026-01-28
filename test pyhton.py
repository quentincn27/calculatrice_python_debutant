print("ma premiere calculatrice sous pyhton !")

#on demande à l'utilisateur de choisir deux nombres
nombre1 = input("Entrez un nombre :")
nombre2 = input("Entrez un deuxième nombre :")

# on vérifie si oui ou non, les deux entrées sont des chiffres
if nombre1.isnumeric() and nombre2.isnumeric():
    print("Vous avez bien choisi deux chiffres !")

# sinon les entrées ne sont pas des chiffres et on sort du programme 
else:
    print("Aumoins et des deux nombres additionnés n'en est pas un")
    raise SystemExit("Fin du programme") 

# c'est des nombres : on change l'entée de str à int
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# demander à l'utilisateur de choisir sa méthode de calcul
operation = input("voulez vous soustraite, additionner, multiplier, ou, diviser ? (tapez -, +, *, /)")

# vérification que l'utilisateur a choisi un bon symbole de calcul
if operation not in ["-", "+", "*", "/"]:
      print("vous n'avez pas choisi de faire un calcul !")
      raise SystemExit("Fin du programme") 

 # mise en place du calcul
else:
     if operation == "-":
         resultat = nombre1 - nombre2
     elif operation == "+":
         resultat = nombre1 + nombre2
     elif operation == "*":
         resultat = nombre1 * nombre2
     elif operation == "/":
         # refuser la division par 0
         if nombre2 == 0:
             print("Division par 0 impossible !")
             raise SystemExit("Fin du programme") 
         else:
             resultat = nombre1 / nombre2
     print(resultat)
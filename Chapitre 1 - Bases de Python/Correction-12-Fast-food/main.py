print("""=========Menu=======
  1. Royal Fromage
  2. Big Sandwich
  3. Sandwich Bacon
  4. Sandwich Deluxe

  Votre choix ? """)

sandwiches=["Royal Fromage","Big Sandwich","Sandwich Bacon","Sandwich Deluxe"]

choix=int(input("quel est votre choix ?"))
print("Vous avez choisi le "+sandwiches[choix-1]+". C'est un très bon choix !")
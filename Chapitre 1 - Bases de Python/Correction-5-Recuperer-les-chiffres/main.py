nombre = int(input("Entrez un nombre à deux chiffres."))
dizaines = nombre//10
units = nombre%10
print("Ce nombre a "+str(dizaines)+" dizaine(s) et "+str(units)+" unité(s).")
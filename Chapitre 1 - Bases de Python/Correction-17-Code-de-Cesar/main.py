phrase = input("Entrez un mot.\n")
phraseChiffree = ""

for ch in phrase:
    if ch == "z" or ch == "Z":
        phraseChiffree += chr(ord(ch) - 25)
    else:
        phraseChiffree += chr(ord(ch) + 1)

print(phraseChiffree)

phraseDechiffree = ""
for ch in phraseChiffree:
    if ch == "a" or ch == "A":
        phraseDechiffree += chr(ord(ch) + 25)
    else:
        phraseDechiffree += chr(ord(ch) - 1)

print(phrasedeChiffree)

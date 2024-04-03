phrase = input("Entrez un mot.\n")
phraseChiffree = ""

for ch in phrase:
  if ch=="z" or ch=="Z":
    phraseChiffree += chr(ord(ch)-25)
  else:
    phraseChiffree += chr(ord(ch)+1)

print(phraseChiffree)
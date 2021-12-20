resultat = ""
clé = input("clé :")
phrase = input(str("Phrase :"))
for i, j in zip(clé, phrase):
    if j == " ":
        resultat +=(j)
    else:
        c = ord(i) - 97 + ord(j)
        while c > 122:
            c = c-26
        resultat +=(chr(c))


print(resultat)

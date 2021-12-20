phrase = input("choisissez une phrase:")
clef = input("Choisissez la clef:")   #ici on peut remplacer par un input si on veut proposer à l'utilisateur de choisir le code de décalage, le programme fonctionnera
code = ""
for i in range(len(phrase)):
    n = ord(clef[i%len(clef)])-97
    if phrase[i] != " ":
        if ord(phrase[i])+n > 122:
            code += chr(ord(phrase[i])+n-26)
        else:
            code += chr(ord(phrase[i])+n)
    else:
        code += " "
    print(phrase[i], n, code[i])
print(code)

a=input("appuyez sur entrée pour mettre fin au programme")
while True:
    try:
        x=int(input("entrez un nombre entier:"))
        break
    except ValueError:
        raise NameError('Ce n"est pas une année')
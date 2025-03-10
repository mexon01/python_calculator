
# calculatrice

# comment faire une calculatrice en python

# 1/  demander un nombre

# 2/ demander un autre nombre indentique ou pas

# 3/ additionner les deux nombres

while (True):

    def addition():
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez un deuxieme nombre: ")

        if nbr1.isdigit() and nbr2.isdigit():
            resultat = int(nbr1) + int(nbr2)
            print(resultat)
        else:
            print("Veuillez entrer uniquement des nombres entiers.")
            print('\n')
            addition()

    def soustraction():
        nbr1 = input("entrez le premier nombre: ")
        nbr2 = input("entrez le deuxième nombre: ")

        if nbr1.isdigit() and nbr2.isdigit():
            resultat = int(nbr1) - int(nbr2)

            print(resultat)
        else:
            print("Veuillez entrer uniquement des nombres entiers.")
            print('\n')
            soustraction()

    def multiplication():
        nbr1 = input("Entrez le premier nombre: ")
        nbr2 = input("Entrez un deuxieme nombre: ")

        if nbr1.isdigit() and nbr2.isdigit():
            resultat = int(nbr1) * int(nbr2)
            print(resultat)
        else:
            print("Veuillez entrer uniquement des nombres entiers.")
            print('\n')
            multiplication()

    def division():
        nbr1 = input("entrez le premier nombre: ")
        nbr2 = input("entrez le deuxième nombre: ")

        if nbr1 == '0' or nbr2 == '0' :
            print('\n')
            print("Impossible de diviser par 0.")
            print('\n')
            division()
        elif nbr1.isdigit() and nbr2.isdigit():
            resultat = int(nbr1) / int(nbr2)

            print(resultat)
        else:
            print("Veuillez entrer uniquement des nombres entiers.")
            print('\n')
            division()

    if __name__ == '__main__':
        while True:
            print("Bienvenue dans la calculatrice")
            operation = input("Quelle oppération voulez vous faire ? +, -, *, /,: ")
            print('\n')

            if operation == '+':
                addition()
                break
            elif operation == '-':
                soustraction()
                break
            elif operation == '*':
                multiplication()
                break
            elif operation == '/':
                division()
                break
            else:
                print("Entrez un signe valide (+, -, *, /) ")
                print('\n')

# int 5
# char '5'
# float 5.5
# str "gay"
# bool True False





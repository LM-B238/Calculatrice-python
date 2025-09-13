# calculatrice.py
# Une petite calculatrice basique en terminal
# Auteur : TECH BOX
# Licence : MIT

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible."
    return a / b

def menu():
    print("\n=== CALCULATRICE PYTHON (Terminal) ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

def main():
    while True:
        menu()
        choix = input("Choisissez une opération (1-5) : ")

        if choix == "5":
            print("Merci d'avoir utilisé la calculatrice ! À bientôt 👋")
            break

        if choix in ["1", "2", "3", "4"]:
            try:
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le second nombre : "))
            except ValueError:
                print("⚠️ Entrée invalide. Veuillez entrer un nombre.")
                continue

            if choix == "1":
                print(f"Résultat : {addition(a, b)}")
            elif choix == "2":
                print(f"Résultat : {soustraction(a, b)}")
            elif choix == "3":
                print(f"Résultat : {multiplication(a, b)}")
            elif choix == "4":
                print(f"Résultat : {division(a, b)}")
        else:
            print("⚠️ Choix invalide, réessayez.")

if __name__ == "__main__":
    main()

import random

befehle = ["Schere", "Stein", "Papier"]
punktestand_spieler = 0
punktestand_computer = 0

print("Willkommen zu Schere, Stein, Papier!")

while True:
    print("\nWähle: Schere, Stein, Papier oder Exit")
    spieler_wahl = input("Deine Wahl: ").capitalize()

    if spieler_wahl == "Exit":
        print("\nSpiel beendet!")
        print(
            f"Endstand: Spieler: {punktestand_spieler} - Computer: {punktestand_computer}"
        )
        break

    if spieler_wahl not in befehle:
        print("Ungültige Eingabe! Bitte wähle Schere, Stein, Papier oder Exit.")
        continue

    computer_wahl = random.choice(befehle)
    print(f"Computer wählt: {computer_wahl}")
    # Unentschieden
    if spieler_wahl == computer_wahl:
        print("Unentschieden!")
    # Sieg Spieler
    elif (
        (spieler_wahl == "Schere" and computer_wahl == "Papier")
        or (spieler_wahl == "Stein" and computer_wahl == "Schere")
        or (spieler_wahl == "Papier" and computer_wahl == "Stein")
    ):
        print("Du gewinnst diese Runde!")
        punktestand_spieler += 1
    # Sieg Computer
    else:
        print("Der Computer gewinnt diese Runde!")
        punktestand_computer += 1

    print(
        f"Punktestand: Spieler: {punktestand_spieler} - Computer: {punktestand_computer}"
    )

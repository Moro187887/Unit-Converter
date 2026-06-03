def umrechnen():
    print("Einheiten Umrechner")
    print("1: Meter zu Kilometer")
    print("2: Kilometer zu Meter")
    print("3: Zentimeter zu Meter")
    print("4: Meter zu Zentimeter")
    print("5: Kilogramm zu Gramm")
    print("6: Gramm zu Kilogramm")
    print("7: Celsius zu Fahrenheit")
    print("8: Fahrenheit zu Celsius")

    auswahl = input("Waehle eine Option: ")

    try:
        wert = float(input("Gib den Wert ein: "))
    except ValueError:
        print("Bitte eine gueltige Zahl eingeben.")
        return

    if auswahl == "1":
        print("Ergebnis:", wert / 1000, "km")
    elif auswahl == "2":
        print("Ergebnis:", wert * 1000, "m")
    elif auswahl == "3":
        print("Ergebnis:", wert / 100, "m")
    elif auswahl == "4":
        print("Ergebnis:", wert * 100, "cm")
    elif auswahl == "5":
        print("Ergebnis:", wert * 1000, "g")
    elif auswahl == "6":
        print("Ergebnis:", wert / 1000, "kg")
    elif auswahl == "7":
        print("Ergebnis:", (wert * 9 / 5) + 32, "Grad Fahrenheit")
    elif auswahl == "8":
        print("Ergebnis:", (wert - 32) * 5 / 9, "Grad Celsius")
    else:
        print("Ungueltige Auswahl.")


umrechnen()

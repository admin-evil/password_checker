import string
import math

password = input("Wie lautet dein Passwort?")           #fragt nach Passwort

hat_klein = any(c.islower() for c in password)          #prüft ob Kleinbuchstaben enthalten sind
hat_gross = any(c.isupper() for c in password)          #prüft ob Großbuchstaben enthalten sind
hat_zahl = any(c.isdigit() for c in password)           #prüft ob Zahlen enthalten sind
hat_sonder = any(c in string.punctuation for c in password)     #prüft ob Sonderzeichen enthalten sind

laenge = len(password)      #Länge des Passworts

zeichen_vorrat = 0      #Anzahl der möglichen Zeichen

if hat_klein:                   
    zeichen_vorrat += 30

if hat_gross:
    zeichen_vorrat += 29

if hat_zahl:
    zeichen_vorrat += 10

if hat_sonder:
    zeichen_vorrat +=len(string.punctuation)


kombination = zeichen_vorrat ** laenge      #Anzahl der möglichen Kombinationen

versuche_pro_sekunde_frage = int(input("Wieviele Versuche sollen pro Sekunde durchgeführt werden: \n [1] Normaler PC (1.5 Mio/s) \n [2] Profi (100 Mio/s) \n [3] GPU-Angriff (1 Milliarde/s) \n [4] Manuell eingeben: \n "))        #Fragt nach der Anzahl der Versuche pro Sekunde

if versuche_pro_sekunde_frage == 1:
    versuche_pro_sekunde = 1_500_000
elif versuche_pro_sekunde_frage == 2:
    versuche_pro_sekunde = 100_000_000
elif versuche_pro_sekunde_frage == 3:
    versuche_pro_sekunde = 1_000_000_000
elif versuche_pro_sekunde_frage == 4:
    versuche_pro_sekunde = int(input("Gib die Anzahl der Versuche pro Sekunde ein: "))
else:
    print("Ungültige Auswahl, Standardwert (1.5 Mio/s) wird verwendet.")
    versuche_pro_sekunde = 1_500_000

time = kombination / versuche_pro_sekunde       #Berechnet die Zeit in Sekunden, die benötigt wird, um das Passwort zu knacken

def format_zeit(s):         #Formatiert die Zeit in eine lesbare Form
    if s < 60:
        return f"{s:.2f} Sekunden"
    elif s < 3600:
        return f"{s/60:.2f} Minuten"
    elif s < 86400:
        return f"{s/3600:.2f} Stunden"
    elif s < 31_536_000:
        return f"{s/86400:.2f} Tage"
    else:
        return f"{s/31_536_000:.2f} Jahre"
    
if laenge < 6 or zeichen_vorrat < 40:       #Prüft die Sicherheitsstufe des Passworts
    sicherheit = "Schwach"

elif laenge < 10 or zeichen_vorrat < 69:
    sicherheit = "Mittel"

else:
    sicherheit = "Stark"


print("Passwortanalyse:")       #Ausgabe der Passwortanalyse
print("---------------------")
print(f"Länge: {laenge}")
print("Kleinbuchstaben:", "✅" if hat_klein else "❌")
print("Großbuchstaben:", "✅" if hat_gross else "❌")
print("Zahlen:", "✅" if hat_zahl else "❌")
print("Sonderzeichen:", "✅" if hat_sonder else "❌")
print(f"Sicherheitsstufe: {sicherheit}")
print(f"🔐 Geschätzte Zeit zum Knacken: {format_zeit(time)}")
import string
import math

password = input("Wie lautet dein Passwort?") #fragt nach Passwort

hat_klein = any(c.islower() for c in password)
hat_gross = any(c.isupper() for c in password)
hat_zahl = any(c.isdigit() for c in password)
hat_sonder = any(c in string.punctuation for c in password)

laenge = len(password)

zeichen_vorrat = 0

if hat_klein:
    zeichen_vorrat += 30

if hat_gross:
    zeichen_vorrat += 29

if hat_zahl:
    zeichen_vorrat += 10

if hat_sonder:
    zeichen_vorrat +=len(string.punctuation)


kombination = zeichen_vorrat ** laenge

versuche_pro_sekunde = 1550000

time = kombination / versuche_pro_sekunde

def format_zeit(s):
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
    
if laenge < 6 or zeichen_vorrat < 40:
    sicherheit = "Schwach"

elif laenge < 10 or zeichen_vorrat < 69:
    sicherheit = "Mittel"

else:
    sicherheit = "Stark"


print("Passwortanalyse:")
print("---------------------")
print(f"Länge: {laenge}")
print("Kleinbuchstaben:", "✅" if hat_klein else "❌")
print("Großbuchstaben:", "✅" if hat_gross else "❌")
print("Zahlen:", "✅" if hat_zahl else "❌")
print("Sonderzeichen:", "✅" if hat_sonder else "❌")
print(f"Sicherheitsstufe: {sicherheit}")
print(f"🔐 Geschätzte Zeit zum Knacken: {format_zeit(time)}")
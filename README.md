# 🔍 Passwort-Checker (Python)

Ein einfaches Python-Tool zur Analyse der Passwortstärke.

Du gibst ein Passwort ein – das Programm bewertet es anhand von Länge und enthaltenen Zeichenarten. Zusätzlich wird geschätzt, wie lange ein Brute-Force-Angriff zur Entschlüsselung dauern würde.

---

## ⚙️ Funktionen

- Erkennung von:
  - ✅ Kleinbuchstaben (`a-z`)
  - ✅ Großbuchstaben (`A-Z`)
  - ✅ Zahlen (`0-9`)
  - ✅ Sonderzeichen (`!@#$...`)
- Berechnung der Passwortkombinationen
- Geschätzte Knackzeit in:
  - Sekunden / Minuten / Stunden / Tage / Jahre
- Sicherheitsbewertung:
  - 🔴 Schwach
  - 🟡 Mittel
  - 🟢 Stark

---

## 🧪 Beispielausgabe

```
Wie lautet dein Passwort? Test123!
Passwortanalyse:
---------------------
Länge: 8
Kleinbuchstaben: ✅
Großbuchstaben: ✅
Zahlen: ✅
Sonderzeichen: ✅
Sicherheitsstufe: Mittel
🔐 Geschätzte Zeit zum Knacken: 221.32 Jahre
```

---

## 💻 Voraussetzungen

- Python 3.x
- Terminal oder Visual Studio Code

---

## ▶️ Ausführen

```bash
python password_checker.py
```

---

## 📝 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.  
Du darfst es frei nutzen, ändern und teilen.

---

## 📦 Hinweis

Die Datei ist ein Lernprojekt und kann jederzeit verbessert und erweitert werden.  
Pull Requests und Feedback sind willkommen!

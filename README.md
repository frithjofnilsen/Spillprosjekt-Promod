# Dungeon Brawler

**Opprettet av:** Frithjof Nilsen  
**Dato:** 12.01.2025

---

## Beskrivelse av spillet

**Dungeon Brawler** er et spennende spill hvor målet er å oppnå så høy poengsum som mulig.  
Du styrer en spiller som kan hoppe og bevege seg til høyre og venstre. Du starter med **5 liv**.

***For å starte spillet, kjør main.py***

### Viktige mekanikker:

- En fiende spawner med varierende hastighet, enten til høyre eller venstre.  
  Fienden beveger seg fram og tilbake på skjermen.
- Hvis fienden treffer deg mens du står på bakken:
    - Du mister ett liv.
    - Du blir udødelig i ett sekund.
- Hvis du hopper på fienden:
    - Fienden dør.
    - Poengsummen din øker med 1.
    - En ny fiende spawner.

**Spillet avsluttes når du mister alle 5 livene, og en slutt-skjerm vises.**

Hvis du ønsker å spille på nytt, kan du trykke `ENTER`.  
For å avslutte spillet, lukk vinduet ved å trykke på krysset øverst i hjørnet.

---

## Kontrollene

| Handling            | Tast              |
|---------------------|-------------------|
| Beveg til venstre   | ⬅ PIL TIL VENSTRE |
| Beveg til høyre     | ➡ PIL TIL HØYRE   |
| Hopp                | `MELLOMROM`       |

---

## Filstruktur

Spillet er organisert i følgende filer:

- **`main.py`**  
  Hovedfilen til spillet. Styrer alt og kaller på funksjonene fra de andre filene.

- **`player.py`**  
  Styrer bevegelser og tegning av spilleren.

- **`enemy.py`**  
  Styrer bevegelse og tegning av fienden.

- **`settings.py`**  
  Bestemmer ulike konstanter i spillet.

- **`utils.py`**  
  Inneholder funksjoner som brukes på tvers av filene.

---

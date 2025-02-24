# Experimentele
This is the repo for **Mathias Meersschaut**'s and **Michail Ognyanov**'s practica. Here you will find all files and papers (and Ruben Van Den Borght's folder).
## Hoe werkt github???
### Ik wil de code downloaden, hoe werkt dat?
Als je de code gewoon eens wilt downloaden, dan kan je rechtsboven op de groene knop *Code* klikken en dan `download .zip`.
### Ik wil wijzigingen toepassen op mijn apparaat
Eerst moet je een keer de hele structuur kopieren, dit doe je met: `git clone git@github.com:MathiMuts/Experimentele.git`.
Dan kan je elke keer als er wijzigingen zijn en je die op uw apparaat wilt volgend comando runnen in die map: `git pull`. Als je een error krijgt, dat betekent dat dat je aanpassingen hebt op jouw apparaat die overschreven zouden worden als je pullt, er zijn 2 opties:
1) Delete lokale aanpassingen en pull daarna: `git reset --hard` en `git pull`
2) push eerst je changes, je kan dit forced doen als je zeker bent dat je de al geuploade files wilt overschrijven, pas hiermee op: `git push --force`
### Ik wil mijn wijzigingen online zetten
Run eerst volgend comando om de huidige files te tracken: `git add -A`
Run volgende comando om je wijzigingen te bundelen en een tag te geven: `git commit -a -m "__SCHRIJF HIER IETS NUTTIG OVER WAT ER VERANDERD IS__"`
Tot slot kan je alle bundels die je lokaal hebt pushen naar de server: `git push`
## Samenvatting
```
git pull
```
```
git add -A
git commit -a -m "__KORTE BESCHRIJVING__"
git push
```
# PRACTICA
## Practicum 1: *De werking van een oscilloscoop*
- **Totaal (17/20)**
- Practicum (9/10 --> 11/12)
    -	Bespreking van de calibratie. (1 /1)
    -	Bespreking AC/DC schakelaar ( 1/2). 
    -	Resonantiefrequentie meten circuit 1 (fig. 3). Bespreken statistische vs systematische fout. ( 2.5/2.5)
    -	Fase circuit 2 (fig 4). In X-Y modus ( 1.5/1.5)
    -	Fase circuit 2 in y-t modus Zie of juiste teken bekomen wordt, en of punten verstandig gekozen zijn rond resonantie. (2/2)
    -	Inwendige weerstand besproken? ( 1/1)
- Stijl (6/8)
- Voorbereiding 8.5/10
## Practicum 2: *Netwerken en de wetten van Kirchoff*
- **verslag: 9/10**
- voorbereiding: 5/5
## Practicum 3: *Pythontaak*
- **Totaal: 10/10**
- Ordelijk verslag : 1/1
- Python code ordelijk bijgevoegd : 1/1
## Practicum 4: *Analoge en digitale Prismaspectrometer*
- **Totaalscore 19.5/20**
- Cauchyfit Prisma (He) 2/2 
    - Fitwaardes 0.5/0.5 
    - Fouten bij fitwaardes 0.5/0.5
    - Chi2 p waarde 0.5/0.5
    - Interpretatie fitkwaliteit 0.5/0.5
- Onbekende Lamp (goed behandeld?) 1/1
- Meetsysteem schema 1.5/1.5
    - Figuur toegevoegd 0.5/0.5
    - Vergelijking analoog en digitaal meetsysteem (sensor) 1/1
- Opstellingen goed uitgelegd 1/1
- Calibratie blauwe en rode kleurstof (+ Lineaire fit) 3/3
    - Rico + fouten voor twee reeksen 2/2
    - Chi2 p waarde 0.5/0.5
    - Interpretatie fitkwaliteit 0.5/0.5
- Mystery concentratie 1.5/2
    - Uitvoering 1/1
    - Interpretatie twee componenten 0.5/1
- Spectra edelgas van digitale (+ vgl met hun analoge metingen) 2/2
    - Identificatie lijnen 1/1
    - Bespreking vergelijking met analoge 0.5/0.5
    - p waarde 0.5/0.5
- Piek fit 2/2
    - chi2 p waarde 0.5/0.5
    - interpretatie fitkwaliteit 0.5/0.5
    - figuur 1/1
- Baseline corr. 0.5/0.5 (verklaring gegeven of niet)
- Verslag vormt 1 geheel 1/1
- Stijlgids  4/4 
- Voorbereiding 4/4
## Practicum 5: *Analyse van een Am241 bron*
- **Totaalscore :  7/10**
- Poisson verdeling verwachten + juiste formules en uitvoering om fout achtergrond kleiner te krijgen dan 1 + is de fout op achtergrond kleiner dan 1: 0.5/1
- Fout metingen kleiner dan 5%? 0.5/0.5
- Achtergrond overal afgetrokken (ook bij de proef-specifieke meting) 0/1
- Motivatie gebruikt om de straling te indentificeren 0.5/1
- Fout tellingen onder 10% 0/0.5
- Log I(d) grafiek? 1.5/1.5
- Fit bij grote en kleine d waardes met p-waardes 1.5/1.5
- Verantwoording waarom dit mag! De 27 keV verwaarlozen bij grotere d. 1/1.5
- Beide halveringsdiktes met fout erop 1.5/1.5
## Practicum 6: *De gedreven gedempte harmonischeoscillator*
- **Totaalscore :  9.5/10**
    - Herschrijven uitdrukking:   0.5/1
    - Plotten theoretische spectra:  1/1
    - Python-fits experimentele spectra + interpretatie:  5/5
    - Vergelijking tussen oscillator configuraties:  1.5/1.5
    - Limietgevallen voor hoge en lage frequenties: 0.5/0.5
- Stijlgids:  1/1
## Practicum 6: *Chemie practicum 1: Maken vanoplossingen en kinetica*
WARNING: nog geen verbetering

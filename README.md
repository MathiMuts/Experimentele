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
## Practicum 7: *Chemie practicum 1: Maken vanoplossingen en kinetica*
- **Totaalscore :  18.5/20**
- Voorbereiding 12/12 -> herleiden naar 6 (deel punten door 2)
    - Molaire concentratieberekeningen  4/4 (Voorbereiding, check per waarde)
        - Berekening concentratie correct  4/4 (1pt per waarde)
    - Kinetica 5/8
    - Reactiesnelheid intuitie 3/3
        - statistische verklaring – hogere kans/waarschijnlijkheid op interactie moleculen: pA~ [A]  	1/1
        - reactieorde-stoichiometrie relatie voor elementaire reacties via zelfde principe, bv 2A + B -> A2B, dan 	kans op interactie pA - pA pB .      1/1
        - Niet voor complexe en meerstapsreacties, onder meer door compatibiliteitsoverwegingen tussen moleculen   	1/1
    - Fysische betekenis k  2/2
        - schaalfactor die concentraties (interactiewaarschijnlijkheid) relateert aan de reactiesnelheid. Geeft dus in zekere zin  ‘effectiviteit’ van reactieproces (omzetting reagentia naar reactieproducten)  1/1
        - Hangt voornamelijk af van temperatuur (Arrhenius verband) 1/1
    - Differentiaalvergelijking en plotten  3/3 (/1 per orde, helft op uitwerking, helft op plot)
- DEEL 1: Maken en karakteriseren van oplossingen 6/8
    - Beschrijving bereidingsmethode oplossingen + foutenschatting (glaswerk, bronnen van systematische en statistische fouten)  2/3. 
        - Correct vermelden van het gebruikt glaswerk + fouten 1/1
        - Formule foutenpropagatie (systematische fouten uit glaswerk & stockoplossing voldoende) 1/1
        - Foutwaardes op de concentraties, berekend via de formule, in correcte notatie 0/1
    - Ijklijn  3/3
    - Figuur met data en lineaire fit 1/1 (Beer-Lambert, offset is toegelaten indien besproken/gemotiveerd)
    - Geven van fitwaarden (extinctiecoëfficiënt en eventuele offset) 0.5/0.5 en fitstatistieken (p-waarde en chi-kwadraat) 0.5/0.5   
    - Interpretatie fitstatistieken/fitkwaliteit (0.5)  +  terugkoppeling bereidingsmethode m.a.w. zijn sommige fouten over-of onderschat of waar komen eventuele uitschieters vandaan (0.5). Indien de fitkwaliteit hoog is, hoeft de terugkoppeling naar bereidingsmethode niet uitgebreid.  1/1

    - Bepalen concentratie onbekende oplossing 1/2
    - Omvormen formule – idealiter grafisch aanduiden op figuur ijklijn (niet verplicht)  0/1
    - Foutschatting op de concentratie (via propagatie) 1/1 
- DEEL 2: Kinetica  10/10
    - Pseudo-reactieorde kristalviolet  2/2
    - Figuur met data en fit voor reactieverloop als functie van tijd (mag zowel aangepast linear verband als origineel verband zijn) /2  (1 voor elke concentratie NaOH) 

    - Bepalen snelheidsconstante k’ en halveringstijd t1/2  (fitparameters) 6/6
    - Pseudo-snelheidsconstantes met correcte eenheden en fout  /2 (1 voor elke concentratie)
    - Halveringstijd en bijbehorende fout – via formule (en eventueel grafisch)  /2 (1 voor elke concentratie)
    - Interpretatie fitkwaliteit op basis van fitstatistieken 2/2 (1 voor elke concentratie)

    - Pseudo-reactieorde NaOH 2/2
    - Correct toepassen formule, rekening houdend met verdunning /1.5
    - Foutenschatting via propagatie /0.5
## Practicum 8: *Geluidsgolven*
- **Totaalscore : 10.5/11 -> 9.5/10**
    - Staande golven en kallibratie: 2/2
    - Amplitudes als functie van positie: 2/2
    - Geluidssnelheid: 2/2
    - Golven bij 200 mm: 1/1
    - golven bij 300 mm: 1/1
    - Staandegolfverhouding: 1/1
    - Bijkomende vragen: 1/1
    - stijl 0.5/1
## Practicum 9: *RLC-kring*
- **Totaalscore : 9.75/10**
    - Nagedacht over keuze frequentie opgave 1. ( zodat halve periode b >> RC) 1/1
    - Plot + fit opladen/ontladen 2/2
    - Amplitude en faseplot + vgl met theorie (RC) 2/2
    - Cut off aangeduid : ½*pi*RC vs de 1/sqrt(2) waarde? 1/1
    - Filtertype (hoog- en laagdoorlaatfilter) 1/1
    - Analogie met mechanische oscillator 2/2
    - Stijlgids 0.75/1
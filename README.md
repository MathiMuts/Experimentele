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
## Practicum 7+: *Chemie practicum 2: geen paper*
Geen verslag  
TODO: nog geen punten

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
## Practicum 10: *Chemie practicum 3: Bufferoplossingen en pH titratie*
- **Totaalscore : 19.5/20**
    - Voorbereiding 9.25/10 -> 4.5/5
    - Activiteit en activiteitscoefficient  0.75/1
    - Afleiding stellingen bufferend vermogen  3/3
    - Motivatie keuze buffer + berekening 2/2
    - Verklaring sprong in pH   1.5/2
    - Uitleg pH meter   2/2
    - Deel 1: bereiden van buffers 6/6
        - Kritische reflectie bereidingsmethodes: vermelding gebruikt glaswerk en fouten     1/1
        - Berekening totale nauwkeurigheid op de bereidde pH en concentraties   	           1.5/1.5
        - Vergelijking met gemeten pH + verklaring eventuele afwijkingen  1.5/1.5
        - Bepaling buffercapaciteit adhv twee teststalen met resp. 2 mL NaOH en HCl.        2/2
    - Deel 2:pH titratie 11.5/12 = 9/9
        - Plotten titratiecurve in correcte figuur	(conform stijl, eenheden etc.)		2/2
        - Bepalen equivalentiepunt en fout						1/2
        - Vergelijking indicatoren: methyloranje vs. fenolftaleine (is normaal de beste)      1/1
        - Concentraties azijnzuuroplossing in maatkolf en commerciële oplossing + fouten   2/2
        - Massaprocent azijnzuuroplossing (#g azijnzuur per 100g oplossing) + fout	  2/2
        - Verklaring plateau in begin omslaggebied met reactievgl			1.5/2
        - Bepalen van pKa uit de titratiecurve	                                                           1/1

## Practicum 11: *Chemie practicum 4: Destillatie en redoxtitratie*
- **Totaalscore : 20/20**
    - Voorbereiding	 	6/6
    - Globale reactievergelijking redoxtitratie en molaire verhouding sulfiet/dijood + vergelijking reductiepotentialen 	2/2
    - Uitleg vigreuxkolom en liebigkoeler   2/2
    - Formule volumeprocent water uit dichtheid    2/2
    - Destillatie 		7/7
    - Dichtheid destillaat + fout		2/2
    - Procent wateronzuiverheid		1/1
    - Volume ethanol + fout  + werkwijze    	3/3
    - Volumeprocent ethanol + fout		1/1
    - Redox-titratie 		7/7
    - Waarde + fout op volume en aantal mol titrans (+ relatie tot maatglaswerk en bereidingsprocedure)    	2/2
    - Molariteit (concentratie) waterstofsulfiet + fout 	2/2
    - Sulfietgehalte (mg/L) + fout 		2/2
    - Vergelijking wettelijke limiet  		1/1
## Practicum 12 + 13: *Geavanceerde proeven: E/M ratio + Michelson interferrometer*
**Totaalscore : 18/20**

Geen verslag maar een presentatie:  
> Dit was zowel een zeer goede presentatie als een zeer goede uitvoering van de experimenten. De enige opmerking voor de presentatie die ik heb is dat je best alle symbolen zorgvuldig definieert, als je over een spanning spreekt, verklaar dan ook waarover deze spanning valt. Verder was er heel duidelijk goed nagedacht over een experiment dat niet werkte (en de gevonden conclusie klopte uiteindelijk ook). Verdere vragen bevestigden een uitstekend inzicht in de uitgevoerde experimenten.
## Practicum 14: *Vrije-proef*
TODO: nog geen punten

## Projectwerk: *Werking en analyse van Atom Probe Tomography*
**Totaalscore : 18/20**

Geen verslag maar een presentatie:
> De presentatie was van goede kwaliteit, gestructureerd en wetenschappelijk diepgaand. Een kleine opmerking is dat bij de uitleg in het begin van het werkingsprincipe nog iets visueler kon (de naald van het materiaal onder hoogspanning en dan m.b.v. laser atomen los te werken, hier was een figuur waardevol geweest). Het was wel echt duidelijk dat jullie de techniek begrepen en bij de dataverwerking zeer rigoureus te werk zijn gegaan (wetenschappelijke literatuur meegedeeld en kritisch vergeleken). Ook jullie presentatiestijl komt duidelijk over, met voldoende vertrouwen en met aandacht voor het bevattelijk overbrengen van achtergrond en resultaten. Kortom, sterk wetenschappelijk werk en helder gepresenteerd.

## Samengevat:
- 17/20
- 9/10
- 10/10
- 19.5/20
- 7/10
- 9.5/10
- 18.5/20
- 19.5/20
- 9.5/10
- 9.75/10
- 20/20
- 18/20
- ?
- 18/20

> Vakscore: /20
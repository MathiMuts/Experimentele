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
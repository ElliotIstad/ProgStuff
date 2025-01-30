import random

def monty_hall():
    kan_velges = [1, 2, 3]
    kan_åpnes = [1, 2, 3]
    bil = random.randint(1, 3)
    kan_åpnes.remove(bil)
    valg = int(input('Velg en dør: '))
    kan_velges.remove(valg)
    if valg in kan_åpnes:
        kan_åpnes.remove(valg)
    synlig = random.choice(kan_åpnes)
    print('Det er en geit bak døren', synlig)
    kan_velges.remove(synlig)
    bytte=input('Vil du bytte dør? ')
    if bytte == 'ja':
        valg = kan_velges[0]
    if valg == bil:
        print('Du vant en bil!')
    else:
        print('Du vant en geit!')

monty_hall()
#det er høyere sannsynlighet for å vinne bilen visst du bytter dør
#når du velger en dør gjør det at sjansen for å vinne bilen er 1/3 og de andre to dørene til sammen er 2/3
#visst en av de blir åpnet endrer ikke sjansene seg så den ene døren som ikke er din er fortsatt 2/3 og din er 1/3
#for å konkludere, alltid bytt visst du har sjansen
import time as t

 

def colored(r, g, b, text):

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

 

print('Hva er din favorittfarge?')

t.sleep(1)

 

farge = input('Farge: ')

t.sleep(0.2)

 

if farge=="blå":

    print(f'Favorittfargen din er {colored(0,0,255, farge)}')

if farge=="grønn":

    print(f'Favorittfargen din er {colored(0,255,0, farge)}')

if farge=="rød":

    print(f'Favorittfargen din er {colored(255,0,0, farge)}')

if farge=="gul":

    print(f'Favorittfargen din er {colored(255,255,0, farge)}')      

if farge=="oransje":

    print(f'Favorittfargen din er {colored(255,165,0, farge)}')  

if farge=="rosa":

    print(f'Favorittfargen din er {colored(255, 192, 203, farge)}')
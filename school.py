import time as t

navn = str(input("Hva er navnet ditt? : "))
alder = int(input("Hvor gammel er du? : "))
høyde = float(input("Hva er høyden din i meter? : "))
navnsvar = "er navnet ditt"
aldersvar = "er alderen din"
høydesvar = "er hvor høy du er i meter"

navnfinal = (navn, navnsvar)
alderfinal = (alder, aldersvar)
høydefinal = (høyde, høydesvar)

print(navnfinal)
print(alderfinal)
print(høydefinal)

t.sleep(5)

'''
print(type(navn))
print(type(alder))
print(type(høyde))
'''

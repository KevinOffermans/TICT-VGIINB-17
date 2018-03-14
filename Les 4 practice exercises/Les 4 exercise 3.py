Antwoord = int(input ('Hoe lang ben je?'))
def lang_genoeg (Lengte):
    if Lengte >= 120:
        return 'Je mag in de attractie'
    else:
        return 'Helaas, je bent te klein'
print (lang_genoeg (Antwoord))
afstand = 12
def standaardprijs (afstandKM):
    if afstandKM >= 0 and afstandKM <= 50:
        return afstandKM * 0.8
    elif afstand < 0:
        print ('Je bent retarded')
        return 0
    else:
        return 15 +(afstandKM * 0.6)

dag = 'zondag'
leeftijd = 37

def prijsmetkorting (afstandKM,leeftijd,dag):
    K = 0
    if (dag == 'zaterdag' or dag == 'zondag') and (leeftijd <= 12 or leeftijd >= 65):
        K= 0.35
    elif (dag != 'zaterdag' or dag != 'zondag') and (leeftijd <= 12 or leeftijd >= 65):
        K= 0.30
    elif (dag == 'zaterdag' or dag == 'zondag') and (leeftijd >= 12 or leeftijd <= 65):
        K= 0.40  #K = korting
    else:
        K = 1
    return standaardprijs(afstandKM) * K

print (prijsmetkorting (afstand,leeftijd,dag))







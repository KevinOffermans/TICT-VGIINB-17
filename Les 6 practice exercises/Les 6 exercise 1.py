maandnummer = 1
def seizoen (maand):
    if maand <= 2 or maand == 12:
        print ('winter')
    elif maand >= 3 and maand <= 5:
        print ('lente')
    elif maand >= 6 and maand <= 8:
        print ('zomer')
    elif maand >= 9 and maand <= 11:
        print ('herfst')

print (seizoen (maandnummer))
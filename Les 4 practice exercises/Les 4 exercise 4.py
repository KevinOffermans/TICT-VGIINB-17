def wachtwoord_keuren(oudwachtwoord, nieuwwachtwoord):
    nummer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nummer:
        if (nieuwwachtwoord.count(num) >= 1):
            Result = True
            break
        else:
            Result = False
    if nieuwwachtwoord != oudwachtwoord and len(nieuwwachtwoord) >= 6 and Result = True:
        print('Wachtwoord goedgekeurd')
    else:
        if len(nieuwwachtwoord) < 6:
            print('Het wachtwoord is te kort')
        if Result == False:
            print('Het wachtwoord moet een getal bevatten')
        if nieuwwachtwoord == oudwachtwoord:
            print('Het nieuwe wachtwoord moet anders zijn dan het oude wachtwoord')


Antwoord_1 = str(input ('Wat is je oude wachtwoord?'))
Antwoord_2 = str(input ('Wat is je nieuwe wachtwoord?'))
while wachtwoord_keuren(Antwoord_1, Antwoord_2) == False:
    print('Wachtwoord afgekeurd, voer een nieuw wachtwoord in')
    Antwoord_2 = str(input('Wat is je nieuwe wachtwoord?'))
print('Wachtwoord goedgekeurd')






# if len(nieuwwachtwoord) >= 6 and nieuwwachtwoord != oudwachtwoord:
#     return 'Wachtwoord goedgekeurd'
# else:
#     return 'Wachtwoord afgekeurd, voer een nieuw wachtwoord in'
#
# print (wachtwoord_keuren(Antwoord_1, Antwoord_2))
TempC = 50

def convert (celsius):
    TempF = (celsius * 1.8) + 32
    return TempF

def table ():
    # TemperaturenC = [-30,-20,-10,0]
    for Temp in range (-30, 41, 10):
        print ('{:5} {:3}'.format (convert (Temp), Temp))
        # print (convert (Temp), Temp)

table ()

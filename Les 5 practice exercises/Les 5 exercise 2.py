infile = open('kaartnummers.txt', 'r+')
linelist = infile.readlines ()
infile.close ()


for line in linelist:
    V1 = line.split(',')
    print (V1[1].strip ()+ ' ' + 'heeft kaartnummer: ' + V1[0].strip ())

infile = open('kaartnummers.txt')

linelist = infile.readlines()
print ('Deze file telt ' + str(len(linelist)) + ' regels')

for line in linelist:
    V1 = line.split(',')
    linelist= (V1[0].split())
    print (linelist)
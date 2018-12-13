import urllib.request, csv

URLEnds = []
congress = "107"

file  = open(congress + ".txt", "r")
for line in file:
    identifier = ""
    index = line.find("index=")
    if(index > 0):
        identifier = line[index + 6:index + 6 + 7]
        URLEnds.append(identifier)

print(URLEnds)
bios = []
alreadyInDatabase = [] #TODO

# with open('bios.csv', mode='rw') as readFile:
#     csv_reader = csv.reader(file, delimiter=',')
#     for row in csv_reader:
#         alreadyInDatabase.append(row[1])
#     for ids in URLEnds:
#         if ids in alreadyInDatabase:



def getDegreeArray(text):
    degrees = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    if(text.find("B.A.") > 0 or text.find("A.B.") > 0):
        degrees[0] = 1
    if(text.find("B.S.") > 0 or text.find("S.B.") > 0):
        degrees[1] = 1
    if(text.find("J.D.") > 0):
        degrees[2] = 1
    if(text.find("Ph.D.") > 0 or text.find("Ed.D.") > 0):
        degrees[3] = 1
    if(text.find("M.B.A.") > 0):
        degrees[4] = 1
    if(text.find("M.A.") > 0):
        degrees[5] = 1
    if(text.find("M.S.") > 0):
        degrees[6] = 1
    if(text.find("M.P.H.") > 0):
        degrees[7] = 1
    if(text.find(" M.D.") > 0):
        degrees[8] = 1
    if(text.find("D.M.D.") > 0):
        degrees[9] = 1
    return(degrees)



for end in URLEnds[250:]:

    fp = urllib.request.urlopen("http://bioguide.congress.gov/scripts/biodisplay.pl?index=" + end)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    #get name
    name_start = mystr.find("<P><FONT SIZE=4 COLOR=\"#800040\">") + 32
    name_end = name_start+ mystr[name_start:].find("</FONT>")-1
    name = mystr[name_start:name_end]
    if(name[-1] == ","):
        name = name[:-1]
    print(name)

    #get bio
    bio_start = name_end + 8
    bio_end = bio_start + mystr[bio_start:].find("</TD")
    bio = mystr[bio_start:bio_end]
    bio = [line for line in bio.split('\n') if line.strip() != '']
    bio = str(bio)
    #print(bio)

    degrees = getDegreeArray(bio)
    entry = [name, end, bio, degrees]
    bios.append(entry)

with open('bios107.csv', mode='a') as writeFile:
    fieldnames = ['Name', 'Bio', 'Identifier', 'B.A.', 'B.S.', 'J.D.', 'Ph.D.', 'M.B.A', 'M.A.', 'M.S.', 'M.P.H.', 'M.D.', 'D.M.D.']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    writer.writeheader()
    for entry in bios:
        writer.writerow({'Name': entry[0], 'Identifier': entry[1], 'Bio': entry[2], 'B.A.': entry[3][0], 'B.S.': entry[3][1], 'J.D.': entry[3][2], 'Ph.D.': entry[3][3], 'M.B.A': entry[3][4], 'M.A.': entry[3][5], 'M.S.': entry[3][6], 'M.P.H.': entry[3][7], 'M.D.': entry[3][8], 'D.M.D.': entry[3][9]}) 


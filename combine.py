import csv
all_entries = []
length = 0
for congress in range(107, 114):
	with open("bios" + str(congress) + ".csv", "r") as file:
		csv_reader = csv.reader(file, delimiter = ',')
		for line in csv_reader:
			if (length == 0):
				length = len(line)
			if (line[0] == "Name"):
				continue
			if (len(line) == length):
				line.append(str(congress))
			else:
				line[length] = str(congress)
			all_entries.append(line)
			#print(line)
print(all_entries)

for i in range(0, len(all_entries)):
	if (i < len(all_entries)):
		current_id = all_entries[i][1]
		congress_array = [all_entries[i][length]]
		for j in range(i+1, len(all_entries)):
			if (j < len(all_entries) and all_entries[j][1] == current_id):
				congress_array.append(all_entries[j][length])
				all_entries.remove(all_entries[j])
		all_entries[i][length] = congress_array

with open('bios_combined.csv', mode='w') as writeFile:
    fieldnames = ['Name', 'Bio', 'Identifier', 'B.A.', 'B.S.', 'J.D.', 'Ph.D.', 'M.B.A', 'M.A.', 'M.S.', 'M.P.H.', 'M.D.', 'D.M.D.', 'Congress']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    writer.writeheader()
    for entry in all_entries:
        writer.writerow({'Name': entry[0], 'Identifier': entry[1], 'Bio': entry[2], 'B.A.': entry[3], 'B.S.': entry[4], 'J.D.': entry[5], 'Ph.D.': entry[6], 'M.B.A': entry[7], 'M.A.': entry[8], 'M.S.': entry[9], 'M.P.H.': entry[10], 'M.D.': entry[11], 'D.M.D.': entry[12], 'Congress': entry[13]}) 





import csv
all_entries = []
length = 0
start_congress = 107 #The first congress to include
end_congress = 115 #The last congress to include

for congress in range(start_congress, end_congress + 1):
	with open("bios" + str(congress) + ".csv", "r") as file:
		csv_reader = csv.reader(file, delimiter = ',')
		for line in csv_reader:
			if (length == 0):
				length = len(line)
			if (line[0] == "Name"):
				continue
			#Add congress number to the dataset
			if (len(line) == length):
				line.append(str(congress))
			else:
				line[length] = str(congress)
			all_entries.append(line)
			#print(line)
#print(all_entries)

#Consolidate duplicates
for i in range(0, len(all_entries)):
	if (i < len(all_entries)):
		current_id = all_entries[i][1]
		congress_array = [all_entries[i][length]]
		for j in range(i+1, len(all_entries)):
			if (j < len(all_entries) and all_entries[j][1] == current_id):
				congress_array.append(all_entries[j][length])
				all_entries.remove(all_entries[j])
		all_entries[i][length] = congress_array

#Fix mistake in datasets that ignores M.P._ for every _ other than H
for i in range(0, len(all_entries)):
	if (all_entries[i][1]).find("M.P.") > 0:
		all_entries[i][10] = '1'
	if (all_entries[i][1]).find("S.M.") > 0:
		all_entries[i][9] = '1'
	if (all_entries[i][1]).find("M.Div") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.Acc") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.H.S.") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("D.Min") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.S.W.") > 0:
		all_entries[i][9] = '0'
		all_entries[i][12] = '1'

#Remove reps from special elections
special_107 = ['W000794', 'S001154', 'F000445', 'L000562', 'B001236', 'W000795', 'M001144', 'S001155', 'C001055']
special_108 = ['N000182', 'H000067', 'C001058', 'H001037', 'B001251', 'A000361']
special_109 = ['M001163', 'S001164', 'C001064', 'B000461', 'S001165', 'S001166']
special_110 = ['B001262', 'R000581', 'T000465', 'L000566', 'F000454', 'C001072', 'C001074', 'S001176', 'C001073', 'S001175', 'E000290', 'F000455']
special_111 = ['Q000023', 'M001178', 'C001080', 'G000559', 'O000169', 'D000610', 'C001081', 'D000611', 'R000585', 'G000560', 'S001188']
special_112 = ['H001062', 'H001063', 'A000369', 'T000471', 'B001278', 'B001279', 'P000604', 'D000617', 'C001089', 'M001184']
special_113 = []
special_114 = ['D000625', 'K000388', 'L000585', 'D000626', 'E000296', 'H001050', 'C001108']
special_115 = ['E000298', 'G000585', 'H001078', 'N000190', 'G000584', 'C001114', 'L000588', 'J000303', 'L000589', 'B001306', 'M001206', 'C001115', 'H001082', 'S001205', 'W000826']
special_116 = []
for i in range(0, len(all_entries)):
	if all_entries[i][2] in special_107:
		all_entries[i][length].remove('107')
	if all_entries[i][2] in special_108:
		all_entries[i][length].remove('108')
	if all_entries[i][2] in special_109:
		all_entries[i][length].remove('109')
	if all_entries[i][2] in special_110:
		all_entries[i][length].remove('110')
	if all_entries[i][2] in special_111:
		all_entries[i][length].remove('111')
	if all_entries[i][2] in special_112:
		all_entries[i][length].remove('112')
	if all_entries[i][2] in special_113:
		all_entries[i][length].remove('113')
	if all_entries[i][2] in special_114:
		all_entries[i][length].remove('114')
	if all_entries[i][2] in special_115:
		all_entries[i][length].remove('115')


#print degrees for each Congress
print("Degree distribution in each Congress:")
for congress in range(start_congress, end_congress + 1):
	count = 0
	jd_count = 0
	non_jd_count = 0
	no_postgrad = 0
	for i in range(0, len(all_entries)):
		hasJD = False
		hasNonJD = False
		if (str(congress) in all_entries[i][length]):
			count += 1
			if (all_entries[i][5] == '1'):
				jd_count += 1
				hasJD = True
			non_jd_degrees = 0
			for j in range(6, 13):
				non_jd_degrees += int(all_entries[i][j])
			if (non_jd_degrees > 0):
				non_jd_count += 1
				hasNonJD = True
			if (not hasJD and not hasNonJD):
				no_postgrad += 1
	print("In", 2*int(congress) + 1788, ": JDs:", jd_count, "Non-JDs:", non_jd_count, "No postgrad:", no_postgrad, "count:", count)

#print degree turnover in each election
print("Degree turnover in each Congress:")
for congress in range(start_congress, end_congress):
	jds_lost = 0
	jds_gained = 0
	non_jd_lost = 0
	non_jd_gained = 0
	non_degree_lost = 0
	non_degree_gained = 0
	total_turnover = 0
	for i in range(0, len(all_entries)):
		hasJD = False
		hasNonJD = False
		if str(congress + 1) in all_entries[i][length]:
			if str(congress) not in all_entries[i][length]:
				total_turnover += 1
				if (all_entries[i][5] == '1'):
					jds_gained += 1
					hasJD = True
				non_jd_degrees = 0
				for j in range(6, 13):
					non_jd_degrees += int(all_entries[i][j])
				if (non_jd_degrees > 0):
					non_jd_gained += 1
					hasNonJD = True
				if (not hasJD and not hasNonJD):
					non_degree_gained += 1
					#print("JD added: ", all_entries[i][0])
		if str(congress) in all_entries[i][length]:
			if str(congress + 1) not in all_entries[i][length]:
				if (all_entries[i][5] == '1'):
					jds_lost += 1
					hasJD = True
				non_jd_degrees = 0
				for j in range(6, 13):
					non_jd_degrees += int(all_entries[i][j])
				if (non_jd_degrees > 0):
					non_jd_lost += 1
					hasNonJD = True
				if (not hasJD and not hasNonJD):
					non_degree_lost += 1
					#print("JD removed: ", all_entries[i][0])
	print("In", 2*int(congress) + 1788, ": JDs Lost:", jds_lost, ", JDs Gained:", jds_gained, ", non-JDs Lost:", non_jd_lost, ", non-JDs Gained:", non_jd_gained, ", no degree lost:", non_degree_lost, ", no degree gained:", non_degree_gained, ", Total Turnover:", total_turnover)

with open('bios_combined.csv', mode='w') as writeFile:
    fieldnames = ['Name', 'Identifier', 'Bio', 'B.A.', 'B.S.', 'J.D.', 'Ph.D.', 'M.B.A', 'M.A.', 'M.S.', 'M.P._.', 'M.D.', 'Other Masters', 'Congress']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    writer.writeheader()
    for entry in all_entries:
        writer.writerow({'Name': entry[0], 'Identifier': entry[1], 'Bio': entry[2], 'B.A.': entry[3], 'B.S.': entry[4], 'J.D.': entry[5], 'Ph.D.': entry[6], 'M.B.A': entry[7], 'M.A.': entry[8], 'M.S.': entry[9], 'M.P._.': entry[10], 'M.D.': entry[11], 'Other Masters': entry[12], 'Congress': entry[13]}) 




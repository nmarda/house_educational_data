import csv, os
all_entries = []
length = 0
start_congress = 107 #The first congress to include
end_congress = 116 #The last congress to include

count =0
for congress in range(start_congress, end_congress + 1):
	with open("other_data//bios" + str(congress) + ".csv", "r") as file:
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
# print(len(all_entries))

#Consolidate duplicates
for i in range(0, len(all_entries)):
	if (i < len(all_entries)):
		current_id = all_entries[i][2]
		congress_array = [all_entries[i][length]]
		for j in range(i+1, len(all_entries)):
			if (j < len(all_entries) and all_entries[j][2] == current_id):
				congress_array.append(all_entries[j][length])
				all_entries.remove(all_entries[j])
		all_entries[i][length] = congress_array

# print(len(all_entries))
#Fix mistake in datasets that ignores M.P._ for every _ other than H
for i in range(0, len(all_entries)):
	if (all_entries[i][1]).find("LL.B.") > 0:
		all_entries[i][3] = '1'
	if (all_entries[i][1]).find("B.B.A.") > 0:
		all_entries[i][3] = '1'
	if (all_entries[i][1]).find("B.E.E.") > 0:
		all_entries[i][4] = '1'
	# if (all_entries[i][1]).find("LL.M.") > 0:
	# 	all_entries[i][5] = '1'
	if (all_entries[i][1]).find("M.P.") > 0:
		all_entries[i][10] = '1'
	if (all_entries[i][1]).find("S.M.") > 0:
		all_entries[i][9] = '1'
	if (all_entries[i][1]).find("M.Div") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.Ed") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.Acc") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.H.S.") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("D.Min") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("D.V.M.") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("D.P.M.") > 0:
		all_entries[i][12] = '1'
	if (all_entries[i][1]).find("M.F.") > 0:
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
out_in_2018 = ['R000435','B000213','W000799','Z000018', 'J000174', 'S001191','M001151', 'B001290', 'S000480', 'M001197', 'L000567', 'L000263', 'R000583','B001283','S001154','D000604','B001294','C001107','P000591','P000588','R000409','S000051','B001269','B001227','K000387','F000448','R000578','V000129','L000580','L000584','R000598','D000625','F000460','D000620','D000533','P000602','H001045','M001182','J000297','B001273','B001243','J000290','L000554','N000184','R000586','S000250','C001037','T000462','P000606','C001106','M001181','B001293','C001105','C001048','E000288','E000293','B000287','G000289','G000566','H001036','H001059','L000573','M001189','P000592','R000592','R000580','R000593','S000583','T000475','T000465','Y000063','D000621','R000604','C001038','C001077','C001096','C001076','D000612','F000372','G000410','G000535','I000056','C000714','M001193','N000127','O000170','P000594','P000611','P000598','R000487','R000570','W000820','Y000066','H001050','L000587','S001170','T000477','G000580','K000390','F000464','T000478','R000608'] 
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
	if all_entries[i][2] == 'K000368': #adding 116 to Ann Kirkpatrick
		all_entries[i][length].append('116')
	if '115' in all_entries[i][length]:
		if all_entries[i][2] not in out_in_2018:
			all_entries[i][length].append('116')

#TODO: Take every member of the 115th who is not in lost_in_2018 and assign them 116th congress too


#print degrees for each Congress
print("Degree distribution in each Congress:")
for congress in range(start_congress, end_congress + 1):
	count = 0
	jd_count = 0
	non_jd_count = 0
	no_postgrad = 0
	ms_count = 0
	mba_count = 0
	ma_count = 0
	ms_count = 0
	mpaph_count = 0
	md_count = 0
	phd_count = 0
	for i in range(0, len(all_entries)):
		hasJD = False
		hasNonJD = False
		if (str(congress) in all_entries[i][length]):
			count += 1
			if (all_entries[i][5] == '1' or all_entries[i][5] == 1):
				jd_count += 1
				hasJD = True
				# if(congress == 116):
				# 	print("Has JD", all_entries[i][0])
			if (all_entries[i][6] == '1' or all_entries[i][6] == 1):
				phd_count += 1
			if (all_entries[i][7] == '1' or all_entries[i][7] == 1):
				mba_count += 1
			if (all_entries[i][8] == '1' or all_entries[i][8] == 1):
				ma_count += 1
			if (all_entries[i][9] == '1' or all_entries[i][9] == 1):
				ms_count += 1
			if (all_entries[i][10] == '1' or all_entries[i][10] == 1):
				mpaph_count += 1
			if (all_entries[i][11] == '1' or all_entries[i][11] == 1):
				md_count += 1
			non_jd_degrees = 0
			for j in range(6, 13):
				non_jd_degrees += int(all_entries[i][j])
			if (non_jd_degrees > 0):
				non_jd_count += 1
				hasNonJD = True
			if (not hasJD and not hasNonJD):
				no_postgrad += 1
	print("In", 2*int(congress) + 1786, ": JDs:", jd_count, "Non-JDs:", non_jd_count, "PhD:", phd_count, "MS:", ms_count, "MBA:", mba_count, "MA:", ma_count, "MPA/P/H:", mpaph_count, "MD:", md_count, "No postgrad:", no_postgrad, "count:", count)

#print degree turnover in each election
print("Degree turnover in each election:")
for congress in range(start_congress, end_congress):
	jds_lost = 0
	jds_gained = 0
	non_jd_lost = 0
	non_jd_gained = 0
	non_degree_lost = 0
	non_degree_gained = 0
	ms_lost = 0
	ms_gained = 0
	phd_gained = 0
	phd_lost = 0
	mba_gained = 0
	mba_lost = 0
	ma_gained = 0
	ma_lost = 0
	mpaph_gained = 0
	mpaph_lost = 0
	md_gained = 0
	md_lost = 0

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
				if (all_entries[i][6] == '1' or all_entries[i][6] == 1):
					phd_gained += 1
				if (all_entries[i][7] == '1' or all_entries[i][7] == 1):
					mba_gained += 1
				if (all_entries[i][8] == '1' or all_entries[i][8] == 1):
					ma_gained += 1
				if (all_entries[i][9] == '1' or all_entries[i][9] == 1):
					ms_gained += 1
				if (all_entries[i][10] == '1' or all_entries[i][10] == 1):
					mpaph_gained += 1
				if (all_entries[i][11] == '1' or all_entries[i][11] == 1):
					md_gained += 1
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
				if (all_entries[i][6] == '1' or all_entries[i][6] == 1):
					phd_lost += 1
				if (all_entries[i][7] == '1' or all_entries[i][7] == 1):
					mba_lost += 1
				if (all_entries[i][8] == '1' or all_entries[i][8] == 1):
					ma_lost += 1
				if (all_entries[i][9] == '1' or all_entries[i][9] == 1):
					ms_lost += 1
				if (all_entries[i][10] == '1' or all_entries[i][10] == 1):
					mpaph_lost += 1
				if (all_entries[i][11] == '1' or all_entries[i][11] == 1):
					md_lost += 1
				non_jd_degrees = 0
				for j in range(6, 13):
					non_jd_degrees += int(all_entries[i][j])
				if (non_jd_degrees > 0):
					non_jd_lost += 1
					hasNonJD = True
				if (not hasJD and not hasNonJD):
					non_degree_lost += 1
					#print("JD removed: ", all_entries[i][0])
	print("In", 2*int(congress) + 1788, ": JDs -/+:", jds_lost, jds_gained, ", non-JDs -/+:", non_jd_lost, non_jd_gained, ", PhD -/+", phd_lost, phd_gained, ", MS -/+:", ms_lost, ms_gained, ", MBA -/+:", mba_lost, mba_gained, "MA -/+:", ma_lost, ma_gained, "MPA/P/H -/+:", mpaph_lost, mpaph_gained, "MD -/+:", md_lost, md_gained, ", no postgrad -/+:", non_degree_lost, non_degree_gained, ", Total Turnover:", total_turnover)

with open('bios_combined.csv', mode='w') as writeFile:
    fieldnames = ['Name', 'Identifier', 'Bio', 'B.A. or equiv.', 'B.S.', 'J.D.', 'Ph.D.', 'M.B.A', 'M.A.', 'M.S.', 'M.P._.', 'M.D.', 'Other Masters', 'Congress']
    writer = csv.DictWriter(writeFile, fieldnames = fieldnames)
    writer.writeheader()
    for entry in all_entries:
        writer.writerow({'Name': entry[0], 'Identifier': entry[1], 'Bio': entry[2], 'B.A. or equiv.': entry[3], 'B.S.': entry[4], 'J.D.': entry[5], 'Ph.D.': entry[6], 'M.B.A': entry[7], 'M.A.': entry[8], 'M.S.': entry[9], 'M.P._.': entry[10], 'M.D.': entry[11], 'Other Masters': entry[12], 'Congress': entry[13]}) 




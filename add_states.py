import urllib.request, csv

bios = []
congress = "109"

file = open("bios" + congress + ".csv", "r")
for line in file:
	bios.append(line)
#for i in range(1, len(bios)):
	#print(bios[i][bios[i].find("from")+5:bios[i].find(";", bios[i].find("from"))])

previous_state = "Alabama"
count = 0
state_JD_count = 0
state_pg_count = 0
states = []
with open("bios" + congress + "_sorted_by_state.csv", "r") as file:
	csv_reader = csv.reader(file, delimiter = ',')
	for line in csv_reader:
		if (line[-1] == "State"):
			continue
		current_state = line[-1]
		print(current_state)
		if (current_state == previous_state):
			count += 1
			if (line[5] == '1'):
				state_JD_count += 1
			if (int(line[6])+int(line[7])+int(line[8])+int(line[9])+int(line[10])+int(line[11])+int(line[12]) > 0):
				state_pg_count += 1
		else:
			states.append((previous_state, count, state_JD_count/count, state_pg_count/count))
			previous_state = current_state
			count = 1
			state_pg_count = 0
			state_JD_count = 0
			if (line[5] == '1'):
				state_JD_count += 1
			if (int(line[6])+int(line[7])+int(line[8])+int(line[9])+int(line[10])+int(line[11])+int(line[12]) > 0):
				state_pg_count += 1
	states.append((previous_state, count, state_JD_count/count, state_pg_count/count))
#print(states)
print(len(states))

for i in range(len(states)):

	print(states[i][0] + "," + str(round(states[i][2], 2))+ "," + str(round(states[i][3], 2)))
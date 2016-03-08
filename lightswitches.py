from sys import argv
script_name, file_name = argv

file_obj = open(file_name)
num_bulbs = int(file_obj.readline())
range_lines = file_obj.readlines()

switch_ranges = []
curr_range = []

for line in range_lines :
    split_line = line.split()
    curr_range = [int(i) for i in split_line]
    curr_range.sort()
    switch_ranges.append(curr_range)

OFF = 0
ON = 1

light_switches = []
for i in range(num_bulbs) :
    light_switches.append(OFF)

for r in switch_ranges :
    for i in range(r[0],r[1] + 1) :
        if light_switches[i] == OFF :
            light_switches[i] = ON
        elif light_switches[i] == ON :
            light_switches[i] = OFF

num_on = 0
for switch in light_switches :
    if switch == ON :
        num_on += 1 

print num_on
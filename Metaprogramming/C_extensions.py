header = """
	C_extensions.py by Erik Lanning 12/04/2016
	Last ran on: 13/04/2016
	Extends the C language.
	Currently supports a very rudimentary "auto", eg
	auto example = some_struct -> struct struct_type example = some_struct;
	This is code is meant as demonstration only.
"""

import sys
import time
import fileinput

def update_last_ran_time():
	this_file = sys.argv[0]
	script_last_run_line = 3
	curr_line = 0
	for line in fileinput.input(this_file, inplace = 1):
		curr_line += 1
		if curr_line == script_last_run_line:
			line = ""
			line += '\tLast ran on: ' + time.strftime("%d/%m/%Y") + '\n'
			print line,
		else:
			print line,
			
	fileinput.close()

def replace_auto_keywords():
	keyword = "auto"
	assignment_token = "="
	for current_file_name in sys.argv[1:]:
		with open(current_file_name, "r") as f:
			file_contents = f.readlines()	
		for line in fileinput.input(current_file_name, inplace = 1):
			if keyword in line:
				found_variable = 0
				for element in line.split():
					if element == assignment_token:
						found_variable = 1
						continue
					if found_variable == 1:
						new_type = find_type(file_contents, element[:-1])
						break
				for updated_line in range(len(file_contents)):
					if keyword in file_contents[updated_line]:
						file_contents[updated_line] = file_contents[updated_line].replace(keyword, new_type)
				print line.replace(keyword, new_type),
			else:
				print line,
	
def find_type(data, key):
	for line in data:
		if key in line:
			return line[ : line.index(key)]
	raise ValueError('Error in the C code.')
	
update_last_ran_time()
replace_auto_keywords()
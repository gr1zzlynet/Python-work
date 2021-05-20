import sys
import os.path

def read_statistics(filepath):
	file = open(filepath, "r")
	file_content = file.read()
	file.close()
	print("errors " + str(file_content.count("[error]")))
	print("notice " + str(file_content.count("[notice]")))

def read_error(filepath):
	file = open(filepath, "r")
	for line in file:
		if "[error]" in line:
			print(line.replace("[error]","").replace("[","").replace("]"," "))
	file.close()

def read_notice(filepath):
	file = open(filepath, "r")
	for line in file:
		if "[notice]" in line:
			print(line.replace("[notice]","").replace("[","").replace("]"," "))
	file.close()

def read_log(filepath, action):
	if not os.path.isfile(filepath):
		print("Invalid file path")
		return
	
	if action == "statistics": 
		read_statistics(filepath)
	elif action == "error":
		read_error(filepath)
	elif action == "notice":
		read_notice(filepath)
	else:
		print("Invalid action [statistics, error, notice]")

def analyze_input(): 
	if len(sys.argv) != 3:
		print("Wrong argument count - python loganalyzer.py <filepath> <action>")
	else: 
		read_log(sys.argv[1], sys.argv[2])

analyze_input()


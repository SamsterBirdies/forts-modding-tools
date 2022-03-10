import os, re

writing = False
file = ""

with open('log.txt','rt') as file:
	data = file.readlines()
try:
	os.mkdir("devices")
except Exception:
	pass

for line in data:
	if line.find("BEGIN SCRIPT DUMP *=*=*=*=*=") != -1:
		writing = True
		name = ""
		for char in line:
			if char.isalnum():
				name += char
			if char == ":" or char == "[":
				break
		file = open(f"devices/{name}.lua", "wt")
		#file.close()
		#file = open(f"devices/{name}.lua", "at")
	elif line.find("END SCRIPT DUMP *=*=*=*=*=") != -1:
		writing = False
		file.close()
	elif line.find("--[[") != -1:
		pass
	elif line.find("--]]") != -1:
		pass
	else:
		if writing:
			file.write(line)
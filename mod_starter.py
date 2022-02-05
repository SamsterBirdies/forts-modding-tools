import os
import sys
'''
Modes: 
1: Create in current directory with prompts.
2: Specify directory to create with arguments. <dir,name,category,priority> (dir can be "cd" for current directory)
3: Specify directory to create with prompts.
'''
mode = 1

currentDir = os.getcwd()

def ConvertToFolderName(name):
	validChar = "abcdefghijklmnopqrstuvwxyz1234567890"
	filename = ""
	for char in name:
		if char.lower() in validChar:
			filename += char
	return filename

def Create(dir,name,category,priority):
	folderName = ConvertToFolderName(name)
	modDir = dir + "/" + folderName
	try:
		#create mod folder
		os.makedirs(modDir)
		#create displayname.lua
		create = open(modDir + "/displayname.lua" , "wt")
		create.write("DisplayName = { \n    ['English'] = L\"" + name + "\",\n}")
		create.close()
		#create mod.lua
		create = open(modDir + "/mod.lua", "wt")
		create.write("Selectable = true\nCategory = \"" + category + "\"\nPriority = " + priority)
		create.close()
		#create folder for category
		if category == "Weapons":
			os.makedirs(modDir + "/weapons")
		elif category == "Devices":
			os.makedirs(modDir + "/devices")
		elif category == "Materials":
			os.makedirs(modDir + "/materials")
		print("done")
	except:
		print("Unable to create files. Check privelages or correct usage")
def Main(mode):
	if mode == 1:
		dir = currentDir
		name = input("Mod name:")
		category = input("Mod category:")
		priority = input("Mod priority:")
	elif mode == 2:
		if sys.argv[1] == "cd":
			dir = currentDir
		else:
			dir = sys.argv[1]
		name = sys.argv[2]
		category = sys.argv[3]
		priority = sys.argv[4]
	elif mode == 3:
		dir = input("Mod Directory:")
		name = input("Mod name:")
		category = input("Mod category:")
		priority = input("Mod priority:")
	else:
		Print("Not a valid mode!")
		exit(0)
	Create(dir,name,category,priority)
Main(mode)
import os, sys, shutil
#place this file in the mods folder of forts. By default the script will open in menu mode if insufficient arguments are given.

#globals
mod_path:str = os.getcwd()
commanders = [
	"commander-bpo-scattershot","commander-bpo-seep","commander-bpo-shockenaugh",
	"commander-cf-buster","commander-cf-moonshine","commander-cf-phantom",
	"commander-da-builder","commander-da-overclocker","commander-da-speed-demon",
	"commander-ee-fireman","commander-ee-heavy-weapons","commander-ee-marksman",
	"commander-iba-miser","commander-iba-spy","commander-iba-turtle"
]
#functions
def localxWorkshop():
	'''Copies local mod folder name folders in commander folders to workshopid folder name in commander folders'''
	#get workshop id
	try:
		publishedfileid = open(mod_path + "/publishedfileid.lua", "rt")
		workshopId = publishedfileid.read()[19:-2]
		print("Workshop id is '"+workshopId+"'")
	except:
		print("No publishedfileid.lua found")
		workshopId = int(input("Enter workshop id:"))
	#discover folders
	try:
		dirFolders = os.listdir(mod_path + "/mods")
	except:
		print("No " + mod_name +"/mods folder")
		exit(0)
	foldersToCopy = []
	for name in commanders: #scan for <commander> folder
		if name in dirFolders:
			foldersToCopy.append(name)
	foldersToCopyTemp = []
	for folder in foldersToCopy: #scan for <commander>/mods folder
		if "mods" in os.listdir(mod_path + "/mods/" + folder):
			foldersToCopyTemp.append(folder)
	foldersToCopy = foldersToCopyTemp
	foldersToCopyTemp = []
	for folder in foldersToCopy: #scan for <commander>/mods/<mod name> folder
		if mod_name in os.listdir(mod_path + "/mods/" + folder + "/mods"):
			foldersToCopyTemp.append(folder)
	foldersToCopy = foldersToCopyTemp
	print("Performing operations on folders: " + str(foldersToCopy))
	#copy folders
	for folder in foldersToCopy:
		shutil.rmtree(mod_path + "/mods/" + folder + "/mods/" + workshopId, True)
		shutil.copytree(mod_path + "/mods/" + folder + "/mods/" + mod_name, mod_path + "/mods/" + folder + "/mods/" + workshopId)
	print("\nDone")
#main
if len(sys.argv) > 1:
	mod_name = sys.argv[1]
else:
	#get mod name
	mod_name = input("Mod folder name:")
mod_path = mod_path + "/" + mod_name
print("Mod directory: " + mod_path)
try:
	os.listdir(mod_path)
except:
	print("Failiure to find mod directory")
	exit(0)
#run main function
localxWorkshop()
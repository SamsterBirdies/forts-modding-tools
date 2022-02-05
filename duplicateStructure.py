import sys, re

#constants
devicesToSearch = [ #add all needed devices here
	#potential vanilla devices
	'barrel','sandbags','reactor',
	#potential vanilla weapons
	'machinegun','minigun','sniper','sniper2', #no tech or upgrade
	'mortar','mortar2', #workshop
	'flak','shotgun','rocketemp','rocket', #armory
	'cannon20mm','cannon', #munitions
	'firebeam','beamlaser', #factory
	#FF devices
	'sbballoon','sbantigravity','sbweight','sbminicore','sbminicore2','sbpropeller','sbjet','sbrocket',
	#FF weapons
	'sbcarpetbomb','sbnukebomb','sbhangflak','sbhangcannon','sblightning','sbthunderbolt'
]

#arg vs prompt mode detection
if len(sys.argv) == 4:
	file2read = sys.argv[1]
	iterations = int(sys.argv[2])
	startID = int(sys.argv[3])
else:
	file2read = input("File to iterate:")
	iterations = int(input("Iteration amount:"))
	startID = int(input("Device ID to start with:"))

#main
with open(file2read + ".spr","rb") as fSource:
	currentID = startID
	startIndexs = {}
	file = fSource.read().hex(' ')#read bytes into a hex string\
	newfile = file
	#search for name matches and enter index and length into dict.
	for deviceType in devicesToSearch:
			#per device in devicetype
			deviceTypeHex = bytes(deviceType, 'utf-8').hex(' ')
			for match in re.finditer(deviceTypeHex, file):#convert string to hexstring and search for all cases in file.
				startIndexs[match.start()] = len(deviceTypeHex)
	#per file
	for iteration in range(iterations):
		#start replacing strings
		for k, v in startIndexs.items():
			txt2replace = newfile[k:k+v+48] #gather substring to replace.
			newtxt = txt2replace[:-11] + currentID.to_bytes(4, 'little').hex(' ')
			newfile = newfile.replace(txt2replace, newtxt) # replace substring with new ID
			currentID += 1
		with open(file2read+str(iteration+1)+".spr","wb") as fDest:
			fDest.write(bytes.fromhex(newfile))
	try:
		with open("IDlog.txt","at") as idlog:
			idlog.write(f"{file2read}: {startID}-{currentID}.\n")
	except Exception:
		with open("IDlog.txt","wt") as idlog:
			idlog.write(f"{file2read}: {startID}-{currentID}.\n")

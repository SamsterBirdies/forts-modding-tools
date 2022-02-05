import os, sys

def copybank(input,output):
	file = open(input + ".bank","rb")
	data = file.read()
	save = open(output + ".bank","wb")
	save.write(data)
	save.close()
	file.close()
	file = open(input + ".strings.bank","rb")
	data = file.read()
	save = open(output + ".strings.bank","wb")
	save.write(data)
	save.close()
	file.close()
	print("finished")
def pathselector(mod):
	if mod == "bg":
		copybank("C:/Users/SamsterBirdies/Documents/FMOD Studio/BirdiesGuns2.1.6/Build/audio/BirdiesGunsBank", "D:/Steam_Games/steamapps/common/Forts/data/mods/BirdiesGuns/audio/BirdiesGunsBank")
	elif mod == "ff":
		copybank("C:/Users/SamsterBirdies/Documents/FMOD Studio/FlyingForts2.1.6/Build/audio/FlyingFortsBank", "D:/Steam_Games/steamapps/common/Forts/data/mods/FlyingForts/audio/FlyingFortsBank")
	elif mod == "mu":
		copybank("C:/Users/SamsterBirdies/Documents/FMOD Studio/ManyUpgrades/Build/audio/ManyUpgrades", "D:/Steam_Games/steamapps/common/Forts/data/mods/ManyUpgrades/audio/ManyUpgrades")
	elif mod == "ipw":
		copybank("C:/Users/SamsterBirdies/Documents/FMOD Studio/IPW2.1.6/Build/audio/IPWbank", "D:/Steam_Games/steamapps/common/Forts/data/mods/insanepsychoweapons/audio/IPWbank")
	elif mod == "rg":
		copybank("C:/Users/SamsterBirdies/Documents/FMOD Studio/realguns/Build/Desktop/RealGUNS_bank", "D:/Steam_Games/steamapps/common/Forts/data/mods/RealGuns/audio/RealGUNS_bank")
	elif mod == "vp":
		#copybank("C:\Users\SamsterBirdies\Documents\FMOD Studio\Vanillaplus2.1.6\Build\audio")
		pass
	else:
		print("Not a valid mod!")
def mainloop():
	print("Valid mods are: bg, ff, ipw, mu, rg, vp")
	choice = input("Select:")
	pathselector(choice)
#main

#if more than 1 argument is given, then those arguments will each copy a bank. Otherwise prompt loop mode is activated.
if len(sys.argv) > 1:
	i = 0
	for option in sys.argv:
		if i > 0:
			pathselector(option)
		i+= 1
else:
	while True:
		print("No arguments given. Using prompt loop mode")
		mainloop()
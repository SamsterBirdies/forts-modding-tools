This is a collection of tools I use for modding the game "Forts"
All contents are free to use, modify, and redistribute.

sbutil.lua This script can be used with dofile(). Contains:
	AddCompGroups(weapons)
	modDUsupport(savename, maxage)
	UpgradeWeaponKeyToIndex(weaponName, upgradeName, index)
	UpgradeDeviceKeyToIndex(deviceName, upgradeName, index)
	TableContains(t, element)
	RemoveSprite(name)
	FindSprite(saveName)
	DisableWeaponDowngrades(saveName)
	DisableDeviceDowngrades(saveName)

Tools:
	
	fortspivots.html
		This will help you setup your sprites on its pivots perfectly.
		File is also accessible from https://www.samsterbirdies.com/tools/fortspivots.html
	
	//You can run the scripts below with python. https://www.python.org/downloads/
	
	bank_copier.py
		This script will copy bank files from your fmod project into your mod folder.
		It requires the code to be rewritten a bit for your fmod and mod project paths.
		Script can be run from any location.
	
	cmdrLocal2Workshop.py
		When modifying your mod with a commander, 
		you need to have a copy of both local and workshop folders containing the change. 
		This script will sync the local folders to the workshop folders.
		Script must be run in Forts/data/mods.
		
	duplicateStructure.py
		Using LoadStructureFile in a map multiple times causes bugs because of duplicate device ID's.
		Step one: make the starting ID in the map a high number like 20000. (you can use this tool for that)
		Step two: dupe the structure file as needed with this tool with an id starting with 1.
		So long and no device ID's overlap, everything will function normally. 
		When the player places a new device, the new ID gets assigned the next highest number. 
		(if highest number is 20000 for example, the next one will be 20001). 
		This way, no device ID's will overlap.
		This script will also keep a log of what the currently used ID's are.
		Script must be run in the same folder as the structure files.
	
	hudiconsTOGtoMS.py
		Before moonshot, HUD icons had a different semi-transparent background. 
		This script will take those old HUD icons and convert them to the new ones.
		Script must be run in the same folder as the icons.
		Please make a backup of your icons before running this. There is a chance of error.
		
	log_device_extract.py
		when using endos dump mod for weapons and devices, 
		this tool will split the single log into seperate neat and tidy files.
		
	make_HUD_icon.py
		This tool will automatically create A, D, R, S textures for HUD sprites.
		An 'example.png' is included
		This script requires PIL (can be installed by running: python -m pip install pillow)
		
	
	mod_starter.py
		This script will save time by creating the basic files needed for starting a new mod.
		Script must be run in Forts/data/mods.

#only runs in linux (needs diff)
import os, sys

#editable directories
local_folder = "/mnt/d/Steam_Games/steamapps/common/Forts/data/mods"
workshop_folder = "/mnt/d/Steam_Games/steamapps/workshop/content/410900"
output_file = "diff.txt"

#get input
if len(sys.argv) > 1:
	mod = sys.argv[1]
else:
	mod = input("mod folder to compare:")

#get directories
local_folder += "/" + mod
workshopid = ""
with open(local_folder + "/publishedfileid.lua") as publishedfileid:
	workshopid = publishedfileid.read()[19:-2]
workshop_folder += "/" + workshopid
print(f"local folder: {local_folder}")
print(f"workshop folder: {workshop_folder}")

#do operations and print results
print("running...\n")
os.system(f"diff -r \"{local_folder}\" \"{workshop_folder}\" > {output_file}")
print("\n ---- FINISHED ---- \n")
with open(output_file) as output:
	print(output.read())
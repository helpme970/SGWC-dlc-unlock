import os

# folder name, minversion, dlc name, dlc id
sgwc2 = [
["dlcAbstractAssassin", "1.0.0.33416", "dlcAbstractAssassin", "10"],
["dlcAngloPack", "1.0.0.34435", "dlcAngloPack", "21"],
["dlcAsiaPack", "1.0.0.34435", "dlcAsiaPack", "23"],
["dlcAssaultPack", "1.0.0.33416", "dlcAssaultPack", "8"],
["dlcBloodFlesh", "1.0.0.33416", "dlcBloodFlesh", "24"],
["dlcCrossbowPack", "1.0.0.34435", "dlcCrossbowPack", "15"],
["dlcEuroPack", "1.0.0.34435", "dlcEuroPack", "22"],
["dlcFire", "1.0.0.33416", "dlcFire", "26"],
["dlcGraffitiGlow", "1.0.0.33416", "dlcGraffitiGlow", "12"],
["dlcHunter", "1.0.0.34435", "dlcHunter", "16"],
["dlcIce", "1.0.0.33416", "dlcIce", "27"],
["dlcInfluencer1", "1.0.0.33416", "dlcInfluencer1", "14"],
["dlcInfluencer2", "1.0.0.33416", "dlcInfluencer2", "28"],
["dlcInfluencerCyril", "1.0.0.33416", "dlcInfluencerCyril", "29"],
["dlcPreorder1", "1.0.0.0", "dlcPreorder1", "6"],
["dlcPreorder2", "1.0.0.0", "dlcPreorder2", "7"],
["dlcSkullBones", "1.0.0.33416", "dlcSkullBones", "25"],
["dlcSnakes", "1.0.0.34435", "dlcSnakes", "17"],
["dlcSolitarySniper", "1.0.0.33416", "dlcSolitarySniper", "9"],
["dlcSupernova", "1.0.0.33416", "dlcSupernova", "13"],
["dlcTemple", "1.0.0.33416", "dlcTemple", "20"],
["dlcWildCats", "1.0.0.34435", "dlcWildCats", "18"],
["dlcWildPlains", "1.0.0.34435", "dlcWildPlains", "19"],
["dlcXrayted", "1.0.0.33416", "dlcXrayted", "11"]
]

sgwc = [
["dlcEngravedBullets", "3.1.1.5000", "EngravedBullets", "13"],
["dlcSpecialCamoAnglo", "3.1.1.5000", "dlcSpecialCamoAnglo", "18"],
["dlcSpecialCamoPack03", "3.1.1.5000", "dlcSpecialCamoPack03", "14"],
["dlcSpecialCamoPack02", "3.1.1.5000", "SpecialCamoPack02", "12"],
["dlcSpecialCamo04", "3.1.1.5000", "SpecialCamo04", "9"],
["dlcSMilitary45", "3.1.1.5000", "SMilitary45", "5"],
["dlcSpecialCamo25", "3.1.1.5000", "SpecialCamo25", "7"],
["dlcHub93", "3.1.1.5000", "Hub93", "2"],
["dlcSpecialCamoEuro", "3.1.1.5000", "dlcSpecialCamoEuro", "20"],
["dlcKellT", "3.1.1.5000", "KellT", "10"],
["dlcSavageSniper", "3.1.1.5000", "dlcSavageSniper", "22"],
["dlcSpecialCamoPack01", "3.1.1.5000", "SpecialCamoPack01", "11"],
["dlcSpecialCamoAsia", "3.1.1.5000", "dlcSpecialCamoAsia", "19"],
["dlcRambowBow", "3.1.1.5000", "Rambow_Bow", "16"],
["dlcMultiplayer", "3.1.1.5000", "dlcMultiplayer", "15"],
["dlcHJ762", "3.1.1.5000", "HJ762", "1"],
["dlcSpecialCamo10", "3.1.1.5000", "SpecialCamo10", "6"],
["dlcMercilessMarksman", "3.1.1.5000", "dlcMercilessMarksman", "21"],
["dlcCrossbowChaos", "3.1.1.5000", "dlcCrossbowChaos", "24"],
["dlcAmur", "3.1.1.5000", "SVAmur", "0"],
["dlcSBodyguard9", "3.1.1.5000", "SBodyguard9", "4"],
["dlcSpecialCamo35", "3.1.1.5000", "SpecialCamo35", "8"],
["dlcSeekersSelects", "3.1.1.5000", "dlcSeekersSelects", "23"],
["dlcP5QSteel", "3.1.1.5000", "P5QSteel", "3"],
]

path = input("Path to game: ")
game = input("Sniper Ghost Warrior 1 or 2: ")
if game == "1":
    dlcs = sgwc
elif game == "2":
    dlcs == sgwc2
else:
    exit("error")

if path[-1] != "/" and path[-1] != "\\":
    path = path + "/"

for dlc in dlcs:
    os.mkdir(path + dlc[0])
    open(path + dlc[0] + "/dlc.xml", "w").write(f"""<dlc minversion="{dlc[1]}" name="{dlc[2]}" id="{dlc[3]}">
	<crcs/>
</dlc>
""")
import os

# folder name, dlc name, dlc id
dlcs = [
["dlcEngravedBullets", "EngravedBullets", "13"],
["dlcSpecialCamoAnglo", "dlcSpecialCamoAnglo", "18"],
["dlcSpecialCamoPack03", "dlcSpecialCamoPack03", "14"],
["dlcSpecialCamoPack02", "SpecialCamoPack02", "12"],
["dlcSpecialCamo04", "SpecialCamo04", "9"],
["dlcSMilitary45", "SMilitary45", "5"],
["dlcSpecialCamo25", "SpecialCamo25", "7"],
["dlcHub93", "Hub93", "2"],
["dlcSpecialCamoEuro", "dlcSpecialCamoEuro", "20"],
["dlcKellT", "KellT", "10"],
["dlcSavageSniper", "dlcSavageSniper", "22"],
["dlcSpecialCamoPack01", "SpecialCamoPack01", "11"],
["dlcSpecialCamoAsia", "dlcSpecialCamoAsia", "19"],
["dlcRambowBow", "Rambow_Bow", "16"],
["dlcMultiplayer", "dlcMultiplayer", "15"],
["dlcHJ762", "HJ762", "1"],
["dlcSpecialCamo10", "SpecialCamo10", "6"],
["dlcMercilessMarksman", "dlcMercilessMarksman", "21"],
["dlcCrossbowChaos", "dlcCrossbowChaos", "24"],
["dlcAmur", "SVAmur", "0"],
["dlcSBodyguard9", "SBodyguard9", "4"],
["dlcSpecialCamo35", "SpecialCamo35", "8"],
["dlcSeekersSelects", "dlcSeekersSelects", "23"],
["dlcP5QSteel", "P5QSteel", "3"],
]

path = input("Path to game: ")

if path[-1] != "/" and path[-1] != "\\":
    path = path + "/"

for dlc in dlcs:
    os.mkdir(path + dlc[0])
    open(path + dlc[0] + "/dlc.xml", "w").write(f"""<dlc minversion="3.1.1.5000" name="{dlc[1]}" id="{dlc[2]}">
	<crcs/>
</dlc>
""")
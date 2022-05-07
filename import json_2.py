import json
import csv
import os
import re

cwd = os.getcwd()
print(cwd)
filePath = "C:\\Users\\Logan\\Desktop\\GTMasters\\Spring2022\\BME8902\\8902_Wrapper\\ukb37912_JSONTEST2.tab"


# def JSON_fix(file_name):
# 	with open(file_name,"w") as file:
# 		for line in file:
# 			changed = "(" + line + "),"
# 			print(line.strip().replace(line,changed))
			
# JSON_fix(filePath)

def ukbJSON(file_name):
	#initialize dicts
	
	fieldJSONList = []
	fileLines = []
	#Get field and patient lists from file
	with open(file_name, "r") as readFile:
		for line in readFile:
			line = line.rstrip().split("\t")
			#all lines
			fileLines.append(line)

	#iterate through matrix
	for row in range(len(fileLines)):
		for col in range(len(fileLines[row])):
			if row != 0 and col != 0:
				if fileLines[row][col] != "NA":
					fieldJSON = {
							"f.eid": "",
							"field": "",
							"assessment": "",
							"index": "",
							"value": "",
							"version": ""
						}
					fieldJSON["f.eid"] = fileLines[row][0]
					fieldJSON["value"] = fileLines[row][col]
					col = (fileLines[0][col].split("."))
					fieldJSON["field"] = col[1]
					fieldJSON["assessment"] = col[2]
					fieldJSON["index"] = col[3]
					fieldJSON["version"] = "2019"
					fieldJSONList.append(json.dumps(fieldJSON))

	with open("test_json.txt","w") as test_json:
		for line in fieldJSONList:
			print("("+line+"),")
			test_json.write("("+line+"),")
			test_json.write('\n')
	

ukbJSON(filePath)
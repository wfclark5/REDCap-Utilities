import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path
import csv
import numpy as np
import datetime

def getData(data):
	r = post("https://redcap.duke.edu/redcap/api/", data)	
	r.content
	d = urllib.parse.urlencode(data).encode("utf-8")
	req = urllib.request.Request("https://redcap.duke.edu/redcap/api/", d)
	response = urllib.request.urlopen(req)
	file = response.read()
	result = json.loads(file)
	df = pd.DataFrame.from_records(result)
	return df


def retrieveInstru(token):
	data = {
	    'token': token,
	    'content': 'instrument',
	    'format': 'json',
	    'returnFormat': 'json'
	}
	instrument = getData(data)
	instrument = instrument['instrument_name']
	instrument = list(instrument)
	return instrument

arc_token = "0845F71549970EA7756BD5765A1F3986"
arc_instruments = retrieveInstru(arc_token)
arc_instruments = set([x.lower() for x in arc_instruments]) 

p1_token = "1C5FEA79CCE2910D921AED8EBDF522E9"
p1_instruments = retrieveInstru(p1_token)
p1_instruments = set([x.lower() for x in p1_instruments]) 

p2_token = "F2E17F1291ED0990E0B64E88ED70CCE5"
p2_instruments = retrieveInstru(p2_token)
p2_instruments = set([x.lower() for x in p2_instruments]) 

p3_token = "4048FA48421A95C1C69123CB4C322BCE"
p3_instruments = retrieveInstru(p3_token)
p3_instruments = set([x.lower() for x in p3_instruments]) 

dev_token = "E643DF26872773CD6C4BE421CF36A476"
dev_instruments = retrieveInstru(dev_token)
dev_instruments = set([x.lower() for x in dev_instruments]) 


arc_dev = list(arc_instruments & dev_instruments)
arc_dev = sorted(arc_dev)
p1_dev = list(p1_instruments & dev_instruments)
p1_dev = sorted(p1_dev)
p2_dev = list(p2_instruments & dev_instruments)
p2_dev = sorted(p2_dev)
p3_dev = list(p3_instruments & dev_instruments)
p3_dev = sorted(p3_dev)
p1_arc = list(p1_instruments & arc_instruments)
p1_arc = sorted(p1_arc)
p1_p2 = list(p1_instruments & p2_instruments)
p1_p2 = sorted(p1_p2)
p1_p3 = list(p1_instruments & p2_instruments)
p1_p3 = sorted(p1_p3)
p2_arc = list(p2_instruments & arc_instruments)
p2_arc = sorted(p2_arc)
p2_p3 = list(p2_instruments & p3_instruments)
p2_p3 = sorted(p2_p3)
p3_arc = list(p3_instruments & arc_instruments)
p2_arc = sorted(p3_arc)



changed_from = []
changed_to = []
change_type = []
project_title = []
instrument_name = []


def compare(token1, token2, instrument):
	data_c1 = {
	    'token': token1,
	    'content': 'metadata',
	    'format': 'json',
	    'returnFormat': 'json',
	    'forms[0]': instrument
	}

	data_c2 = {
	    'token': token2,
	    'content': 'metadata',
	    'format': 'json',
	    'returnFormat': 'json',
	    'forms[0]': instrument
	}

	compare_1 = getData(data_c1)
	compare_2 = getData(data_c2)
	return compare_1, compare_2

logf = open("download.log", "w")



def compareLog(token1, token2, comparison, project_comparison):
	for i in range(len(comparison)):
		print("{} ".format(project_comparison)+ str(comparison[i]))
		df1, df2 = compare(token1, token2, comparison[i])
		print(len(df1), len(df2))
		if(df1.equals(df2)== False):
			try:

				ne_stacked = (df1 != df2).stack()
				changed = ne_stacked[ne_stacked]
				changed.index.names = ['row','col']
				row = changed.index.get_level_values('row')
				col = changed.index.get_level_values('col')
				for j in range(len(row)):
					instrument_name.append(comparison[i])
					project_title.append(project_comparison)
					change_type.append(col[j])
					changed_from.append(df2[col[j]].loc[row[j]])
					changed_to.append(df1[col[j]].loc[row[j]])
				else:
					"Equals"

			except Exception as e:
				logf.write(("{} ".format(project_comparison)+ str(comparison[i])))

				pass

compareLog(p1_token, arc_token, p1_arc, "Project 1/ARC Comparison")
compareLog(p1_token, p2_token, p1_p2, "Project 1/Project 2 Comparison")
# compareLog(p1_token, p3_token, p1_p3, "Project 1/Project 3 Comparison")
# # compareLog(p2_token, arc_token, p2_arc, "Project 2/ARC Comparison")
# compareLog(p2_token, p3_token, p2_p3, "Project 2/Project 3 Comparison")
# compareLog(p3_token, arc_token, p3_arc, "Project 3/ARC Comparison")
# compareLog(arc_token, dev_token, arc_dev, "ARC/Dev Comparison")
# compareLog(p1_token, dev_token, p1_dev, "P1/Dev Comparison")
# compareLog(p2_token, dev_token, p2_dev, "P2/Dev Comparison")
# compareLog(p3_token, dev_token, p3_dev, "P3/Dev Comparison")


d = {'project_title' : project_title, 'instrument_name' : instrument_name, 'type': change_type, 'changed_from' : changed_from, 'changed_to' : changed_to}

corrections = pd.DataFrame(d)

print(instrument_name)

corrections.to_csv('change_log.csv')


# for i in range(len(p1_p2)):
# 	try:
# 		print("p1 to p2 comparison on measure " + str(p1_p2[i]))
# 		compare(p1_token, p2_token, p1_p2[i])
# 	except:
# 		pass

# for i in range(len(p1_p3)):
# 	try:
# 		print("p1 to p3 comparison on measure "+ str(p1_p3[i]))
# 		compare(p1_token, p3_token, p1_p3[i])
# 	except:
# 		pass

# for i in range(len(p2_p3)):
# 	try:
# 		print("p2 to p3 comparison on measure "+ str(p2_p3[i]))
# 		compare(p2_token, p3_token, p2_p3[i])
# 	except:
# 		pass
# for i in range(len(changed)):

# differences_locations = np.where(df1 != df2)
# print(differences_locations)
# changed_from = df1[differences_locations.item[0], differences_locations.item[1]]
# chaged_to = df2[differences_locations[0], differences_locations[1]]

# print(x)


# for i in range(len(p2_dev)):
# 	try:
# 		print("p2 to development comparison on measure "+ str(p2_dev[i]))
# 		compare(p1_token, dev_token, p2_dev[i])
# 	except:
# 		pass

# for i in range(len(p3_dev)):
# 	try:
# 		print("p3 to development comparison on measure "+ str(p2_dev[i]))
# 		compare(p1_token, dev_token, p3_dev[i])
# 	except:
# 		pass





# compare_1.to_csv('test.csv')


# print(len(compare_1))

# print(len(compare_1))




# print(comparison_array)

# if False in comparison_array:
#     print ("Not the same")


# data_c2 = {
#     'token': p2_token,
#     'content': 'metadata',
#     'format': 'csv',
#     'returnFormat': 'csv',
#     'forms[0]': instrument
# }
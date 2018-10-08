import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path
import datetime
# import requests

##Definition to grab data off of the redcap API

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


#Redcap structure and qglobal structure comparison

redcap_structure = pd.read_csv('vabs-new.csv')

qglobal_structure = pd.read_csv('vabs-3.csv')

qglobal = pd.read_csv('vabs_qglobal_test.csv')

table1 = []

for stuff in range(len(redcap_structure)):
	table1.append(redcap_structure.values[stuff][0].lower())


table2 = []

for stuff in range(len(qglobal_structure)):
	table2.append(qglobal_structure.values[stuff][0].lower())

table1.remove('vineland3_form')
table1.remove('vi3_mbc_subdomains')

# print(table2)

redcap_set = set(table1)

qglobal_set = set(table2)

difference_set = qglobal_set ^ redcap_set

difference_list = list(difference_set)

print(difference_list)

#qglobal data manipulation for redcap import

qglobal.columns = map(str.lower, qglobal.columns)
qglobal_redcap = qglobal.drop(columns=difference_list)
qglobal_redcap = qglobal_redcap.fillna("")
qglobal_redcap = qglobal_redcap.applymap(str)
qglobal_json = qglobal_redcap.to_dict(orient='records')

print(qglobal_redcap)
print(len(qglobal_json[0]))


data_export = {
	'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'forms[0]': 'vabs3',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}

records = getData(data_export)


#Filter the data for  completed vabs and then import
for i in range(len(records)):
	if(records['vabs3_complete'].values[i] == '2'):
		qglobal_json[0]['record_id'] = str(records['record_id'].values[i])
		
		qglobal_json = json.dumps(qglobal_json)

		print(qglobal_json)
		data_import = {
		    'token': '',
		    'content': 'record',
		    'format': 'json',
		    'type': 'flat',
		    'overwriteBehavior': 'normal',
		    'forceAutoNumber': 'false',
		    'data': qglobal_json,
		    'returnContent': 'count',
		    'returnFormat': 'json',
		}
		

		r = post("https://redcap.duke.edu/redcap/api/", data_import)
		print(r.status_code)


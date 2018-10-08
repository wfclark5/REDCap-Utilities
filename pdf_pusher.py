import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path

print("Calling RedCAP API...")

data = {
    'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'forms[0]': 'consent_example_testing',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}


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


data_logic = getData(data)

data_logic = data_logic[data_logic["enrollment_testing_complete"] == 'Complete']


def getPdf(record, instrument, filepath):

	pdf = {
    'token': '',
    'content': 'pdf',
    'record': str(record),
    'instrument': str(instrument),
    'returnFormat': 'json'
	}
	
	r = requests.post("https://redcap.duke.edu/redcap/api/", pdf, stream = True)

	filename = r'C:\Users\wfc3\Desktop\Software\ace\{}\{}_{}.pdf'.format(filepath, record, instrument)

	if(os.path.isfile(filename) == False):
		with open(filename, 'wb') as f:
			for chunk in r.iter_content():
				f.write(chunk)

for i in range(len(data_logic)):
	if(data_logic['arc_consent'].values[i]  == 'Yes'):
		getPdf(data_logic['record_id'].values[i], 'arc_consent', "arc\\consents")

for i in range(len(data_logic)):
	if(data_logic['p1_consent'].values[i]  == 'Yes'):
		getPdf(data_logic['record_id'].values[i], 'p1_consent', "p1\\consents")

for i in range(len(data_logic)):
	if(data_logic['p2_consent'].values[i]  == 'Yes'):
		getPdf(data_logic['record_id'].values[i], 'p2_consent', "p2\\consents")

for i in range(len(data_logic)):
	if(data_logic['p3_consent'].values[i]  == 'Yes'):
		getPdf(data_logic['record_id'].values[i], 'p3_consent', 'p3\\consents')


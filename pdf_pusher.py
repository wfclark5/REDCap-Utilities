import os
import urllib2
import urllib
from urllib2 import Request
from urllib import urlencode 
import sys
import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path
import csv
import numpy as np
import datetime
import pandas
import os

# define the name of the directory to be created

# 1. Consent Documentation
# 2. Study Data
# 3. Reports
# 4. Communications

# K:\ACE\ACE1\Participant Data

# 40030 


def getData(data):
	r = post("https://redcap.duke.edu/redcap/api/", data)
	r.content
	d = urlencode(data)
	req = urllib2.Request("https://redcap.duke.edu/redcap/api/", d)
	response = urllib2.urlopen(req)
	file = response.read()
	result = json.loads(file)
	return pandas.DataFrame.from_records(result)



data = {
    'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'fields[0]': 'ace_id',
    'events[0]': 'event_1_arm_1',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}

print("Calling RedCAP API...")


consent_ids = getData(data)
consent_ids = consent_ids['ace_id'].tolist()


ace_id = "".join(
    str("[ace_id]= " + "'" + str(consent_ids[i]) + "'" + " or ")
    for i in range(len(consent_ids)))

ace_id_filter = ace_id[:-4]

print(ace_id)

consent_ids = {
    'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'fields[0]': 'ace_id',
    'fields[1]': 'record_id',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json',
    'filterLogic': "{}".format(ace_id_filter)
}


consent_ids = getData(consent_ids)
ace_ids = consent_ids['ace_id'].tolist()
print(consent_ids.columns.values)
consent_ids = consent_ids['record_id'].tolist()



def getPdf(record, ace_id):
	
	pdf = {
	    'token': '715AD86FEC436F5361105156DCC6BA43',
	    'content': 'pdf',
	    'record': str(record),
	    'instrument': 'ace1_consent_english',
	    'returnFormat': 'json'
	}

	r = requests.post("https://redcap.duke.edu/redcap/api/", pdf, stream = True)

# K:\ACE\ACE1\Participant Data
# 1. Consent Documentation
# 2. Study Data
# 3. Reports
# 4. Communications


	path0 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}'.format(ace_id)
	path1 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\1. Consent Documentation'.format(ace_id)
	path2 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\2. Study Data'.format(ace_id)
	path2_1 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\2. Study Data\\ADOS'.format(ace_id)
	path2_2 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\2. Study Data\\EEG'.format(ace_id)
	path2_3 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\2. Study Data\\EGT'.format(ace_id)
	path2_4 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\2. Study Data\\Leiter'.format(ace_id)
	path3 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\3. Reports'.format(ace_id)
	path4 = r'K:\\ACE\\ACE1\\Participant Data\\ACE1_{}\\4. Communications'.format(ace_id)



	if not os.path.exists(path0):
		try:     
		    os.makedirs(path0)
		    os.makedirs(path1)
		    os.makedirs(path2)
		    os.makedirs(path2_1)
		    os.makedirs(path2_2)
		    os.makedirs(path2_3)
		    os.makedirs(path2_4)
		    os.makedirs(path3)
		    os.makedirs(path4)

		except OSError:  
		    print ("Creation of the directory %s failed" % path4)
		else:  
		    print ("Successfully created the directory %s" % path4)

	filename = r'K:\\ACE\\ACE1\Participant Data\\ACE1_{}\\1. Consent Documentation\\ACE1_{}.pdf'.format(ace_id, ace_id)

	if(os.path.isfile(filename) == False):
		with open(filename, 'wb') as f:
			for chunk in r.iter_content():
				f.write(chunk)


for i in range(len(consent_ids)):
	getPdf(consent_ids[i], ace_ids[i])

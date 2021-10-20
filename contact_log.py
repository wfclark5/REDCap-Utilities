import os
import urllib
from requests import post
import sys
import pandas
import json
import datetime

print("Calling RedCAP API...")


contact = {
    'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'fields[0]': 'a_assessment_consent_english_complete',
    'forms[0]': 'a_assessment_consent_english',
    'rawOrLabel': 'raw',
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
      return pandas.DataFrame.from_records(result)

contact = getData(contact)

contact.to_csv("test.csv")


# flagged = []



# print str(flagged).strip("[]")



# print("Moving data to path...")

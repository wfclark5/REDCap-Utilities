import io 
import json
import yaml
import csv
import pandas as pd
from itertools import chain

from rios.conversion import (
    redcap_to_rios,
    qualtrics_to_rios,
    rios_to_redcap,   
    rios_to_qualtrics,
)  

##This is a qualtrics to rios conversion 
qualtrics = qualtrics_to_rios(id='id0',  title='test', description='test',stream = "/mnt/c/Users/wfc3/Desktop/redcap_upload/qualtrics/qualtrics_health.qsf", instrument_version=None, filemetadata=False, suppress=False)

print qualtrics

instrument = qualtrics['instrument']

form = qualtrics['form']

rios = rios_to_redcap(instrument, form)

print rios

redcap = pd.DataFrame.from_dict(rios['instrument'])

x = redcap.transpose()

print type(x)

outlist = []

for things, rows in x.iterrows():
	outlist.append(rows[0])
	

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(outlist)

    


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


rios_definition = redcap_to_rios(
     id='id0',
     title='test',
     description='This is a test file',
     stream='/mnt/c/Users/wfc3/Desktop/Software/Python/Testing/Data/complex_1.csv',
     localization='en',
     instrument_version='1.0',
     suppress=False )



form = rios_definition['form']

instrument = rios_definition['instrument']

with open("/mnt/c/Users/wfc3/Desktop/Software/Python/Testing/Data/test_i.yaml", 'w') as infile:
	yaml.dump(instrument, infile, default_flow_style=False)


with open("/mnt/c/Users/wfc3/Desktop/Software/Python/Testing/Data/test_f.yaml", 'w') as infile: 
	yaml.dump(form ,infile, default_flow_style=False)






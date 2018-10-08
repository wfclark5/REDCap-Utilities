
from rios.conversion import (
    redcap_to_rios,
    qualtrics_to_rios,
    rios_to_redcap,   
    rios_to_qualtrics,
)  
import glob
import csv
import pandas
import os
import numpy as np



names = []

files = glob.glob("*.txt")

print files

for file in files:
	names.append(file[:-4])


#print new.drop(new(new.filter(like='Author:').rows, 1))
for i in range(0, len(files)):
	new = '{}'.format(names[i])
	new = pandas.read_table(str(os.getcwd()) + '/datatypes/biospecimens.txt', skiprows=0)
	to_drop = ['Author', 'Page', 'Summary', 'Dataset']

	dropped = new[~new['----------------------- Page 1-----------------------'].str.contains('|'.join(to_drop))]


	split = pandas.DataFrame(dropped['----------------------- Page 1-----------------------'].str.split(':',1).tolist(),
	                                   columns = ['Data','FieldType'])

	extras = pandas.DataFrame([['Subject ID', 'TEXT'],['Visit','Radio']], columns=['Data', 'FieldType'])

	clean = split.append(extras)

	clean.FieldType = clean.FieldType.str.replace(" ", "")

	clean.Data = clean.Data.str.replace(" ", "")

	clean =  clean.drop_duplicates()

	final = clean.replace([None,'DATETIME'], 'TEXT')

	conditions = (final['Data'].str.contains('YESNO') == True), (final['Data'].str.contains('YESNO') == False)

	choices = ['0, 1. Yes | 1, 2. No', ' ']

	final['Choices'] = np.select(conditions, choices, default=' ')

	final.FieldType = final.FieldType.str.replace(" ", "")

	print final




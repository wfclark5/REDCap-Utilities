import pandas as pd
import numpy as np
from redcap import Project, RedcapError
import json


#Using the URL and API to connect to Project 1 using the RedCAP API
url_p1 = 'https://redcap.duke.edu/redcap/api/'
api_p1 = ''
project1 = Project(url_p1, api_p1)

#Using the URL and API to connect to Project 2 using the RedCAP API
url_p2 = 'https://redcap.duke.edu/redcap/api/'
api_p2 = ''
project2 = Project(url_p2, api_p2)

print project1
#begin pulling out all of the values of the ADOS test file in P1
forms = project1.forms[5:6]

#create a subset of that project and export the records out of the seelcted form
subset = project1.export_records(forms=forms)
 
#create a dataframe from the list of data that was retrieved from the selected form
ados_testp1 = pd.DataFrame.from_dict(subset)

#begin pulling out all of the values of the ADOS test file in P2
forms_2 = project2.forms[6:7]

#create a subset of that project and export the records out of the seelcted form
subset_2 = project2.export_records(forms=forms)
 

#create a dataframe from the list of data that was retrieved from the selected form
ados_testp2 = pd.DataFrame.from_dict(subset_2)

#create a numpy array object that stores the records data from project 1 and project 2

p1_values = ados_testp1.values[2]
p2_values = ados_testp2.values[0]


#check to see if the values are already up to date. If they are not up to date update the the records across projects.

# if (np.array_equal(p1_values, p2_values)):
# 	print "Form " + forms + " is up-to-date!"
# else:
# 	print "Records for the form: " + str(forms[0]) + " are currently being updated across projects updating..."
# 	response = project2.import_records(subset)


#Begin check on the individual records 

p1_values = p1_values.tolist()
p2_values = p2_values.tolist()


for stuff in range(0,len(p1_values)):
		if p1_values[stuff] == p2_values[stuff]:
			 print 'same'		 
		else:
			print p1_values[stuff] + ' != ' +  p2_values[stuff]
			p2_values[stuff] = p1_values[stuff]

print p2_values
# print p2_values 
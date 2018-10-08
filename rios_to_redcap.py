from rios.conversion import (
    redcap_to_rios,
    qualtrics_to_rios,
    rios_to_redcap,   
    rios_to_qualtrics,
)  


import yaml


with open("format_1_i.yaml") as infile:
	instrument = yaml.load(infile)


with open("format_1_f.yaml") as infile: 
	form = yaml.load(infile)

rios = rios_to_redcap(instrument, form)

print rios

# instrument = "/format_1_i.yaml"
 
#this is a rios_to_redcap conversion
# rios = rios_to_redcap(instrument, form, calculation)

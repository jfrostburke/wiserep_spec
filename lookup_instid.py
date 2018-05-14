"""
This takes an instrument name from the spec database and
returns a wiserep instrument id. Table of ids at:
https://wiserep.weizmann.ac.il/instruments/list
"""

def find(instname,telname):
	if instname == 'en06':
		instid = '108'
		#FLOYDS north
	elif instname == 'en05':
		instid = '125'
		#FLOYDS south
	elif instname == 'EFOSC':
		instid = '31'                 
	elif instname == 'SOFI':
		instid = '34'                 
	elif instname == 'Andor iDus DU440A-BU2':
		instid = '1.22m Reflector+Andor iDus DU440A-BU2'
	elif instname == 'Kast':
		instid = '10'
	elif instname == 'ALFOSC_FASU':
		instid = '41'
	elif instname == 'LRS' and telname == 'TNG':
		instid = '15'
	elif instname == 'LRS' and telname == 'HET':
		instid = '43'
	elif instname == 'GMOS-N':
		instid = '6'
	elif instname == 'LRIS' or 'LRIS+LRISBLUE':
		instid = '3' 
	elif instname == 'DEIMOS':
		instid = '4'
	elif instname == 'STIS':
		instid = '83'
	elif instname == 'Deveny':
		instid = '143'
	elif instname == 'BFOSC':
		instid = '56'
	elif instname == 'YFOSC_YSU':
		instid = '107'
	elif instname == 'GMOS-S':
		instid = '9'
	elif instname == 'lrs2' or 'LRS2-B':
		instid = '43'
	elif instname == 'Goodman Spectro':
		instid = '127'
	elif instname == 'RSS':
		instid = '117'
	elif instname == 'DIS':
		instid = '70'
	else:
		return 'NULL'

	return instid

if __name__ == '__main__':
	find(instrument,telescope)

"""
This takes an classificationid from the targets db and
returns a wiserep object type id. Table of ids at:
https://wiserep.weizmann.ac.il/objtypes/list

Matching classificationid to object type is in
classificationid db.
"""

def find(classificationid):
	if classificationid == 3 or classificationid == 4:
		#SN
		objtypeid = '1'
	elif classificationid == 5 or classificationid == 34:
		#SNIa
		objtypeid = '3'
	elif classificationid == 6 or classificationid == 35:
		#SNIa-bglike
		objtypeid = '103'
	elif classificationid == 7 or classificationid == 36:
		#SNIa-91Tlike
		objtypeid = '104'
	elif classificationid == 8 or classificationid == 37:
		#SNIa-02cxlike (Iax)
		objtypeid = '105'
	elif classificationid == 9 or classificationid == 38:
		#SNIa-02iclike (CSM?)
		objtypeid = '106'
	elif classificationid == 10 or classificationid == 39:
		#SNIa peculiar
		objtypeid = '100'
	elif classificationid == 11 or classificationid == 40:
		#SNIb
		objtypeid = '4'
	elif classificationid == 12 or classificationid == 41:
		#SNIbn
		objtypeid = '9'
	elif classificationid == 13 or classificationid == 42:
		#SNIb/c
		objtypeid = '6'
	elif classificationid == 14 or classificationid == 43:
		#SNIc
		objtypeid = '5'
	elif classificationid == 15 or classificationid == 44:
		#SNIcBL
		objtypeid = '7'
	elif classificationid == 16 or classificationid == 45:
		#SNI-faint
		objtypeid = '15'
	elif classificationid == 17 or classificationid == 46:
		#SNII
		objtypeid = '10'
	elif classificationid == 18 or classificationid == 47:
		#SNIIP
		objtypeid = '11'
	elif classificationid == 19 or classificationid == 48:
		#SNIIL
		objtypeid = '12'
	elif classificationid == 20 or classificationid == 49:
		#SNIIb
		objtypeid = '14'
	elif classificationid == 21 or classificationid == 50:
		#SNIIn
		objtypeid = '13'
	elif classificationid == 22 or classificationid == 51:
		#SLSNI
		objtypeid = '18'
	elif classificationid == 23 or classificationid == 52:
		#SLSNII
		objtypeid = '19'
	elif classificationid == 24 or classificationid == 53:
		#SLSN-R
		objtypeid = '20'
	elif classificationid == 25 or classificationid == 54:
		#Nova
		objtypeid = '26'
	elif classificationid == 26 or classificationid == 55:
		#ILRN/ILRT
		objtypeid = '25'
	elif classificationid == 27 or classificationid == 56:
		#TDE
		objtypeid = '120'
	elif classificationid == 28 or classificationid == 57:
		#Afterglow
		objtypeid = '23'
	elif classificationid == 29 or classificationid == 58:
		#AGN
		objtypeid = '29'
	elif classificationid == 30 or classificationid == 59:
		#LBV
		objtypeid = '24'
	elif classificationid == 31 or classificationid == 60:
		#CV
		objtypeid = '27'
	elif classificationid == 32 or classificationid == 61:
		#Varstar
		objtypeid = '28'
	elif classificationid == 62 or classificationid == 63:
		#SNIa02eslike but just registering as Iapec
		objtypeid = '100'
	elif classificationid == 64:
		#Galaxy
		objtypeid = '30'
	elif classificationid == 65 or classificationid == 66:
		#Kilonova
		objtypeid = '70'
	else:
		objtypeid = '0'

	return objtypeid

if __name__ == '__main__':
	find(classificationid)

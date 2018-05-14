#!/usr/bin/env python

import argparse
import os
import sys
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
import lookup_instid
import lookup_objtypeID

#Things you might want to change later:
#Accessing SN SQL server:
h = 'supernova.science.lco.global'
u = 'supernova'
D = 'supernova'
p = 'supernova'

parser = argparse.ArgumentParser(description='tar together the spectra of a supernova to send to wiserep.')
parser.add_argument('-n', type=str, help='name of the supernova')
parser.add_argument('-e', type=str, help='enter epochs of spectra you want e.g. 20180101-20180430')
parser.add_argument('--all', action = 'store_true', help='get all spectra')

args = parser.parse_args()

name = vars(args)['n']
epochs = vars(args)['e']
get_all = vars(args)['all']

#Set up connection to sn database
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0' % (u,p,h,D))
connection = engine.connect()
Base = declarative_base()
metadata = MetaData(bind=engine)

#Set up tables I'll use
class spec(Base):
	__table__ = Table('spec', metadata, autoload=True)
class targets(Base):
	__table__ = Table('targets', metadata, autoload=True)
class targetnames(Base):
	__table__ = Table('targetnames', metadata, autoload=True)

session = create_session(bind=engine)

#Get targetid
try:
	targetid = session.query(targetnames).filter_by(name=name).first().targetid
except AttributeError:
	print
	print "Error: no supernova of that name in the database."
	print
	sys.exit()
	
####################
#tar spectra together

#Get filepaths of fits spectra
fits_list = []

if get_all:
	criteria = (spec.targetid == targetid)
else:
	#Use epochs
	date1 = epochs.rsplit('-')[0]
	date2 = epochs.rsplit('-')[1]
	criteria = (spec.targetid == targetid) & (spec.dateobs >= date1) & (spec.dateobs <= date2)

spec_list = session.query(spec).filter(criteria)

for spectrum in spec_list:
	full_filepath = spectrum.filepath + spectrum.filename
	fits_list.append(full_filepath)

#Also get ascii spectra
ascii_list = []
for fits_spec in fits_list:
	ascii_spec = fits_spec.rsplit('.',1)[0]+'.ascii'
	if os.path.exists(ascii_spec):
		ascii_list.append(ascii_spec)
	else:
		print ".fits spec with no associated .ascii, removing %s" % (fits_spec)
		fits_list.remove(fits_spec)

filelist = fits_list + ascii_list

print
print "%i spectra found (%i .fits, %i .ascii)" % (len(filelist),len(fits_list),len(ascii_list))
print

#tar files together
tar_command = 'tar -zcvf %s_LCO_spectra.tar.gz' % (name)

for string in filelist:
         filepath = string.rsplit('/',1)[0]
         filename = string.rsplit('/',1)[1]
         tar_command += ' -C %s/ ./%s' % (filepath,filename)

os.system(tar_command)

print
print 'Spectra collected in %s_LCO_spectra.tar.gz' % (name)
print

####################
#Deal with the weird tsv metadata file

metadata = ['Obj-name\tAscii-filename\tFITS-filename\tObs-date [YYYY-MM-DD]\tObs-UT [HH:MM:SS]\tInst-Id\tObserver/s\tExptime\tSlit\tReducer/s\tReduction-date\tQuality [Rapid/Final/Low/Med/High]\tSpec-Type [Object/Host/Sky/Arcs/Synthetic]\tSpec-Remarks\tPublish\tContrib\tAirmass\tDichroic\tGrism\tGrating\tObj-RA\tObj-DEC\tIAU-name\tObj-type-Id\tRedshift\tHost\tRelated-file1\tRelated-file2']
metadata.append(' \t \t[NULL]\t \t[NULL]\t[NULL]\t[Unkown]\t[0]\t[0]\t[Unknown]\t[Obs-date]\t[NULL]\t[NULL=default=object]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]\t[NULL]')

#Getting necessary info for each spectra
speclist = session.query(spec).filter_by(targetid=targetid)

#Get IAU name
namelist = session.query(targetnames).filter_by(targetid=targetid)
for possible_IAU in [x.name for x in namelist]:
	if 'SN' in possible_IAU and ' ' not in possible_IAU:
		IAUname = possible_IAU

try:
	IAUname
except NameError:
	IAUname = 'NULL'

for spectrum in speclist:
	obj_name = name
	FITS_filename = spectrum.filename
	ascii_filename = FITS_filename.rsplit('.',1)[0]+'.ascii'
	Obs_date = spectrum.dateobs
	Obs_UT = spectrum.ut
	Inst_Id = lookup_instid.find(spectrum.instrument, spectrum.telescope)
	Observer = spectrum.observer
	if Observer == None:
		Observer = 'Las Cumbres Observatory'
	Exptime = spectrum.exptime
	Slit = spectrum.slit
	Reducer = spectrum.reducer
	Reduction_date = spectrum.datecreated
	Quality = 'NULL'
	Spec_type = 'Object'
	Spec_remarks = 'NULL'
	Publish = 'NULL'
	Contrib = 'NULL'
	Airmass = spectrum.airmass
	Dichroic = 'NULL'
	Grism = spectrum.grism
	Grating = 'NULL'
	Obj_RA = spectrum.ra0
	Obj_Dec = spectrum.dec0

	#Need to lookup id numbers from wiserep site
	classificationid = session.query(targets).filter_by(id=targetid).first().classificationid
	Obj_type_Id = lookup_objtypeID.find(classificationid)
	
	Redshift = session.query(targets).filter_by(id=targetid).first().redshift
	Host = 'NULL'
	Related_file1 = 'NULL'
	Related_file2 = 'NULL'
	
	new_line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (obj_name, ascii_filename, FITS_filename, Obs_date, Obs_UT, Inst_Id, Observer, Exptime, Slit, Reducer, Reduction_date, Quality, Spec_type, Spec_remarks, Publish, Contrib, Airmass, Dichroic, Grism, Grating, Obj_RA, Obj_Dec, IAUname, Obj_type_Id, Redshift, Host, Related_file1, Related_file2)
	metadata.append(new_line)

#Writing the tsv file
tsv_file = open('%s_LCO_metadata.tsv' % (name),'w')
for item in metadata:
	tsv_file.write('%s\n' % item)

print 'Metadata written to %s_LCO_metadata.tsv' % (name)

connection.close()
print

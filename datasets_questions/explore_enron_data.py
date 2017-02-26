#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
#from .. import *
import sys
sys.path.insert(1, "../tools")

import feature_format as f


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
counter = 0
poi = 0
total = 0
person = ''
salary  = 0
emails = 0
for data in enron_data:
	counter = counter + 1
	if enron_data[data]['poi']:
		poi = poi + 1
	if 'PRENTICE' in data:
		print "James Prentice stocks {}".format(enron_data[data]['total_stock_value'])
	if 'COLWELL' in data:
		print "COLWELL from_this_person_to_poi {}".format(enron_data[data]['from_this_person_to_poi'])
	if 'SKILLING' in data:
		print "{}  {}".format(data, enron_data[data]['exercised_stock_options'])
	if ('FASTOW' in data) or ('SKILLING' in data) or ('LAY' in data):
		if enron_data[data]['total_payments'] > total:
			total = enron_data[data]['total_payments']
			person = data
	if math.isnan(float(enron_data[data]['salary'])):
		salary = salary + 1
	if enron_data[data]['email_address'] and  enron_data[data]['email_address'] != 'NaN' :
		emails = emails + 1
	#print len(enron_data[data])
print counter
print poi
print "{} {}".format(person, total)
print "Salary not nan {}".format(146-salary)
print "emails not nan {}".format(emails)

tmp_list = []
for key, v in enron_data['SKILLING JEFFREY K'].items():
		#print "key:{}, v: {}".format(key, v)
		tmp_list.append(key)

print tmp_list

#for data in enron_data:
#	for key, v in enron_data[data].items():
#		print "key:{}, v: {}".format(key, v)
print f.featureFormat(enron_data, tmp_list);



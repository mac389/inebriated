import json 

from pyexcel_xls import get_data

data = json.loads(json.dumps(get_data("../data/fb20.age_categories.gender_adjusted.rmatrix.top100s.xls")))
db = {}

for age_range,sheet in data.iteritems():
	db[age_range] = {}
	#Format of item in each list -- (feature r p feature r p)
	for item in sheet:
		db[age_range][item[0]] = item[1]
		db[age_range][item[3]] = item[4]

json.dump(db,open('../data/db.json','wb'))
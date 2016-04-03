def updateTerm(phr, timestamp):
	#first set up access to the term collection in MongoDB
	import pymongo
	connection=pymongo.Connection()
	term=connection.hs.trm2.h 
	#check to see if this is a new hot term
	if phr not in term.find().distinct('term'):
		rdoc = { 'term':phr,
				'sthotd':util.parse.makeDateTime(timestamp),
				'ehotd':util.parse.makeDateTime(timestamp),
		}
		term.insert(rdoc)
	#otherwise update the collection with the new end time.
	else:
		term.update({"term":phr},
		{'$set':{"ehotd":util.parse.makeDateTime(timestamp)}})
import time
todaystring=time.strftime('%Y-%m-%d:%H:00:00')
#loop over the hot phrases and update the database of terms
for phrase in getHotResults():
	updateTerm(phrase,todaystring)


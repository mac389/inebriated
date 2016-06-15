__author__ = 'mac389'
import json, re 

class EstimateAge(object):
	def __init__(self,texts):
		self.texts = texts
		self.age_estimates = [None for _ in xrange(len(self.texts))] #To have default value

		self.keywords = json.load(open('../data/db.json','rb'))
		self.estimate()

	def __repr__(self):
		return "Estimating Age using Facebook."

	def estimate(self):
		for i,text in enumerate(self.texts):
			self.odds = {age_range:None for age_range in self.keywords.keys()}
			for age_range in self.keywords.iterkeys():
				txt = text #Reset text for each sheet
				estimate = 0
				for word, correlation in self.keywords[age_range].iteritems():
					if word+' ' in txt or txt.endswith(word): #Using Regular Expressions is difficult with all those emoticons
						#This simulates word boundaries
						estimate += correlation
						txt = txt.replace(word,'')
				
				self.odds[age_range] = estimate

			self.age_estimates[i] = self.odds


	def __iter__(self):
		for i in xrange(len(self.texts)):
			age_estimate = self.age_estimates[i]
			print self.texts[i] + ' 13-18:%.04f 19-22:%.04f 23-29:%.04f Over 30:%.04f'%(age_estimate['a1318'],age_estimate['a1922'],
						age_estimate['a2329'],age_estimate['a30'])
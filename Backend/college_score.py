# coding=utf-8
import datadotworld as dw
def college_score(name):
	dataset_key = 'https://data.world/education/university-rankings-2017'
	try:
		results = dw.query(dataset_key=dataset_key, query="SELECT *FROM national_universities_rankings WHERE name = '%s'" % name)
		df = results.dataframe
		rank = (df.iloc[0]['rank'])
		score=1
		if rank<=5:
			score = 6
		if rank<=10:
			score = 5
		if rank > 50 & rank<100:
			score = 4
		if rank >100 & rank<150:
			score = 3
		if rank >150 & rank<200:
			score = 2
		if rank > 200:
			score = 1
		return score
	except:
		print("Your College Isn't In Here!!")


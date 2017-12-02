# coding=utf-8
import datadotworld as dw
import pandas as pd
def college_score(name):
	dataset_key = 'https://data.world/education/university-rankings-2017'
	results = dw.query(dataset_key=dataset_key, query="SELECT *FROM national_universities_rankings WHERE name = '%s'" % name)
	df = results.dataframe
	rank = (df.iloc[0]['rank'])
	if rank<50:
		score=20
	elif rank >50 & rank<100:
		score = 15
	elif rank >100 & rank<150:
		score = 10
	elif rank >150 & rank<200:
		score = 5
	else:
		score = 0
	return score
college_score("Princeton University")



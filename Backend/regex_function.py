# coding=utf-8
import re
def regex_processing():
	str= "Hi My name is Sheldon Cooper and I have 11 years of experience working with Accenture, I have mathematics and statistics background. I have completed my doctorate from MIT University. I have experience with auto domain and currently have CTC of  $170000."


	name = re.search(r'name is \w+\s+\w+', str) #Use Limit
	if name:
		print ('found', name.group())
	else:
		print ('did not find')
	experience= re.findall(r'\d{1,6}', str)
	if experience:
		print (experience[0])
	else:
		print ('did not find')


regex_processing()
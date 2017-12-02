# coding=utf-8
import re
def regex_processing():
	str= "Hi My name is Sheldon Cooper and I have 11 years of experince working with Accenture, I have mathematics and statistics background. I have completed my doctorate from MIT University. I have experience with auto domain and currently have CTC of  $170000."


	name = re.search(r'name is \w+\s+\w+', str) #Use Limit
	if name:
		print ('found', name.group())
	else:
		print ('did not find')
	experience= re.search(r'I have \w+', str)
	if experience:
		print ('found', experience.group())
	else:
		print ('did not find')

	line = "Cats are smarter than dogs"

	matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

	if matchObj:
	   print ("matchObj.group() : ", matchObj.group())
	   print ("matchObj.group(1) : ", matchObj.group(1))
	   print ("matchObj.group(2) : ", matchObj.group(2))
	else:
	   print ("No match!!")

regex_processing()
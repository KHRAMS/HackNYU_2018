# coding=utf-8
import re
def regex_processing(str):

	name = re.findall(r'name is (\w+\s+\w+)', str) #Use Limit
	print(name[0])
	experience= re.findall(r'I have (\d{1,6})', str)
	print(experience[0])
	co = re.findall(r'working with ([\w\.-]+)',str)
	print(co[0])
	degree = re.findall(r'completed my ([\w\.-]+) from', str)
	print(degree[0])
	college = re.findall(r'from ([\w\.-]+)', str)
	print(college[0])
	ctc = re.findall(r'currently have CTC of  \$(\d{1,6})', str)
	if ctc == []:
		ctc = ctc = re.findall(r'currently have CTC of \$(\d{1,6})', str)
	print(ctc)
	return [name[0],experience[0],co[0],degree[0],college[0],ctc[0]]


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
	ctc = re.findall(r'currently have CTC of \$(\d{1,6})', str)
	print(ctc[0])


regex_processing("Hi My name is Sheldon Cooper and I have 11 years of experience working with Accenture, I have mathematics and statistics background. I have completed my doctorate from MIT University. I have experience with auto domain and currently have CTC of $170000.")
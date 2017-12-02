# coding=utf-8
import re
degreeRankings = {'bachelors':1,'masters':2 ,'phd':3,'doctorate':4}
educationRankings = {'mit':4,'columbia':3 ,'cit':2,'california':1}
companyRankings = {'accenture' : 3,'ibm' : 2, 'amazon' : 4}

def regex_processing(str):
    name = re.findall(r'name is (\w+\s+\w+)', str)  # Use Limit
    experience = re.findall(r'I have (\d{1,6})', str)
    co = re.findall(r'working with ([\w\.-]+)', str)
    degree = re.findall(r'completed my ([\w\.-]+) from', str)
    college = re.findall(r'from ([\w\.-]+)', str)
    if re.search(r'currently have CTC of  \$(\d{1,6})', str):
        ctc = re.findall(r'currently have CTC of  \$(\d{1,6})', str)

    if re.search(r'currently have CTC of \$(\d{1,6})', str):
        ctc = re.findall(r'currently have CTC of \$(\d{1,6})', str)

    if re.search(r'my CTC is \$(\d{1,6})', str):
        ctc = re.findall(r'my CTC is \$(\d{1,6})', str)
    if re.search(r'my CTC is  \$(\d{1,6})', str):
        ctc = re.findall(r'my CTC is  \$(\d{1,6})', str)
    return [int(experience[0]), companyRankings[co[0].lower()], degreeRankings[degree[0].lower()], educationRankings[college[0].lower()], int(ctc[0])]

def regex_processing_real(str):
    name = re.findall(r'name is (\w+\s+\w+)', str)  # Use Limit
    experience = re.findall(r'I have (\d{1,6})', str)
    co = re.findall(r'working with ([\w\.-]+)', str)
    degree = re.findall(r'completed my ([\w\.-]+) from', str)
    college = re.findall(r'from ([\w\.-]+)', str)

    return [int(experience[0]), companyRankings[co[0].lower()], degreeRankings[degree[0].lower()], educationRankings[college[0].lower()]]
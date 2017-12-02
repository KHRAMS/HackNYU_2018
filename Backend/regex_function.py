# coding=utf-8
import re
import college_score as cs

degreeRankings = {'bachelors':0,'masters':1 ,'phd':2,'doctorate':3}
educationRankings = {'mit':cs.college_score("Massachusetts Institute of Technology"),'columbia':cs.college_score("Columbia University") ,'cit':cs.college_score("California Institute of Technology"),'california':cs.college_score("California State University--Fresno")}
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
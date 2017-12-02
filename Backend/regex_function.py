# coding=utf-8
import re
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
    return [name[0], experience[0], co[0], degree[0], college[0], ctc[0]]
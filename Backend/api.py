from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import json
import requests
import urllib3
from bs4 import BeautifulSoup

#Processing, don't worry about this
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)


data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('/Users/KrishnanRam/Documents/Same1', '1'))
data = data.append(dataFrameFromDirectory('/Users/KrishnanRam/Documents/Same2', '2'))

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

#API stuff

app = Flask(__name__)
CORS(app) # <-- CORS is necessary for React.js's Axion to be able to use the methods in the api!
api = Api(app)

notes = {}

class Test(Resource):
    def put(self):

        # Parsing. View docs(https://flask-restful.readthedocs.io/en/latest/) if this isn't what you need.
        # parser.add_argument('list', action='append') lets flask know that list an argument that can hold 2+ pieces of data in this data :
        # put('http://localhost:5000/', data={"list" : ["When was Barack Obama's birthday?", "What is 10 plus 5 equal to?"]}).json()
        # With that, you have one piece of metadata associated with 2 or more peice of data(aka a list) that can be indexed
        # args is the main class here, and since list is the subclass(an arg of class args) of args, we can mention it freely
        # and access it like this : args.list. We can index by doing args.list[index]

        parser = reqparse.RequestParser()
        parser.add_argument('input',type=string)
        args = parser.parse_args()
        # print(request.form)
        # print(args.list[0], " ", args.list[1])
        # notes[0] = args.list
        # print("Notes ")


        http = urllib3.PoolManager()
        # url = 'http://api.glassdoor.com/api/api.htm?t.p=233537&t.k=b3Bt5z7OKJs&userip=0.0.0.0&useragent=&format=json&v=1&action=employers&jobTitle="Data Scientist"&q="IBM"'
        #
        # hdr = {'User-Agent': 'Mozilla/5.0'}
        # req = urllib3.Request(url, headers=hdr)
        # response = urllib2.urlopen(req)
        # # soup = BeautifulSoup(response)
       # hdr = {'User-Agent': 'Mozilla/5.0'}

        r = http.request('GET',
                         'http://api.glassdoor.com/api/api.htm?t.p=233537&t.k=b3Bt5z7OKJs&format=json&v=1&action=employers')
        print(r.status)
        print(BeautifulSoup(r.data))
        # print(requests.get(
        #     'http://api.glassdoor.com/api/api.htm?t.p=233537&t.k=b3Bt5z7OKJs&userip=0.0.0.0&format=json&v=1&action=employers&jobTitle="Data Scientist"&q="IBM"').text)
        z = {'output':{'stuff' : args.string}} # Formatting this is important. If you don't format it right,
        return z                                              # React won't get anything/ won't be able to index it.


api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(debug=True)

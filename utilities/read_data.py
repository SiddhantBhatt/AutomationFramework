import csv
import json


def getCSVData(fileName):
    # create empty list
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


def getJSONData(filename):
    data = []
    dataFile = open(filename, "r")
    loadedjson = json.load(dataFile)
    for fields in loadedjson['data']:
        fields = list(fields.values())
        data.append(fields)
    return data


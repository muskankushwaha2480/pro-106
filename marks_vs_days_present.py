import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    days_present = []
    marks_in_percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row['Days Present']))
            marks_in_percentage.append(float(row['Marks In Percentage']))
    return{'x' : days_present , 'y' : marks_in_percentage}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'] , datasource['y'])
    print("The correlation of Days Present vs Marks in Percentage : " , correlation)

def setup():
    data_path = "Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
   
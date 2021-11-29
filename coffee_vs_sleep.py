import csv
import plotly.express as px
import numpy as np

with open("coffee vs sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df , x = 'Coffee in ml' , y = 'sleep in hours' )
    fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{'x' : coffee , 'y' : sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'] , datasource['y'])
    print("The correlation of cups of coffee vs hours of sleep : " , correlation)

def setup():
    data_path = "coffee vs sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
   
import csv
import numpy as np
import plotly.express as px

def getDataSource():
    SizeOfTV=[]
    average=[]
    with open("Data2.csv") as f:
        df=csv.DictReader(f)
        for row in df:
            SizeOfTV.append(float(row["Size of TV"]))
            average.append(float(row["Average"]))
        return{"x":SizeOfTV, "y":average}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("The Correlation Between Size Of TV And Average IS:=>", correlation[0,1]*100)

def setUp():
    dataSource=getDataSource()
    findCorrelation(dataSource)

setUp()
    
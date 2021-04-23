import plotly.express as px
import csv
import numpy as np

def getDataSource():
    marks=[]
    days=[]
    with open("Data3.csv") as f:
        df=csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
        return{"x":marks, "y":days}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("The Correlation Between Marks In Percentage And Days Present Id:=>", correlation[0,1]*100)

def setUp():
    dataSource=getDataSource()
    findCorrelation(dataSource)

setUp()
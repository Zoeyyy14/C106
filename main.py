import plotly.express as px
import csv 
import numpy as np 

def getDataSource():
    icecream_sales=[]
    coldDrink_sales=[]
    with open("Data1.csv") as f:
        df=csv.DictReader(f)
        for row in df:
            icecream_sales.append(float(row["Temperature"]))
            coldDrink_sales.append(float(row["Ice-cream Sales"]))
        return{"x":icecream_sales, "y":coldDrink_sales}
    
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Icecream Sales And Temperature Is:=>", correlation[0,1]*100)
    
def setUp():
    dataSource=getDataSource()
    findCorrelation(dataSource)

setUp()
import csv
import plotly.express as px
with open("Data3.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()
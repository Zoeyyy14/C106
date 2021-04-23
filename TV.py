import csv
import plotly.express as px
with open("Data2.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df, x="Size of TV", y="Average")
    fig.show()
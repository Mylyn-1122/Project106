import csv
import plotly.express as px
import numpy as np



def getDataSource(datapath):
    daysPresent = []
    marks = []


    with open ('./Student-Marks.csv') as csvfile :
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            daysPresent.append(float(row["Days-Present"]))
            marks.append(float(row["Marks"]))


    return {"x":marks, "y":daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Marks and days present ", correlation[0,1])

def plotFigure(dataPath):
    with open (dataPath)as csvfile :
        df = csv.DictReader(csvfile)
        fig = px.scatter(df, x = "Marks", y = "Days-Present")
        fig.show()

def setup():
    dataPath = "./Student-Marks.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)



setup()

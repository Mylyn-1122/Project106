import csv
import plotly.express as px
import numpy as np



def getDataSource(datapath):
    sleep = []
    coffee = []


    with open ('./coffee.csv') as csvfile :
        csvReader = csv.DictReader(csvfile)
        for row in csvReader:
            sleep.append(float(row["sleep"]))
            coffee.append(float(row["Coffee"]))


    return {"x":coffee, "y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between amountof coffee and sleep ", correlation[0,1])

def plotFigure(dataPath):
    with open (dataPath)as csvfile :
        df = csv.DictReader(csvfile)
        fig = px.scatter(df, x = "Coffee", y = "sleep")
        fig.show()

def setup():
    dataPath = "./coffee.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)



setup()
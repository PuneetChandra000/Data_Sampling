import pandas as pd
import plotly.figure_factory as pff
import statistics as st
import random

data = pd.read_csv("data.csv")

temp = data["temp"].tolist()

dataset = []

n = len(temp)

datasetFor100 = []

for j in range(100) :
    dataset = []

    for i in range(100) :
        dataset.append(random.choice(temp))
        
    datasetFor100.append(st.mean(dataset))

meanOf100 = st.mean(datasetFor100)
stdevOf100 = st.stdev(datasetFor100)


print("Mean of 100 mean of means (sample) :- " , meanOf100)
print("std deviation of 100 mean of means  (sample) :- ", stdevOf100)

print("-------------------------------------------------------------------------------------------")

graph = pff.create_distplot([datasetFor100], ["graph"], show_hist = False) 
graph.show()




















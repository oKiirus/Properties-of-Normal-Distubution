import csv
import pandas as pd
import plotly.figure_factory as px
import statistics as st


rolls = pd.read_csv('yes.csv')
rolls = rolls['height'].tolist()

graph = px.create_distplot([rolls], ['height'])

graph.show()


mean = st.mean(rolls)
median = st.median(rolls)
mode = st.mode(rolls)
standard = st.stdev(rolls)

points = []

for e in rolls:
    if float(e) > (mean - standard) and float(e) < (mean + standard):
        points.append(e)

points2 = []

for e in rolls:
    if float(e) > (mean - standard * 2) and float(e) < (mean + standard * 2):
        points2.append(e)

points3 = []

for e in rolls:
    if float(e) > (mean - standard * 3) and float(e) < (mean + standard * 3):
        points3.append(e)

  
def magic(num):
    return (len(num) / len(rolls)) * 100  

print(magic(points), magic(points2), magic(points3))







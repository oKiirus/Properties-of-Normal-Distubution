import random as rd
import plotly.figure_factory as px
import statistics as st

rolls = []



for i in range(0, 1000):
    dice1 = rd.randint(1, 6)
    dice2 = rd.randint(1, 6)

    rolls.append(dice1 + dice2)

    

graph = px.create_distplot([rolls], ['hi'])

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

    

print((len(points3) / len(rolls)) * 100)



import pandas as pd
import statistics as s
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np

data = pd.read_csv('main.csv')
toefl = data['TOEFL Score'].to_list()
chance = data['Chance of Admit '].to_list()
scatter = px.scatter(x=toefl,y=chance)
#scatter.show()

toefl_array = np.array(toefl)
chance_array = np.array(chance)
m,c = np.polyfit(toefl_array,chance_array,1)

y_array = []
for i in toefl_array:
    y = m*i + c
    y_array.append(y)

scatter2 = px.scatter(x=toefl_array,y=chance_array)
scatter2.update_layout(shapes = [dict(type='line',y0=min(chance_array),y1=max(chance_array),x0=min(toefl_array),x1=max(toefl_array))])
scatter2.show()
print(f'the values of intercept and slope is {c} and {m}')

x = 115
y = m*x + c
print(f'the chances of admit for a person with toefl score 115 is {y}')
print(f'the value of the bestfit line using the computer algorithm is {max(y_array)}')
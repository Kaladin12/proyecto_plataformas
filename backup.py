import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

PATH =  r"D:\Documents\datasets\datasets"
FILES = os.listdir(PATH)

datasets = {
    name[:-4] : pd.read_csv(PATH+r'\\'+name) for name in FILES
}

datasets.keys()

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Load data
data = pd.read_csv("./datasets/population_edited.csv")

# All united states data
usa = data[data["Entity"] == "United States"]

# All china data
chn = data[data["Entity"] == "China"]


slider = []
scl = [[0.0, '#ffffff'],[0.2, '#b4a8ce'],[0.4, '#8573a9'],
       [0.6, '#7159a3'],[0.8, '#5732a1'],[1.0, '#2c0579']] # purples
for year in data['Year'].unique():
    segmented = data[data['Year']==year]

    data_each = dict(
        type = 'choropleth',
        locations = segmented['Code'],
        z = segmented['Population (historical estimates)'].astype(float),
        locationmode = 'ISO-3',
        colorscale = scl,
        colorbar = {'title':'Population (historical estimates)'}
    )
    slider.append(data_each)


steps = []
for i in range(len(slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(slider)],
                label='Year {}'.format(i + 1800))
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

layout = dict(title ='UFO Sightings by State Since 1998', geo=dict(scope='world',
                       projection={'type': 'mercator'}),
              sliders=sliders)

fig = go.Figure(data=slider, layout=layout)
fig.show()

# Population tendency graph for United Sates
x_axis = usa["Year"]
y_axis = usa["Population (historical estimates)"]
fig = px.line(x=x_axis, y=y_axis, title="Population Grouth Graph of USA (1800-2020)")
fig.update_xaxes(title="Year")
fig.update_yaxes(title="Population")

# Population tendency graph for United Sates
x_axis = chn["Year"]
y_axis = chn["Population (historical estimates)"]
fig = px.line(x=x_axis, y=y_axis, title="Population Grouth Graph of China (1800-2020)")
fig.update_xaxes(title="Year")
fig.update_yaxes(title="Population")

trace1 = go.Scatter(
    name = "USA",
    x = list(usa["Year"]),
    y = list(usa["Population (historical estimates)"])
)

trace2 = go.Scatter(
    name = "CHINA",
    x = list(chn["Year"]),
    y = list(chn["Population (historical estimates)"])
)

layout = go.Layout(
    title = "Population Growth",
    yaxis = dict(title='Population'),
    xaxis = dict(title = "Year")
    )

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
fig


population = pd.read_csv('./datasets/urban-vs-rural-majority.csv')
# All united states data
usa = population[population["Entity"] == "United States"]

# All china data
chn = population[population["Entity"] == "China"]

trace1 = go.Scatter(
    name = "USA",
    x = list(usa["Year"]),
    y = list(usa["Urban population (%) long-run with 2050 projections (OWID)"])
)

trace2 = go.Scatter(
    name = "CHINA",
    x = list(chn["Year"]),
    y = list(chn["Urban population (%) long-run with 2050 projections (OWID)"])
)

trace3 = go.Scatter(
    name = "CHINA",
    x = np.linspace(1500, 2020),
    y = [50 for _ in range(2020-1500)]
)

layout = go.Layout(
    title = "Urban Population Percentage Growth",
    yaxis = dict(title='Urban Population %'),
    xaxis = dict(title = "Year"),
    shapes = [
        {'type':'rect', 'x0':1500, 'y0':50, 'x1':2050, 'y1':50, 'line':{ 'dash':'dash' }},
        {'type':'rect', 'x0':2020, 'y0':0, 'x1':2020, 'y1':100, 'line':{ 'dash':'dash' }}
        ]
    )

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
fig
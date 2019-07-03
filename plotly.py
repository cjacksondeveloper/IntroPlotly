# use offline version of plotly
import plotly.offline as py
py.init_notebook_mode(connected=False)

# import graph objects as "go"
import plotly.graph_objs as go

# import pandas for data munging
import pandas as pd
import json

trace1 = go.Scatter(
name = 'Blue',
x = [1,2], y = [1,2])

trace2 = go.Scatter(
name = 'Orange',
x = [2,1], y = [1,2])

layout = go.Layout(
showlegend=True,
legend = dict (
x = 1, y = 0),

    title=go.layout.Title(
        text='Blue and Orange lines',
        xref='paper',
        x=0
    ),
    #Working on the xaxis format
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='x Axis',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='red'
            )
        )
    ),
    
#Working on the yaxis format
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='y Axis',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='red'
            )
        )
    )

)

data = [trace1, trace2]

fig = go.Figure(
data=data,
layout=layout)

py.iplot(fig)

hide_toggle()

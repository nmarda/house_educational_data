import plotly.plotly as py
import plotly.graph_objs as go

# trace1 = {"x": [161/435.0, 31/435.0, 42/435.0, 18/435.0], 
#           "y": ["JD", "MBA", "MA", "MS"], 
#           "marker": {"color": "pink", "size": 12}, 
#           "mode": "markers", 
#           "name": "Percent of 115th House with degree", 
#           "type": "scatter"
# }

# trace2 = {"x": [156/435.0, 39/435.0, 47/435.0, 25/435.0], 
#           "y": ["JD", "MBA", "MA", "MS"], 
#           "marker": {"color": "blue", "size": 12}, 
#           "mode": "markers", 
#           "name": "Percent of 116th House with degree", 
#           "type": "scatter", 
# }


trace1 = {"x": [100, 100*161/435.0, 100*0.6, 100*22/435.0], 
          "y": ["Bachelors", "JD", "Masters", "PhD"], 
          "marker": {"color": "pink", "size": 12}, 
          "mode": "markers", 
          "name": "Percent of 115th House with degree", 
          "type": "scatter"
}

trace2 = {"x": [33, 0.4, 8, 2], 
          "y": ["Bachelors", "JD", "Masters", "PhD"],
          "marker": {"color": "blue", "size": 12}, 
          "mode": "markers", 
          "name": "Percent of Americans with degree", 
          "type": "scatter", 
}

data = [trace1, trace2]
layout = {"title": "Educational attainment of the 115th and 116th House of Representatives", 
          "xaxis": {"title": "Percentage", }, 
          "yaxis": {"title": "Degree"}}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filenmae='basic_dot-plot')

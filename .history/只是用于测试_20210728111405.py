import plotly.plotly as py
from plotly import tools
from plotly.graph_objs import *

tools.set_credentials_file(username='yours', api_key='yours')

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    mode='markers'
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.iplot(data)

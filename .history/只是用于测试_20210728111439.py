import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

data = [Bar(x=df.School,
            y=df.Gap)]

py.iplot(data)

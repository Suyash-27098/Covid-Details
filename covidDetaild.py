from datetime import date
import pandas as pd
import plotly.express as px
from six import MAXSIZE

df = pd.read_csv("Copy+of+data+-+data.csv")
bar_graph = px.scatter(df, x="date", y="cases", color="country", size_max=60)
bar_graph.show()
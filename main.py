import pandas as pd
import plotly.express as px

df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 104\Copy+of+data+-+data.csv')
fig = px.scatter(df,x='date',y='cases', color='country')
fig.show()
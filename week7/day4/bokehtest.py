import pandas as pd
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

# Load the CSV file into a pandas dataframe
df = pd.read_csv("week7/day4/statsfinal.csv")

# create a new date column from the date string column

df["date_new"] = pd.to_datetime(df["Date"], "coerce")

print(df.head())

# create a bar chart with the data from the dataframe column Q-P1 and the Year from the date_new column

df["Year"] = pd.DatetimeIndex(df["date_new"]).year

grouped = df.groupby("Year")["Q-P1"].sum()

p = figure(x_range=list(grouped.index), plot_height=350, title="Yearly Q-P1 Total")
p.vbar(x=list(grouped.index), top=grouped.values, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = "Year"
p.yaxis.axis_label = "Q-P1"

# Display the chart
show(p)

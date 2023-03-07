import pandas as pd
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure

# Load the CSV file into a pandas dataframe
df = pd.read_csv(
    "/Users/sebastienarokeum/Desktop/devi/DI_Bootcamp/week7/day4/statsfinal.csv"
)


def convert_date(df):
    df["newdate"] = pd.to_datetime(df["Date"], "coerce")
    df["newyear"] = df["newdate"].dt.year
    df["quarter"] = df["newdate"].dt.quarter
    df["month"] = df["newdate"].dt.month
    df["day"] = df["newdate"].dt.day


convert_date(df)

# Create a ColumnDataSource object
source = ColumnDataSource(data=df)

# Create a bar chart
p = figure(x_range=list(df["newyear"].unique()), plot_height=350, title="Q-p1 Total")
bars = p.vbar(x="newyear", top="Q-p1", source=source, width=0.9)


# Define the update function for the dropdown menu
def update(attr, old, new):
    if select.value == "Year":
        x = "newyear"
    elif select.value == "Quarter":
        x = "quarter"
    else:
        x = "month"
    bars.data_source.data["x"] = df[x]


# Create a dropdown menu for selecting the time period
options = ["Year", "Quarter", "Month"]
select = Select(title="Time Period", options=options)
select.on_change("value", update)

# Create a layout for the chart and dropdown menu
layout = column(select, p)

# Display the chart and dropdown menu
show(layout)

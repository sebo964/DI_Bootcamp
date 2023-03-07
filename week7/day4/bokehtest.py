import pandas as pd
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.models import Label


# Load the CSV file into a pandas dataframe
df = pd.read_csv(
    "/Users/sebastienarokeum/Desktop/devi/DI_Bootcamp/week7/day4/statsfinal.csv"
)

# Convert the 'Date' column to a datetime type and add the converted date time to a new column New_date
df["Date"] = pd.to_datetime(df["Date"], format="%D-%M-%Y", errors="coerce")

df["New_Date"] = df["Date"].dt.to_period("M").dt.to_timestamp()
# Create a Bokeh ColumnDataSource from the pandas dataframe
source = ColumnDataSource(df)

# Create a Bokeh figure
p = figure(x_axis_type="datetime", title="Q-P1")
p.vbar(
    x="New_Date", top="Q-P1", source=source, width=31 * 24 * 60 * 60 * 1000
)  # 1 month width


# Define the callback function for the slider
def update(attr, old, new):
    if new == 1:
        p.xaxis.major_label_overrides = {
            i: date.strftime("%Y-%m-%d")
            for i, date in enumerate(
                pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="Q")
            )
        }
        p.xaxis.ticker = [
            date.timestamp() * 1000
            for date in pd.date_range(
                start=df["Date"].min(), end=df["Date"].max(), freq="Q"
            )
        ]
        p.xaxis.major_label_orientation = 1
        p.xaxis.axis_label = "Quarterly"
        p.vbar(
            x="Date", top="Q-P1", source=source, width=3 * 31 * 24 * 60 * 60 * 1000
        )  # 3 months width
    elif new == 2:
        p.xaxis.major_label_overrides = {
            i: date.strftime("%Y-%m-%d")
            for i, date in enumerate(
                pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="Y")
            )
        }
        p.xaxis.ticker = [
            date.timestamp() * 1000
            for date in pd.date_range(
                start=df["Date"].min(), end=df["Date"].max(), freq="Y"
            )
        ]
        p.xaxis.major_label_orientation = 1
        p.xaxis.axis_label = "Yearly"
        p.vbar(
            x="Date", top="Q-P1", source=source, width=12 * 31 * 24 * 60 * 60 * 1000
        )  # 12 months width
    else:
        p.xaxis.major_label_overrides = {
            i: date.strftime("%Y-%m-%d")
            for i, date in enumerate(
                pd.date_range(start=df["Date"].min(), end=df["Date"].max(), freq="M")
            )
        }
        p.xaxis.ticker = [
            date.timestamp() * 1000
            for date in pd.date_range(
                start=df["Date"].min(), end=df["Date"].max(), freq="M"
            )
        ]
        p.xaxis.major_label_orientation = 1
        p.xaxis.axis_label = "Monthly"
        p.vbar(
            x="Date", top="Q-P1", source=source, width=31 * 24 * 60 * 60 * 1000
        )  # 1 month width


# Create a Bokeh slider
slider = Slider(start=0, end=2, value=0, step=1, title="Grouping")

# Add the slider and the figure to a Bokeh layout
layout = column(slider, p)

# Add the callback function to the slider
show(layout)

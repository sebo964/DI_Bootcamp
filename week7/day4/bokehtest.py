import pandas as pd
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.models import Label


# Load the CSV file into a pandas dataframe
df = pd.read_csv("week7/day4/statsfinal.csv")

# create a new date column from the date string column
df["date_new"] = pd.to_datetime(df["Date"], errors="coerce")

# rename all the columns to remove - and replace with _

df.columns = df.columns.str.replace("-", "_")


# drop the column Unnamed: 0
df = df.drop(columns=["Unnamed: 0"])

# add a year column

df["year"] = df["date_new"].dt.year


print(df.head())

df_sum = df.groupby("year")["Q_P1"].mean().reset_index()

print(df_sum.head())
# Create a figure object
p = figure(
    x_range=(df_sum["year"].min(), df_sum["year"].max()),
    outer_height=350,
    title="Sum of Q-P1 by Year",
)

# Add a vertical bar chart to the figure
p.vbar(x="year", top="Q_P1", width=0.8, source=df_sum)

for index, row in df_sum.iterrows():
    label = Label(x=row["year"], y=row["Q_P1"], text=str(row["Q_P1"]))
    p.add_layout(label)

# Show the plot
show(p)

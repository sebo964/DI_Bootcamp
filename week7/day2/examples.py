# For this exercise, we will use the Titanic dataset

# Use this url to load it, do not download!
# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

# Do the following:

# Define what are the categorical features and what are the continuous features. Be sure to
# define ordinal vs nominal.

# Explore the data. Print any important summary statistics. Plot the distributions of
# each feature. Plot any important relationships of each feature on the target variable or on each other.
# (You can use Seaborn as well)

# Process the data as you’ve learned in the lesson:

# Figure out what you want to do with the nan values
# Figure out the best way to make the categorical features numeric as we’ve learned
# Scale the continuous features and transform or categorize any feature.
# Deal with any outliers (both categorical and continuous)
# Remove any columns you feel are not important and explain why.
# Split the data into train and test sets.
# Do it randomly and also do it by a certain feature. Explain why you chose that feature.
# Don’t forget about stratifying the target variable

# Be creative!


# Back to Top


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

print(df.head())

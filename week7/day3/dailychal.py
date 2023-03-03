import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

print(raw_df.head())

print(raw_df.shape)

number_of_columns = len(raw_df.columns)

# for each column draw a box plot using seaborn


for i in range(number_of_columns):
    sns.boxplot(x=data[:, i])
    # add label for each column
    plt.xlabel(raw_df.columns[i])
    plt.show()

    apply_iqr_rule = np.abs(data[:, i] - np.median(data[:, i])) > 1.5 * np.percentile(
        data[:, i], 75
    ) - np.percentile(data[:, i], 25)

    print(f"Number of outliers for column {i} is {np.sum(apply_iqr_rule)}")


# For each continuous feature, calculate how many outliers there are using the 1.5 * IQR rule.
# (NumPy has a function to calculate Q1 and Q3.) Did it looks similar to the boxplot?
# How would you deal with the outliers in each of these cases?
# i do not have a full picture of the data but i would consider removing the outlier rows from the data set given at most 20% of the rows would be outliers.

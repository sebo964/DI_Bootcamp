import sklearn.linear_model as lm
import pandas as pd

df_lindata = pd.read_csv(
    "/Users/sebastienarokeum/Desktop/devi/DI_Bootcamp/week7/day4/lindata.csv"
)

df_lindata = df_lindata.drop(columns=["Unnamed: 2"])

height = df_lindata["Height"].values.reshape(-1, 1)

weight = df_lindata["\tWeight"]

lr = lm.LinearRegression()

Reg = lr.fit(height, weight)

print(Reg.coef_, Reg.intercept_)

# using height predict the weight

result = Reg.predict([[140]])

print(result)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
sns.catplot("Sex", "Age", data=df, kind="box")
plt.show()

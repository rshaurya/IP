import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3], [6,7,8], [9,10,11]], columns=['class', 'age', 'grade'], index=['labdhi', 'sha', 'mud'])
df.drop(index='sha', inplace=True)
print(df)

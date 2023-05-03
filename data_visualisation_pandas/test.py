import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = pd.read_csv('crypto_dataset/Price-Data/BTC_Bitcoin.csv', usecols=["High", "Low"])
print(names)

names.plot(kind='line', ylabel='Price', xlabel='Index', title='Test')
plt.show()

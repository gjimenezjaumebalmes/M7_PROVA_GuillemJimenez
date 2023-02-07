import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def function1():
    data = pd.read_csv("data.csv", usecols=['NAME','NOTES','YEAR'])
    data = data.dropna()
    data = data.groupby(by='NAME').mean('NOTES')
    data = pd.DataFrame(data, columns=['NAME', 'NOTES'])
    print(data)
    return data

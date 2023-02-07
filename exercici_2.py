
import numpy as np
import pandas as pd

def function2():
    data = pd.read_csv("data.csv", usecols=['NAME','GROUP','MODULE','ABSENCES'])
    data = data.dropna()
    print(data)
    return data

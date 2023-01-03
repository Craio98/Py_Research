import numpy as np
import pandas as pd


fileName="https://github.com/Craio98/Py_Research/raw/main/graph.uhs"
myCSV=pd.read_csv(fileName,skiprows=4)
df=pd.DataFrame(myCSV)
print(df)
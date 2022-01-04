import csv 
import pandas as pd
import math 
df=pd.read_csv("class1.csv")
Marklist=df["Marks"].tolist()
print(Marklist)
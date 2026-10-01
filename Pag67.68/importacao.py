import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])

print(df)
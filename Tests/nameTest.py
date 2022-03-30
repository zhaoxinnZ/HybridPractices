import numpy as np
import pandas as pd
import matplotlib as plot

df_name = pd.read_csv("../../pythonProject4/CSV/names.csv", names=["姓名"])

print(df_name.head())

df_grades = pd.DataFrame(np.random.randint(6, 16, size=(100, 5)), columns=[
    "國文", "英文", "數學", "自然", "社會"])
print(df_grades.head())

df_concated = pd.concat([df_name, df_grades], axis=1)

print(df_concated.head())

df_sum = df_concated.sum(1)

df_concated["總級分"] = df_sum

df_concated["主科"] = df_concated.get("數學")*1.5 + df_concated.get("英文")

df_sortedvalue = df_concated.sort_values(by=["總級分"], ascending=False)

df_sortedvalue1 = df_concated.sort_values(by=["總級分", "主科"], ascending=False)

print(df_sum)

print(df_concated.head())

print(df_sortedvalue.head(20))

print(df_sortedvalue1.head(20))

df_bike = pd.read_csv("../../pythonProject4/CSV/2012.csv",
                      index_col="Date",
                      parse_dates=True,
                      dayfirst=True
                      )
print(df_bike.head())
print(df_bike.shape)

df_sbike = df_bike[["Berri 1", "Maisonneuve 1","Maisonneuve 2"]].copy()
print(df_sbike.shape)
print(df_sbike.describe())
print(df_sbike.plot())
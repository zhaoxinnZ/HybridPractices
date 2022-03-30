import numpy
import numpy as np
import matplotlib as plt
import pandas as pd

df = pd.read_csv("../../pythonProject4/CSV/grades.csv")

mdata = numpy.random.randn(4, 3)

print(mdata)

list("ABC")

df2 = pd.DataFrame(mdata, columns=list("ABC"))
print(df2)

df3 = pd.DataFrame(numpy.random.randn(4, 3), columns=list("ABC"))

df4 = pd.DataFrame(numpy.random.randn(3, 3), columns=list("123"))

df5 = pd.concat([df3, df4], axis=1)

print(df5)

df6 = pd.concat([df3, df4], axis=1)


print(df6)

data_without_nan = df6.dropna(axis=1)
print(data_without_nan)

print(df6.head())

print(df6.iloc[1:2])

print(df[['國文', '英文', '數學', '自然', '社會']].sum(1))






exit()


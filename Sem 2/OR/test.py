from xxlimited import new
import pandas as pd

#/home/jerinpaul/Documents/ME/Sem 1/Data Mining/Iris.csv

#reading the csv
data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/Iris.csv")

print("Read completed")
leng = len(data)

header = data.head(10)
tails = data.tail(10)
joins = header.append(tails)
print(joins)

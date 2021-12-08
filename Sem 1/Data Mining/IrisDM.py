#SepalLengthCm	SepalWidthCm	PetalLengthCm	PetalWidthCm	Species
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

data = pd.read_csv("/home/jerinpaul/Documents/ME/Data Mining/Iris.csv")
features = data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
target = data[["Species"]]

correlation = features.corr(method = 'pearson')
sb.heatmap(correlation, annot = True)
plt.show()
parallel_coordinates(data, "Species", color = ['blue', 'red', 'green'])
plt.show()

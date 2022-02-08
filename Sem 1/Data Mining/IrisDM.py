import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/Iris.csv")

sns.countplot(x = 'class', data = data)
plt.show()

sns.scatterplot(x= 'sepallength', y = 'sepalwidth', hue = 'class', data = data)
plt.legend(bbox_to_anchor = (1, 1), loc = 2)
plt.show()

sns.scatterplot(x= 'petallength', y = 'petalwidth', hue = 'class', data = data)
plt.legend(bbox_to_anchor = (1, 1), loc = 2)
plt.show()

sns.pairplot(data = data, hue='class', height = 2)
plt.show()

plot = sns.FacetGrid(data, hue="class")
plot.map(sns.distplot, "sepallength").add_legend()
plot = sns.FacetGrid(data, hue="class")
plot.map(sns.distplot, "sepalwidth").add_legend()
plot = sns.FacetGrid(data, hue="class")
plot.map(sns.distplot, "petallength").add_legend()
plot = sns.FacetGrid(data, hue="class")
plot.map(sns.distplot, "petalwidth").add_legend()
plt.show()

print(data.corr(method = 'pearson'))
sns.heatmap(data.corr(method='pearson'), annot = True)
plt.show()


array = data.values
X = array[:,0:4]
Y = array[:,4]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('NB', GaussianNB()))

result = []

for name, alg in models:
    temp = []
    predicted = alg.fit(x_train, y_train).predict(x_test)
    temp.append(name)
    temp.append(round(alg.score(x_train, y_train), 4))
    temp.append(round(alg.score(x_test, y_test), 4))
    temp.append(round(precision_score(y_test, predicted, average='micro'), 4))
    temp.append(round(recall_score(y_test, predicted, average='micro'), 4))
    temp.append(round(metrics.accuracy_score(y_test, predicted), 4))
    result.append(temp)

print("\nAlgorithm \t Traning \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

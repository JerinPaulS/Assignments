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
from sklearn.metrics import confusion_matrix

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/Iris.csv")

array = data.values
X = array[:,0:4]
Y = array[:,4]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.8, random_state=0)

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
    cm = confusion_matrix(y_test, predicted)
    print(cm)

print("\nAlgorithm \t Traning \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

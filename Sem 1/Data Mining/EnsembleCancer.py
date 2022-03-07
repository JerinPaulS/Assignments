import collections

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import VotingClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics, model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/cancer.csv")
data.drop(['Sample Code Number'], axis=1, inplace=True)

#print(data.describe())
#print(data.info())
#print(data.head())
data.replace('?', 0, inplace=True)

values = data.values
imputer = SimpleImputer()
imputedData = imputer.fit_transform(values)

scaler = MinMaxScaler(feature_range=(0, 1))
normalizedData = scaler.fit_transform(imputedData)

models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('GNB', GaussianNB()))
models.append(('LGR', LogisticRegression()))
models.append(('DTC', DecisionTreeClassifier()))
models.append(('SVC', SVC()))

trained_models = []
for model in models:
    sample = DataFrame(normalizedData).sample(n=200)
    sample = sample.to_numpy()
    X = sample[:, 0:9]
    Y = sample[:, 9]
    trained_models.append(model[1].fit(X, Y))


sample = DataFrame(normalizedData).sample(n=140)
sample = sample.to_numpy()
X = sample[:, 0:9]
Y = sample[:, 9]

mapping = []
voted_pred = []
for index, val in enumerate(Y):
    x = X[index]
    temp = collections.defaultdict(int)
    for trained_model in trained_models:
        predicted = trained_model.predict([x])
        #print(predicted)
        temp[predicted[0]] += 1
    max_pred = max(temp.values())
    result = None
    for key in temp:
        if temp[key] == max_pred:
            result = key
            break
    voted_pred.append(result)

print("The accuracy of the ensemble model is = ", round(metrics.accuracy_score(Y, voted_pred), 4))


'''
kfold = model_selection.KFold(n_splits=10, random_state=7, shuffle=True)
ensemble = VotingClassifier(models)
results = model_selection.cross_val_score(ensemble, X, Y, cv=kfold)
print("Mean of all models' accuracy = " + str(results.mean()))
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')
warnings.warn('DelftStack')
warnings.warn('Do not show this message')

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/diabetes_data_upload.csv")

df = data.copy()

positive = df.loc[df['class'] == "Positive"]
negative = df.loc[df['class'] == "Negative"]
count = abs(len(positive) - len(negative))

oversampling = negative.sample(n = count, replace = False)
undersampling = positive.sample(n = count, replace = False)
#df.drop(undersampling.index, axis = 0,inplace = True)

df = pd.concat([oversampling, df], ignore_index = True, sort = False)
#print(len(df[df["class"] == "Positive"]), len(df[df["class"] == "Negative"]))

df['Gender'] = df['Gender'].replace('Female', 1)
df['Gender'] = df['Gender'].replace('Male', 0)

for column in df.columns.drop(['Age', 'Gender', 'class']):
     df[column]= df[column].replace('No', 0)
     df[column]= df[column].replace('Yes', 1)

df['class'] = df ['class'].replace('Positive', 1)
df['class'] = df ['class'].replace('Negative', 0 )

models = []
models.append(('DT', DecisionTreeClassifier(criterion = "entropy", splitter = "best")))
models.append(('LR', LogisticRegression(solver = 'liblinear', random_state = 0)))
#models.append(('LR', LogisticRegression()))
models.append(('KN', KNeighborsClassifier(n_neighbors = 10)))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(kernel = 'poly', degree = 2)))
#models.append(('SVM', SVC()))

print(df.head)

y = df["class"]
x = df.drop("class", axis = 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, shuffle = True, random_state = 0)
scaler = StandardScaler()
x_train = pd.DataFrame(scaler.fit_transform(x_train), index = x_train.index , columns = x_train.columns)

result = []
for name, alg in models:
    #           confusion_matrix
    #       TP              FP
    #       FN              TN
    temp = []
    predicted = alg.fit(x_train, y_train).predict(x_test)
    temp.append(name)
    cm = confusion_matrix(y_test, predicted)
    TP = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]
    TN = cm[1][1]
    print(cm)
    temp.append(round(alg.score(x_train, y_train), 4))
    temp.append(round(alg.score(x_test, y_test), 4))
    temp.append(round(TP / (TP + FP), 4))
    temp.append(round(TP / (TP + FN), 4))
    temp.append(round((TP + TN) / (TP + FP + TN + FN), 4))
    result.append(temp)

print("\nAlgorithm \t Traning \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

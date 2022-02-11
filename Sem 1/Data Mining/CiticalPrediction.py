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

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/diabetes_data_upload.csv")

df = data.copy()
df['Gender'] = df['Gender'].replace('Female', 0)
df['Gender'] = df['Gender'].replace('Male', 1)

for column in df.columns.drop(['Age', 'Gender', 'class']):
     df[column]= df[column].replace('No', 0)
     df[column]= df[column].replace('Yes', 1)

df['class'] = df ['class'].replace('Positive', 0)
df['class'] = df ['class'].replace('Negative', 1 )

train_sizes = list(range(40, 90, 1))
train_sizes = [x / 100 for x in train_sizes]
random_states = list(range(0, 200, 4))
random_statesrev = list(range(200, 0, -4))
#print(len(train_sizes), len(random_states), len(random_statesrev))

print(df.corr(method = 'pearson'))
sns.heatmap(df.corr(method = 'pearson'), annot = True)
plt.show()

models = []
models.append(('DT', DecisionTreeClassifier()))
models.append(('LR', LogisticRegression()))
#models.append(('KN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC(kernel = 'linear', random_state = 0)))

xaxis, yaxis = [[], [], []], [[], [], []]
result = []
print(len(data))
for index, tz in enumerate(train_sizes):

    y = df["class"]
    x = df.drop("class", axis = 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = tz, shuffle = True, random_state = random_states[index])

    scaler = StandardScaler()
    x_train = pd.DataFrame(scaler.fit_transform(x_train), index = x_train.index , columns = x_train.columns)

    count = 0
    for name, alg in models:
        temp = []
        predicted = alg.fit(x_train, y_train).predict(x_test)
        temp.append(name)
        temp.append(round(alg.score(x_train, y_train), 4))
        temp.append(round(alg.score(x_test, y_test), 4))
        temp.append(round(precision_score(y_test, predicted, average = 'micro'), 4))
        temp.append(round(recall_score(y_test, predicted, average = 'micro'), 4))
        temp.append(round(metrics.accuracy_score(y_test, predicted), 4))
        if tz == 0.7:
            result.append(temp)

        xaxis[count].append(tz * 100)
        yaxis[count].append(round(metrics.accuracy_score(y_test, predicted), 4))
        count += 1

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(xaxis[0], yaxis[0], label = "DecisionTreeClassifier")
plt.plot(xaxis[1], yaxis[1], label = "LogisticRegression")
plt.plot(xaxis[2], yaxis[2], label = "Naive Bayes")
plt.xlabel('Train Size and Random State')
plt.ylabel('Accuracy')
count = 0
for a, b in zip(xaxis[0], yaxis[0]):
    plt.text(a, b, str(random_statesrev[count]))
    count += 1
plt.legend()
plt.show()

print("\nAlgorithm \t Traning \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

result = []
xaxis, yaxis = [[], [], []], [[], [], []]
for index, tz in enumerate(train_sizes):

    y = df["class"]
    x = df.drop("class", axis = 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = tz, shuffle = True, random_state = random_statesrev[index])

    scaler = StandardScaler()
    x_train = pd.DataFrame(scaler.fit_transform(x_train), index = x_train.index , columns = x_train.columns)

    count = 0
    for name, alg in models:
        temp = []
        predicted = alg.fit(x_train, y_train).predict(x_test)
        temp.append(name)
        temp.append(round(alg.score(x_train, y_train), 4))
        temp.append(round(alg.score(x_test, y_test), 4))
        temp.append(round(precision_score(y_test, predicted, average = 'micro'), 4))
        temp.append(round(recall_score(y_test, predicted, average = 'micro'), 4))
        temp.append(round(metrics.accuracy_score(y_test, predicted), 4))
        if tz == 0.7:
            result.append(temp)

        xaxis[count].append(tz * 100)
        yaxis[count].append(round(metrics.accuracy_score(y_test, predicted), 4))
        count += 1

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(xaxis[0], yaxis[0], label = 'DecisionTreeClassifier')
plt.plot(xaxis[1], yaxis[1], label = 'LogisticRegression')
plt.plot(xaxis[2], yaxis[2], label = 'Naive Bayes')
plt.xlabel('Train Size and Random State')
plt.ylabel('Accuracy')
count = 0
for a, b in zip(xaxis[0], yaxis[0]):
    plt.text(a, b, str(random_statesrev[count]))
    count += 1
plt.legend()
plt.show()

print("\nAlgorithm \t Traning \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

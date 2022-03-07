import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

data = pd.read_csv("/home/jerinpaul/Documents/ME/Sem 1/Data Mining/Iris.csv")

array = data.values
X = array[:,0:4]
Y = array[:,4]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.8, random_state=0)

result = []

K = 20
xaxis = list(range(1, K))
yaxis = []

res = 0
finalK = 0

for k in range(1, K):
    temp = []
    alg = KNeighborsClassifier(n_neighbors=k)
    predicted = alg.fit(x_train, y_train).predict(x_test)
    temp.append(str(k))
    temp.append(round(alg.score(x_train, y_train), 4))
    temp.append(round(alg.score(x_test, y_test), 4))
    temp.append(round(precision_score(y_test, predicted, average='micro'), 4))
    temp.append(round(recall_score(y_test, predicted, average='micro'), 4))
    temp.append(round(metrics.accuracy_score(y_test, predicted), 4))
    result.append(temp)
    if round(metrics.accuracy_score(y_test, predicted), 4) > res:
        res = round(metrics.accuracy_score(y_test, predicted), 4)
        finalK = k
    yaxis.append(round(metrics.accuracy_score(y_test, predicted), 4) * 100)
    #cm = confusion_matrix(y_test, predicted)
    #print(cm)

print("\nK Val \t Training \t Testing \t Precision \t Recall \t Accuracy")
for nm, a, b, c, d, e in result:
    print(nm + "\t\t " + str(a) + "\t\t " + str(b) + "\t\t " + str(c) + "\t\t " + str(d) + "\t\t " + str(e))

plt.title("Accuracy vs K")
plt.plot(xaxis, yaxis)
plt.show()

print("The best value of k is = ", finalK, " with accuracy = ", res * 100)
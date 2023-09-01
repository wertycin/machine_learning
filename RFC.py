# Иллюстрация работы Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from module import *
clf = RandomForestClassifier(random_state=0)
N = 20 # Размеры прямоугольного поля
M = 80
X = [[8,  10], [18, 25], [0, 9], [10, 78], [15, 20], [0, 1]]
y = [0, 1, 2, 3, 4, 5]
clf.fit(X, y)
table = [[0 for i in range(M)] for i in range(N)]
values = [[0, 0] for i in range(N * M)]
k = 0
for i in range(N):
    for j in range(M):
        values[k] = [i, j]
        k += 1
predict = clf.predict(values)
k = 0
for i in range(N):
    for j in range(M):
        table[i][j] = predict[k]
        k += 1


for i in range(M + 2):
    print('.', end='')
print()
for i in range(N):
    print('.', end='')
    for j in range(M):
        flag = -1
        for k in range(len(X)):
            if X[k] == [i, j]: flag = k
        if flag != -1: print(colours[table[i][j]].format(flag), end = "")
        else: print(colours[table[i][j]].format(" "), end = "")
    print('.')

for i in range(M + 2):
    print('.', end='')

# Иллюстрация работы Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
N = 10 # Размеры прямоугольного поля
M = 20
X = [[0,  0], [9, 9], [0, 9]]
y = [0, 1, 2]
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
        flag = 0
        for k in range(len(X)):
            if X[k] == [i, j]: flag = 1
        if flag: print('*', end = "")
        else: print(table[i][j], end ="")
    print('.')

for i in range(M + 2):
    print('.', end='')

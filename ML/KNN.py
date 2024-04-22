import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv(r"C:\Users\daf20\Documents\GitHub\final\labeled_dataset.csv")
X = dataset.drop("type", axis=1)
X = X.drop("file_name", axis=1)
y = dataset["type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

bk = 1
ba = 0
tbk = 1
tba = 0
for x in range(1, len(X_test)):
    model = KNeighborsClassifier(n_neighbors=x)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    if score > ba:
        bk = x
        ba = score
    score = model.score(X_train, y_train)
    if score > tba:
        tbk = x
        tba = score

print(tbk, tba)
print(bk, ba)

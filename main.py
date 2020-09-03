from sklearn import tree

X = [[150, 0], [170, 0], [140, 1], [130, 1]]

y = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

print(clf.predict([[160, 0]]))

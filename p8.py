import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd
import matplotlib.pyplot as plt
import warnings

df=pd.read_csv("iris_prog8.csv")
print(df)
df.replace('setosa',1, inplace=True)
df.replace('versicolor',2, inplace=True)
df.replace('virginica',3, inplace=True)


df.replace('?',-9999,inplace=True)

X=np.array(df.drop(['species'],1))
Y=np.array(df['species'])

X_train,X_test,Y_train,Y_test= cross_validation.train_test_split(X,Y,test_size=0.8)



clf=neighbors.KNeighborsClassifier()

clf.fit(X_train,Y_train)

accuracy=clf.score(X_test, Y_test)

print("Accurancy:")
print(accuracy)

print("-------------------------------------------------")
example_measures = np.array([[5.1,2.4,4.3,1.3],[4.9,3.0,1.4,0.2]])
example_measures = example_measures.reshape(2,-1)

prediction = clf.predict(example_measures)

print("Prediction")
print(prediction)

import matplotlib.pyplot as plt
from matplotlib import ft2font
import pandas as pd

#fetch data from json file
df = pd.read_json("iris.json")

#visualize through Lines, features(sepal length and species)
plt.plot(df['species'],df['sepalLength'])
plt.show()

#visualize through Line, features(petal Width and species)
plt.plot(df['species'],df['petalWidth'])
plt.show()

#visualize through Line, features(petal Length and species)
plt.plot(df['species'],df['petalLength'])
plt.show()

#visualize through Line, features(sepal Width and species)
plt.plot(df['sepalWidth'],df['species'])
plt.show()

#visualize through Bar, features(sepal length and species)
plt.bar(df['species'],df['sepalLength'])
plt.show()

#visualize through Bar, features(sepal Width and species)
plt.bar(df['species'],df['sepalWidth'])
plt.show()

#visualize through Bar, features(petal Length and species)
plt.bar(df['species'],df['petalLength'])
plt.show()

#visualize through Bar, features(petal Width and species)
plt.bar(df['species'],df['petalWidth'])
plt.show()


#visualize through Scatter, features(sepal length and species)
plt.scatter(df['species'],df['sepalLength'])
plt.show()

#visualize through Scatter, features(sepal Width and species)
plt.scatter(df['species'],df['sepalWidth'])
plt.show()

#visualize through Scatter, features(petal Length and species)
plt.scatter(df['species'],df['petalLength'])
plt.show()

#visualize through Scatter, features(petal Width and species)
plt.scatter(df['species'],df['petalWidth'])
plt.show()
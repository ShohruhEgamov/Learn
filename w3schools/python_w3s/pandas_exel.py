import pandas as pd
from sklearn import linear_model

# Misol uchun pandas ma'lumotlar to'plamini yaratamiz
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [1, 4, 9, 16, 25]
}
df = pd.DataFrame(data)

# Regression modelini yaratamiz
X = df[['X']]
y = df['Y']
model = linear_model.LinearRegression()
model.fit(X, y)

# Bashorat qilish uchun ma'lumotlar to'plamini ko'rsatamiz
y_pred = model.predict(X)
print(y_pred)


df = pd.read_csv("F:\Learn\w3schools\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

# print(predictedCO2)



#Standartlashtirish usuli quyidagi formuladan foydalanadi:

# z = (x - u) / s

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_csv("F:\Learn\w3schools\data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)


import pandas as pd

df = pd.read_csv("F:\Learn\w3schools\data1.csv")

# Bu yerda orniga son qoyish
d = {'UK': 0, 'USA': 1, 'N': 2}

# Pandalarda map()qiymatlarni qanday o'zgartirish haqida ma'lumot bilan lug'at oladigan usul mavjud.
df['Nationality'] = df['Nationality'].map(d)

# Bu yerda esa true ga 1 falsega 0 
d = {'YES': 1, 'NO': 0}

df['Go'] = df['Go'].map(d)

# Bu yerda hammasini chiqaradi
features = ['Age', 'Experience', 'Rank', 'Nationality']


X = df[features]
y = df['Go']

print(X)
print(y)



#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("F:\Learn\w3schools\data1.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names=features)

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#NOTE:
#You will see that the Decision Tree gives you different results if you run it enough times, even if you feed it with the same data.

#That is because the Decision Tree does not give us a 100% certain answer. It is based on the probability of an outcome, and the answer will vary.


# Jini
# Namunalarni ajratishning ko'plab usullari mavjud, biz ushbu qo'llanmada GINI usulidan foydalanamiz.

# Gini usuli quyidagi formuladan foydalanadi:

# Gini = 1 - (x/n)2 - (y/n)2

# xIjobiy javoblar soni ("GO") qayerda , nnamunalar soni va ysalbiy javoblar soni ("YO'Q"), bu bizga ushbu hisobni beradi:

# 1 - (7 / 13)2 - (6 / 13)2 = 0.497
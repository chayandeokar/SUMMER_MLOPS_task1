import pandas
from sklearn.linear_model import LinearRegression

db = pandas.read_csv("SalaryData.csv")

x = db["hrs"].values.reshape(30,1)
y = db["marks"]

mind = LinearRegression()

mind.fit(x,y)
mind.predict([[ 2.5 ]])
model.coef_


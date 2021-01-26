import nsepy
from datetime import date, datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def runner(s):
    try:
        df = nsepy.get_history(symbol=s, start=date(1980,1,1), end=date.today())
        df = df[['Close']]
        df.reset_index(drop=True, inplace=True)
        df.loc[len(df.index)] = [0]
        future_days = 1
        df['Prediction'] = df[['Close']].shift(-future_days)
        X = np.array(df.drop(['Prediction'], 1))[:-future_days]
        y = np.array(df['Prediction'])[:-future_days]
        x_train, x_test ,y_train, y_test = train_test_split(X, y, test_size = 0.25)
        try:
            model = LinearRegression().fit(x_train, y_train)
        except:
            model = LinearRegression().fit(x_train, y_train)
        x_future = df.drop(['Prediction'], 1)[:-future_days]
        x_future = x_future.tail(future_days)
        x_future = np.array(x_future)
        prediction1 = model.predict(x_future)
        df.drop(df.tail(1).index,inplace=True)
        for x in prediction1:
            print(f"Predicted: {x}")
    except:
        return 'Symbol not found'
for i in range(int(input("Enter the number of companies you want to predict: "))):
    symbol = input("Enter symbol: ")
    runner(symbol)   
input("Hit enter to close")
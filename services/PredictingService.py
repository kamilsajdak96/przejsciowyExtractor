import numpy as np
import quandl
import json
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from config import QUANDL_AUTH_TOKEN


def prediction():
    df = quandl.get("WIKI/AMZN", authtoken=QUANDL_AUTH_TOKEN)
    df = df[['Adj. Close']]
    print(df.head())

    forecast_out = 30 #'n=30' days

    df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

    X = np.array(df.drop(['Prediction'],1))
    X = X[:-forecast_out]

    y = np.array(df['Prediction'])
    y = y[:-forecast_out]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_rbf.fit(x_train, y_train)
    svm_confidence = svr_rbf.score(x_test, y_test)

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    lr_confidence = lr.score(x_test, y_test)

    x_forecast = np.array(df.drop(['Prediction'], 1))[-forecast_out:]

    lr_prediction = lr.predict(x_forecast)
    svm_prediction = svr_rbf.predict(x_forecast)

    return json.dumps({'svm_cofidence': svm_confidence,
                       'svm_prediciton': svm_prediction.tolist(),
                       'lr_confidence': lr_confidence,
                       'lr_prediction': lr_prediction.tolist()
                       })
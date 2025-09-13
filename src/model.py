from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(df):
    # features = EMA + RSI, target = Close price
    X = df[['EMA_20', 'RSI']].dropna()
    y = df['Close'].loc[X.index]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    return model, X_test, y_test, preds, mse

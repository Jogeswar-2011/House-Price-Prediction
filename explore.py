import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv('dataset/train.csv')

features=[ "LotArea",
    "BedroomAbvGr",
]

X=df[features]
y=df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
    )

# model=LinearRegression()
# model.fit(X_train, y_train)

# y_pred=model.predict(X_test)

# mae=mean_absolute_error(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# r2=r2_score(y_test,y_pred)
# rmse=np.sqrt(mse)

# print(f'MAE: {mae}')
# print(f'MSE: {mse}')
# print(f'R2 Score: {r2}')
# print(f'RMSE: {rmse}')

# plt.figure(figsize=(8,5))
# plt.scatter(y_test, y_pred)
# plt.xlabel('Actual House Price')
# plt.ylabel('Predicted House Price')
# plt.title('House Price Prediction')
# plt.show()

rf_model=RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)
rf_pred=rf_model.predict(X_test)

mae=mean_absolute_error(y_test,rf_pred)
mse=mean_squared_error(y_test,rf_pred)
r2=r2_score(y_test,rf_pred)
rmse=np.sqrt(mse)

# print(f'MAE: {mae}')
# print(f'MSE: {mse}')
# print(f'R2 Score: {r2}')
# print(f'RMSE: {rmse}')

# print("\nMODEL COMPARISON")

# print("Linear Regression R2:", r2_score(y_test, y_pred))
# print("Random Forest R2:", r2)

# print("Linear Regression MAE:",mean_absolute_error(y_test, y_pred))

# print("Random Forest MAE:", mae)

joblib.dump(rf_model,'model/house_price_model.pkl')
print("Model saved successfully as 'house_price_model.pkl' in the 'model' directory.")

loaded_model=joblib.load('model/house_price_model.pkl')
sample=X_test.iloc[[0]]
prediction=loaded_model.predict(sample)
print("House Details:")
print(sample)
print(f"Predicted House Price: {prediction[0]}")
print("Actual price:",y_test.iloc[0])
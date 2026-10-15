import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv('transactions.csv')
print(df['is_fraud'].value_counts())

# Convert city to numbers
df = pd.get_dummies(df, columns=['city'])
X = df.drop(['customer_name', 'is_fraud'], axis=1)
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"Accuracy: {accuracy_score(y_test, model.predict(X_test)) * 100:.2f}%")

with open('fraud_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as fraud_model.pkl")
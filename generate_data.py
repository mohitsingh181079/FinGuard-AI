import pandas as pd
import random

data = []
cities = ["Mumbai", "Delhi", "Bangalore", "Indore", "Pune"]

for i in range(1000):
    amount = random.randint(100, 100000)
    age = random.randint(18, 75)
    hour = random.randint(0, 23)
    city = random.choice(cities)
    
    # Better logic for fraud
    is_fraud = 0
    if amount > 75000 and hour < 5:
        is_fraud = 1
    elif amount > 50000 and random.random() > 0.6:
        is_fraud = 1
    elif hour < 4 and amount > 30000:
        is_fraud = 1
    else:
        is_fraud = 0 if random.random() > 0.05 else 1
    
    data.append([f"Cust_{i}", amount, age, hour, city, is_fraud])

df = pd.DataFrame(data, columns=['customer_name','amount','age','hour','city','is_fraud'])
df.to_csv('transactions.csv', index=False)
print("New Data Generated!")
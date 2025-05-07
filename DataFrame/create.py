
import numpy as np
import pandas as pd


np.random.seed(42)  # Для відтворюваності
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
product_ids = range(1, 21) 
categories = ["Electronics", "Clothing", "Food", "Furniture", "Toys"]
customers = range(1, 101)  


data = pd.DataFrame({
    "date": np.random.choice(dates, size=50),
    "product_id": np.random.choice(product_ids, size=50),
    "category": np.random.choice(categories, size=50),
    "quantity": np.random.randint(1, 10, size=50),
    "price": np.random.uniform(5.0, 500.0, size=50).round(2),
    "customer_id": np.random.choice(customers, size=50)
    
})

print(data)

data.to_csv("sales_data.csv", index=False)
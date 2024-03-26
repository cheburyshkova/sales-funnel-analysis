import pandas as pd
import numpy as np

# генерация значений
np.random.seed(42)
n_users = 100 
n_products = 20 
n_records = 1000  

user_ids = np.random.randint(1, n_users + 1, n_records)

event_dates = pd.date_range(start='2024-01-01', periods=n_records, freq='h')

event_types = np.random.choice(['view', 'add_to_cart', 'purchase'], n_records, p=[0.6, 0.3, 0.1])

product_ids = np.random.randint(1, n_products + 1, n_records)

categories = ['electronics', 'books', 'home', 'clothing', 'toys']
product_categories = np.random.choice(categories, n_records)

prices = np.random.uniform(5, 500, n_records).round(2)

data = pd.DataFrame({
    'user_id': user_ids,
    'event_date': event_dates,
    'event_type': event_types,
    'product_id': product_ids,
    'product_category': product_categories,
    'price': prices
})

data.head()
print(data.head())
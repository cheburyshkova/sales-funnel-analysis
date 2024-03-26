import pandas as pd
from userbehavior import data

def analyze_sales_funnel(df):
    print("Базовый анализ данных:")
    print(df.describe())
    print(df.info())

    funnel_stages = ['view', 'add_to_cart', 'purchase']
    funnel_counts = df['event_type'].value_counts()[funnel_stages]
    
    print("\nВоронка продаж:")
    print(funnel_counts)
    
    conversion_rates = funnel_counts.shift(-1) / funnel_counts
    print("\nКонверсия на каждом этапе:")
    print(conversion_rates)

if __name__ == "__main__":
    analyze_sales_funnel(data)
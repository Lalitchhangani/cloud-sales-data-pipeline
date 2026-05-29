import pandas as pd

df = pd.read_csv("data/sales.csv")

print("Raw Data")
print(df)

customer_sales = df.groupby("customer")["amount"].sum().reset_index()

print("\nTotal Sales By Customer")
print(customer_sales)

customer_sales.to_csv(
    "data/customer_sales.csv",
    index=False
)

print("\nFile Saved Successfully")
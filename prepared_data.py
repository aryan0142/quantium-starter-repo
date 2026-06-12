import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Convert price from "$3.00" to 3.00
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Create sales column
    df["sales"] = df["price"] * df["quantity"]

    # Keep required columns
    df = df[["sales", "date", "region"]]

    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("formatted_sales_data.csv", index=False)

print(final_df.head())
print("Rows:", len(final_df))
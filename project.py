import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Load the dataset
df = pd.read_csv("new_data.csv", encoding="ISO-8859-1")

# Drop rows with missing values
df.dropna(inplace=True)

# Convert data to transaction format
transactions = df.groupby("InvoiceNo")["Description"].apply(list).values.tolist()

# Apply one-hot encoding
te = TransactionEncoder()
oht = te.fit_transform(transactions)
oht_df = pd.DataFrame(oht, columns=te.columns_)

# Find frequent itemsets
frequent_itemsets = fpgrowth(oht_df, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Print results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

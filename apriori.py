import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv("cleaned_file.csv", encoding="ISO-8859-1")

data.dropna(subset=["CustomerID"], inplace=True)

data["CustomerID"] = data["CustomerID"].astype(int)

basket = (data.groupby(["InvoiceNo", "Description"])["Quantity"]
          .sum().unstack().reset_index().fillna(0)
          .set_index("InvoiceNo"))

def encode_units(x):
    return 1 if x > 0 else 0

basket_sets = basket.applymap(encode_units)


frequent_itemsets = apriori(basket_sets, min_support=0.02, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

print(rules)

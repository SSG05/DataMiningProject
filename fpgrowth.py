import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules


data = pd.read_csv('cleaned_file.csv', encoding='ISO-8859-1')

transactions = data.groupby("InvoiceNo")["Description"].apply(list).values.tolist()

te = TransactionEncoder()
oht = te.fit_transform(transactions)
oht_df = pd.DataFrame(oht, columns=te.columns_)

frequent_itemsets = fpgrowth(oht_df, min_support=0.02, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

rules.to_csv('association_rules.csv', index=False)

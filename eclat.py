import pandas as pd
from itertools import combinations, chain

data = pd.read_csv('cleaned_file.csv', encoding='ISO-8859-1')

data.dropna(inplace=True)

transactions = data.groupby('InvoiceNo')['Description'].apply(list).values.tolist()

def eclat(transactions, min_support, max_length):
    items = {}
    for transaction in transactions:
        for item in transaction:
            if item not in items:
                items[item] = set()
            items[item].add(transaction[0])
    
    def _support(itemset):
        return len(items[itemset[0]]) / len(transactions)
    
    def _expand(prefix, items, min_support, max_length, frequent_itemsets):
        if max_length is None or len(prefix) < max_length:
            for item, transactions in items.items():
                if len(transactions) >= min_support:
                    new_itemset = prefix + [item]
                    frequent_itemsets.append(new_itemset)
                    new_items = {key: value for key, value in items.items() if key > item}
                    _expand(new_itemset, new_items, min_support, max_length, frequent_itemsets)
    
    frequent_itemsets = []
    _expand([], items, min_support, max_length, frequent_itemsets)
    return frequent_itemsets

def generate_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = list(antecedent)
                    consequent = list(set(itemset) - set(antecedent))
                    if len(transactions) == 0:
                        confidence = 0 
                    else:
                        confidence = support_antecedent / sum(1 for transaction in transactions if set(itemset).issubset(set(transaction)) / len(transactions))
                        confidence = support_antecedent / sum(1 for transaction in transactions if set(itemset).issubset(set(transaction)) / len(transactions))
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence))
    return rules

min_support = 0.02
min_confidence = 0.5

frequent_itemsets = eclat(transactions, min_support, max_length=2)

rules = generate_rules(frequent_itemsets, min_confidence)

for antecedent, consequent, confidence in rules:
    print(f"{antecedent} => {consequent}, Confidence: {confidence}")

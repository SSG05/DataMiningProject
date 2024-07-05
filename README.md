# DMproject

This repository contains implementations of three popular algorithms for frequent itemset mining and association rule learning: Apriori, ECLAT, and FP-Growth.

## Introduction

Frequent itemset mining and association rule learning are fundamental tasks in data mining. They are used to discover interesting relations between variables in large databases. This project provides Python implementations of three key algorithms in this domain:

1. Apriori
2. ECLAT
3. FP-Growth

## Algorithms

### Apriori

The Apriori algorithm identifies frequent itemsets in a transactional database and builds strong association rules from these itemsets. It uses a bottom-up approach where frequent subsets are extended one item at a time (a step known as candidate generation), and groups of candidates are tested against the data.

### ECLAT

ECLAT (Equivalence Class Transformation) is an algorithm that improves upon Apriori by using a depth-first search strategy to traverse the itemset lattice. It uses a vertical data format where each item is associated with a list of transaction IDs in which it appears, which often leads to better performance.

### FP-Growth

FP-Growth (Frequent Pattern Growth) is an algorithm that uses a divide-and-conquer approach to mine frequent itemsets without candidate generation. It compresses the database representing frequent items into a frequent pattern tree (FP-tree) and extracts frequent itemsets directly from the FP-tree.

## Installation

To run these scripts, you need to have Python installed on your machine. Clone this repository and navigate to the project directory.

```bash
git clone https://github.com/SSG05/DataMiningProject.git


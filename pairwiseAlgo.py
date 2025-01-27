""""
This is the simple data input to illustrate the example -
This can be further expanded to include a CSV input of transactions

transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Bread', 'Eggs'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter', 'Eggs'],
    ['Milk', 'Bread', 'Butter', 'Eggs'],
    ['Bread', 'Butter'],
    ['Milk', 'Eggs'],
    ['Bread', 'Eggs'],
    ['Milk', 'Bread'],
    ['Butter', 'Eggs'],
    ['Butter', 'Ham'],
    ['Bread', 'Eggs'],
    ['Ham', 'Cheese']
]
 
The program will return the following output:

{('Butter', 'Bread'): 0.5714285714285714,
 ('Bread', 'Butter'): 0.5,
 ('Bread', 'Milk'): 0.5,
 ('Eggs', 'Bread'): 0.7142857142857143,
 ('Bread', 'Eggs'): 0.625}

We can interpret this as Shoppers who purchase Butter have a ~57% chance of purchasing Bread.

Additionally if a Shopper purchases Bread they are 50% likely to purchase Butter or Milk and 71% likely to purchase Eggs.

If I ran a retail store grouping these commonly purcahsed items together or including financial incentives can further drive incremental sales.
"""

transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Bread', 'Eggs'],
    ['Milk', 'Butter'],
    ['Bread', 'Butter', 'Eggs'],
    ['Milk', 'Bread', 'Butter', 'Eggs'],
    ['Bread', 'Butter'],
    ['Milk', 'Eggs'],
    ['Bread', 'Eggs'],
    ['Milk', 'Bread'],
    ['Butter', 'Eggs'],
    ['Butter', 'Ham'],
    ['Bread', 'Eggs'],
    ['Ham', 'Cheese']
]

from collections import defaultdict
from itertools import combinations
import copy

def create_rules_from_source(source, conf_threshold, min_count):
    
    def create_item_sets(data):
        """
        Input: source data: lorem ipsum text, recipes
        Output: itemized data set ready to rock and be counted
        """
        itemSet = []
        for elem in data:
            itemSet.append(set(elem))

        #display(itemSet)
        return itemSet
    
    itemized = create_item_sets(source)

    def create_pair_counts(itemset):
        """
        Updates a dictionary of pair counts for
        all pairs of items in a given itemset.
        """

        pair_counts = defaultdict(int)
        
        for item in itemset: 
            for a, b in combinations(item, 2):
                pair_counts[(a,b)] += 1
                pair_counts[(b,a)] += 1

        #display(pair_counts)
        
        return pair_counts
    
    pair_counts_dict = create_pair_counts(itemized) # returns itemized/counted pair counts
    
    
    def count_items(itemset):
        """
        Count the occurrence of individual items in our basket
        Input: itemized data set 
        Output: dictionary of individual item counts
        """
        
        item_counts = defaultdict(int)

        for item in itemset:
            for i in item:
                item_counts[i] += 1

        #display(item_counts)

        return item_counts
    
    
    count_of_items = count_items(itemized)
        

    def create_rules_from_counts(pair_counts, item_counts):
        rules_dict = {} # (item_a, item_b) -> conf (item_a => item_b)

        """
        Parameters
            ----------
            pair_counts : dict
                A dictionary where keys are (item_a, item_b) tuples and 
                values are counts for how often (item_a, item_b) co-occur.
            item_counts : dict
                A dictionary where keys are items (e.g. strings) and
                values are counts for how often each item appears.

            Returns
            -------
            rules : dict
                A dictionary mapping (item_a, item_b) -> confidence 
                (interpreting item_a => item_b).

        """

        for item in pair_counts:
            rules_dict[item] = pair_counts[item] / item_counts[item[0]]

            
        #display(rules_dict)
        
        return rules_dict
    
    
    rules = create_rules_from_counts(pair_counts_dict, count_of_items)




    def filter_rules(pairCounts, Rules, itemCounts, min_count, conf_threshold):
        resultDict = {}

        for (a, b), cooc_count in pairCounts.items():
            conf = Rules.get((a, b), None)  # Use .get() to avoid KeyError
            print(f"Processing pair: ({a}, {b}), cooc_count: {cooc_count}, conf: {conf}")
            display(min_count)
            if conf is not None and itemCounts.get(a, 0) >= min_count and conf >= conf_threshold:
                resultDict[(a, b)] = conf
                print(f"Added rule: ({a}, {b}) with confidence: {conf}")

                
        return resultDict
            

    
    
    dictOutput = filter_rules(pair_counts_dict, rules, count_of_items, min_count, conf_threshold)
    
    
    return dictOutput

    
groceryRules = create_rules_from_source(transactions, 0.5, 7)
# hangi elemandan kaç tane var

from collections import Counter
lst = ["a", "c", "b", "a", "c", "c"]
print(Counter(lst))
#Counter({'c': 3, 'a': 2, 'b': 1})
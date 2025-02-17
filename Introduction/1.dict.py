Summary
Method	Use Case
for k, v in dict.items()	Best for key-value traversal
for k in dict.keys()	When you only need keys
for v in dict.values()	When you only need values




  from collections import defaultdict

d = defaultdict(int)
d = defaultdict(list)

d = defaultdict(lambda:-1)
d = defaultdict(lambda:0)
d = defaultdict(lambda:[])


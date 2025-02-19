
---

# **1️⃣ Sorting & Reversing Methods**

## **`.sort()` vs `sorted()`**
| Method | Mutates Original List? | Returns a New List? | Works on Other Iterables? |
|--------|---------------------|------------------|----------------|
| `list.sort()` | ✅ Yes | ❌ No (modifies in-place) | ❌ No (only works on lists) |
| `sorted(iterable)` | ❌ No | ✅ Yes | ✅ Yes (works on strings, tuples, dicts, etc.) |

### **Example:**
```python
nums = [3, 1, 4, 1, 5]

nums.sort()  # ✅ In-place sorting
print(nums)  # Output: [1, 1, 3, 4, 5]

nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)  # ✅ Returns a new sorted list
print(sorted_nums)  # Output: [1, 1, 3, 4, 5]
print(nums)  # Output: [3, 1, 4, 1, 5] (original unchanged)
```

---

## **`.reverse()` vs `reversed()`**
| Method | Mutates Original List? | Returns a New List? | Works on Other Iterables? |
|--------|---------------------|------------------|----------------|
| `list.reverse()` | ✅ Yes | ❌ No (modifies in-place) | ❌ No (only works on lists) |
| `reversed(iterable)` | ❌ No | ✅ Returns an iterator | ✅ Yes (works on strings, tuples, dicts, etc.) |

### **Example:**
```python
nums = [1, 2, 3, 4, 5]

nums.reverse()  # ✅ In-place reversal
print(nums)  # Output: [5, 4, 3, 2, 1]

nums = [1, 2, 3, 4, 5]
rev_nums = list(reversed(nums))  # ✅ Returns a new reversed list
print(rev_nums)  # Output: [5, 4, 3, 2, 1]
print(nums)  # Output: [1, 2, 3, 4, 5] (original unchanged)
```

---

# **2️⃣ `join()` vs `split()`**
| Method | Purpose | Works on |
|--------|---------|----------|
| `"separator".join(iterable)` | Joins elements with a separator | Lists, tuples, sets of strings |
| `string.split("separator")` | Splits string into a list | Strings |

### **Example:**
```python
words = ["hello", "world"]
sentence = " ".join(words)  # ✅ Joins list elements into a single string
print(sentence)  # Output: "hello world"

sentence = "apple,banana,grape"
fruits = sentence.split(",")  # ✅ Splits string into a list
print(fruits)  # Output: ['apple', 'banana', 'grape']
```

---

# **3️⃣ `defaultdict` (Advanced Dictionary Handling)**  
**Regular `dict`:**
```python
d = {}
print(d["key"])  # ❌ KeyError if key is missing
```

**Using `defaultdict`:**
```python
from collections import defaultdict

d = defaultdict(int)  # ✅ Default value for missing keys is 0
print(d["key"])  # Output: 0

d_list = defaultdict(list)  # ✅ Default value is an empty list
d_list["key"].append(10)
print(d_list["key"])  # Output: [10]

d_lambda = defaultdict(lambda: "default_value")  # ✅ Custom default
print(d_lambda["missing"])  # Output: "default_value"
```

---

# **4️⃣ `lambda` Functions for Sorting**
**Lambda functions are useful for custom sorting.**
```python
arr = [(1, 2), (3, 1), (5, 0)]
arr.sort(key=lambda x: x[1])  # ✅ Sort by second element of tuple
print(arr)  # Output: [(5, 0), (3, 1), (1, 2)]
```

**Sorting in reverse order:**
```python
nums = [3, 1, 4, 1, 5]
nums.sort(key=lambda x: -x)  # ✅ Sorts in descending order
print(nums)  # Output: [5, 4, 3, 1, 1]
```

---

# **5️⃣ `enumerate()` and Other Similar Methods**
| Method | Purpose |
|--------|---------|
| `enumerate(iterable, start=0)` | Returns index-value pairs |
| `zip(iterable1, iterable2)` | Pairs elements from both iterables |
| `map(function, iterable)` | Applies function to each element |
| `filter(function, iterable)` | Filters elements based on function |

### **Example 1: `enumerate()`**
```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(index, name)

# Output:
# 1 Alice
# 2 Bob
# 3 Charlie
```

### **Example 2: `zip()`**
```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
for pair in zip(a, b):
    print(pair)

# Output:
# (1, 'a')
# (2, 'b')
# (3, 'c')
```

---

# **6️⃣ Other Useful Python Tricks for DSA**
### **Using `Counter` for Frequency Counting**
```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
freq = Counter(nums)
print(freq)  # Output: Counter({3: 3, 2: 2, 1: 1})
```

---

### **Heap (Priority Queue)**
```python
import heapq

min_heap = [3, 1, 4, 1, 5]
heapq.heapify(min_heap)  # ✅ Convert list into a heap
print(heapq.heappop(min_heap))  # Output: 1 (smallest element)
```

For **max heap**, use:
```python
max_heap = [-x for x in min_heap]  # Invert values for max heap
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))  # Output: Largest element
```

---

### **Deque (Fast Insertion/Deletion from Both Ends)**
```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # ✅ Insert at front
dq.append(4)      # ✅ Insert at back
print(dq)  # Output: deque([0, 1, 2, 3, 4])

dq.pop()      # ✅ Remove from back
dq.popleft()  # ✅ Remove from front
print(dq)  # Output: deque([1, 2, 3])
```

---

# **Final Thoughts & Best Practices**
1. **Use `sorted()` over `.sort()` if you need to preserve the original list.**
2. **Use `reversed()` over `.reverse()` if you need a new reversed list.**
3. **Use `defaultdict(int)` for frequency counting instead of checking keys manually.**
4. **Use `lambda` functions with `sorted()` or `.sort()` for custom sorting.**
5. **Use `enumerate()` for index-value iteration.**
6. **Use `Counter`, `heapq`, and `deque` for optimized DSA solutions.**

🚀 **Mastering these tricks will make your Python DSA journey much smoother!** 🚀

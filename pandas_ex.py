import numpy as np
import pandas as pd
## Pandas 자료구조 중 Series
obj = pd.Series([4,7,-5,3])
print(obj.index)
print("=" * 55)
obj2 = pd.Series([4,7,-5,3], index=['a','b','c','d'])
print(obj2)

print("=" * 55)
sdata = {'Kim': 35000, 'Beomwoo' : 67000, 'Joan' : 12000, 'Choi': 4000}
obj3 = pd.Series(sdata)
print(obj3)
print("=" * 55)
obj3.name = 'Salary'
obj3.index.name = "Names"
print(obj3)
print("=" * 55)

## Pandas 자료구조 중 Data Frame

data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df)


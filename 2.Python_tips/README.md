# Python Tips

1.对一个列表进行的不同类别计数
```python
import collections
test=['a','a','b','c','c','c']
collections.Counter(test)
# Result: Counter({'c': 3, 'a': 2, 'b': 1})
```

2.Python模式匹配内置库[fnmatch & glob](https://www.cnblogs.com/dachenzi/p/8215584.html) <br>
glob == os.listdir + fnmatch
```python
import glob
glob.glob('*.txt')
# Result: ['a1.txt', 'a2.txt', 'aA.txt']
```
3.对列表元素去重
```python
test=[1,1,2,2,3,3,3,4]
list(set(test))  # Method 1
list({}.fromkeys(test).keys())  # Method 2
# Result:[1, 2, 3, 4]
```


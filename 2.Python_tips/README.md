# Python Tips

1.对一个列表进行的不同类别计数
```python
import collections
test=['a','a','b','c','c','c']
collections.Counter(test)
```
结果：Counter({'c': 3, 'a': 2, 'b': 1})

2.Python模式匹配内置库fnmatch & glob
glob == os.listdir + fnmatch


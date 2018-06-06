# Python Tips

1.对一个列表进行的不同类别计数
```python
import collections
test=['a','a','b','c','c','c']
collections.Counter(test)
```
结果：Counter({'c': 3, 'a': 2, 'b': 1})

2.Python模式匹配内置库fnmatch & glob <br>
glob == os.listdir + fnmatch
```
import glob
glob.glob('*.txt')
```
Result: ['a1.txt', 'a2.txt', 'aA.txt']

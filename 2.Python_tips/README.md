# Python Tips

1.对一个列表进行的不同类别计数
```python
import collections
test = ['a','a','b','c','c','c']
collections.Counter(test)
# Result: Counter({'c': 3, 'a': 2, 'b': 1})
```

2.模式匹配内置库[fnmatch & glob](https://www.cnblogs.com/dachenzi/p/8215584.html) <br>
*glob == os.listdir + fnmatch*
```python
import glob
glob.glob('*.txt')
# Result: ['a1.txt', 'a2.txt', 'aA.txt']
```
3.对列表元素去重
```python
test = [1,1,2,2,3,3,3,4]
list(set(test))  # Method 1
list({}.fromkeys(test).keys())  # Method 2
# Result:[1, 2, 3, 4]
```

4.无限接近0的数
```python
eps = np.finfo(np.float).eps
print(eps)
# Result: 2.220446049250313e-16
```

5.在Jupyter中在线听Audio
```python
from IPython.display import Audio
Audio(data, rate=framerate)
or Audio('/path/to/sound.wav')
```

6. 将列表中的所有元素组合成字符串
```python
a = ["Python", "is", "awesome"]
print("".join(a))
```

7. 检查两个字符串是不是由相同字母不同顺序组成
```python
from collections import Counter
Counter(str1) == Counter(str2)
```

8. 反转字符串
```python
num = 1234
reverse_num = int(str(num)[::-1])

a = [4, 3, 2, 5]
print(a[::-1])
```

9.
```python

# Result: 
```

10.
```python

# Result: 
```

11.
```python

# Result: 
```

12.
```python

# Result: 
```

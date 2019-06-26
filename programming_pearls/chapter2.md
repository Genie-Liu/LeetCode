# Chaper2

1. 遍历词典，以签名作为字典的key，同样签名的单词形成一个列表value。维护好这个字典后，任意一个单词，都可以通过签名从字典中获取到所有变位词。

```python
sig_dict = {}
with open("source.txt", "r") as fin:
  for word in fin:
    sig = "".join(sorted(word))
    if sig not in sig_dict:
      sig_dict[sig] = []
    sig_dict[sig].append(word)
    
def get_similar(word, sig_dict):
  sig = "".join(sorted(word))
  return sig_dict.get(sig, [])
```



2. 这里很多人都被前面的查找不存在的整数影响而造成思维定势，其实只要在遍历的时候，对比前后整数就可以在遍历一遍的过程中找到出现两次的整数。

```python
prev = None
with open("source.txt", "r") as fin:
  for number in fin:
    if number == prev:
      print("duplicate number: {}".format(number))
      break
    else:
      prev = number
```

3. i和n的最大公约数m表示要从a[0]…a[m-1]这m个数开始做移动才行。

   证明如下：

   ```
   令 i = am, n = bm
   由于m为最大公倍数，所以a, b互质，假设起点为x, 则(x+i)%n = (x+am)%bm, a和b互质，所以需要遍历b个数之后才回到原来的x。
   总数为bm，所以要遍历m个不同的x才能遍历所有元素。
   ```

   

   


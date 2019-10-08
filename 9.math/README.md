## 数学だって

for Python 3.7.+

### 基本演算

基本の四則演算

```python
>>> 1 + 3
4
>>> 4 / 2
2
>>> 4 - 2
2
>>> 2 * 3
6
```

剰余残と、整除除算

```python
>>> 5 % 2
1
>>> 5 // 2
2
```

べき乗

```python
>>> 4 ** 2
16
```

### Python の数学計算ライブラリ

探してみると種類が結構あるのですが、ここでは `nummpy` と `scipy` のを紹介します。  
`numpy` は数値計算やベクトル計算を行うための拡張パッケージ。  
`scipy` は学術計算ライブラリです。

scipy には numpy を使いますので、numpy を先に入れてしまいます。

```bash
$ pip install numpy
$ pip install scipy
```

### numpy を試す

こちらは非常に簡単に。


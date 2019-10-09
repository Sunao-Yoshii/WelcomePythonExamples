# 数学を手軽に

for Python 3.7.+

## 基本演算

Python は標準でもそこそこ計算する機能が揃ってます。  
計算の機能だけでもこれだけあります。

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

他の言語だと馴染みがないかもシリーズでは、 **分数** とか。

```python
>>> from fractions import Fraction
>>> f = Fraction(3, 4)
>>> f
Fraction(3, 4)
>>> f2 = Fraction('2/5')
>>> f + f2
Fraction(23, 20)
```

**複素数** とか普通に使えるのはあんまりみないかなと。

```python
>>> a = 2 + 3j
>>> b = 4 + 2j
>>> 
>>> a.real
2.0
>>> a.imag
3.0
>>> 
>>> a * b
(2+16j)
```

## Python の数学計算ライブラリ

探してみると種類が結構あるのですが、ここでは `nummpy` と `scipy` のを紹介します。  
`numpy` は数値計算やベクトル計算を行うための拡張パッケージ。  
`scipy` は学術計算ライブラリです。

scipy には numpy を使いますので、numpy を先に入れてしまいます。

```bash
$ pip install numpy
$ pip install scipy
```


# Numpy を利用してみる

これはまず import から始まります。  
`as` は別名インポートですね。


```python
import numpy as np

# 小数点第3位まで表示する様指定
%precision 3
```




    '%.3f'



## 基本操作

配列の操作から行きます


```python
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])
data
```

    array([ 9,  2,  3,  4, 10,  6,  7,  8,  1,  5])


データ型の判定をしたり

```python
data.dtype
```

    dtype('int64')

行列と見立てた場合の次元数と要素数の表示。

```python
print(data.ndim)
print(data.size)
```

    1
    10


行列の掛け算その他

```python
print('掛け算: ', np.array([2, 4, 6, 8]) * np.array([1, 3, 5, 7]))
print('累乗　: ', np.array([2, 4, 6, 8]) ** 2)
print('割り算　: ', np.array([2, 4, 6, 8]) * np.array([2, 2, 2, 2]))
```

    掛け算:  [ 2 12 30 56]
    累乗　:  [ 4 16 36 64]
    割り算　:  [ 4  8 12 16]

ソートに

```python
data.sort()
data
```

    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

色々情報

```python
print(data.min())
print(data.max())
print(data.sum())
print(data.cumsum())
print(data.mean())
```

    1
    10
    55
    [ 1  3  6 10 15 21 28 36 45 55]
    5.5


## 行列としての操作

numpy は行列計算のためのライブラリですので、ここから本領発揮です。

```python
import numpy.random as random

values = np.arange(9, 18).reshape(3, 3)
values
```

    array([[ 9, 10, 11],
           [12, 13, 14],
           [15, 16, 17]])

`reshape` を使えば行列の形を整形できます。

```python
values2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).reshape(3, 3)
values2
```

    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])

dot 積はメソッドから。

```python
np.dot(values, values2)
```

    array([[ 96, 126, 156],
           [123, 162, 201],
           [150, 198, 246]])

スカラ倍はそのまま掛け算します。

```python
values * values2
```

    array([[  0,  10,  22],
           [ 36,  52,  70],
           [ 90, 112, 136]])

# Scipy

`Scipy` は Python の数学演算用ライブラリです。  
内部的に numpy を利用しているため、 Numpy の機能も一通りそのまま使えます。

## 行列の計算

`Scipy` から行列でよく使う機能を読んでみましょう。  
まずは行列式

```python
import scipy.linalg as linalg  # 線形代数ライブラリひゃっほい

matrix = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
linalg.det(matrix)  # 行列式の計算に
```

    -4.000

逆行列はまだ覚えてる人も多いのでは？

```python
linalg.inv(matrix)  # 逆行列
```

    array([[ 0. , -0.5, -0.5],
           [-0.5, -0. , -0.5],
           [-0.5, -0.5,  0. ]])



逆行列で dot 積をとると単位行列になるので、確認が取れます。

```python
np.dot(matrix, linalg.inv(matrix))
```

    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])

さらに固有値と固有ベクトル


```python
eigval, eigvec = linalg.eig(matrix)
print(eigval)  # 固有値
print(eigvec)  # 固有ベクトル
```

    [-1.+0.j  2.+0.j  2.+0.j]
    [[ 0.577 -0.816  0.428]
     [ 0.577  0.408 -0.816]
     [ 0.577  0.408  0.389]]


## 簡単な機能

基本的な関数をネタに色々遊んでみます。


```python
def example_func(x):
    return x**2 + 2*x + 1
```

まずはニュートン法で解の近似値を探してみます。


```python
from scipy.optimize import newton

newton(example_func, 0)
```

    -1.000

最小値検索を行ってみます

```python
from scipy.optimize import minimize_scalar

minimize_scalar(example_func, method='Brent')
```

         fun: 0.0
        nfev: 9
         nit: 4
     success: True
           x: -1.0000000000000002

こんな感じで様々な機能が存在します。
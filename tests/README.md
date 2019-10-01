# テストライブラリ

for Python 3.7.x

## 標準テスト

Python には Unittest ライブラリが標準付属しています。

```python
import unittest

def target_add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8, target_add(2, 6))
    def test_add_zero(self):
        self.assertEqual(2, target_add(2, 0))

if __name__ == "__main__":
    unittest.main()
```

実行することこんな感じになります

```bash
$ python -m unittest test_example
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

なお、実行時に discover を指定すると、同一ディレクトリ内の python スクリプトテストをまとめて実行できます。

```bash
$ python -m unittest discover
```

## Assert 一覧

<table>
<thead>
<tr><th>ASSERメソッド</th><th>チェック対象</th></tr>
</thead>
<tbody>
<tr><td>assertEqual(a, b)</td><td>a == b</td></tr>
<tr><td>assertNotEqual(a, b)</td><td>a != b</td></tr>
<tr><td>assertTrue(x)</td><td>bool(x) is True</td></tr>
<tr><td>assertFalse(x)</td><td>bool(x) is False</td></tr>
<tr><td>assertIs(a, b)</td><td>a is b</td></tr>
<tr><td>assertIsNot(a, b)</td><td>a is not b</td></tr>
<tr><td>assertIsNone(x)</td><td>x is None</td></tr>
<tr><td>assertIsNotNone(x)</td><td>x is not None</td></tr>
<tr><td>assertIn(a, b)</td><td>a in b</td></tr>
<tr><td>assertNotIn(a, b)</td><td>a not in b</td></tr>
<tr><td>assertIsInstance(a, b)</td><td>isinstance(a, b)</td></tr>
<tr><td>assertNotIsInstance(a, b)</td><td>not isinstance(a, b)</td></tr>
<tr><td>assertAlmostEqual(a, b)</td><td>round(a-b, 7) == 0</td></tr>
<tr><td>assertNotAlmostEqual(a, b)</td><td>round(a-b, 7) != 0</td></tr>
<tr><td>assertGreater(a, b)</td><td>-a > b</td></tr>
<tr><td>assertGreaterEqual(a, b)</td><td>a >= b</td></tr>
<tr><td>assertLess(a, b)</td><td>a < b</td></tr>
<tr><td>assertLessEqual(a, b)</td><td>a <= b</td></tr>
<tr><td>assertRegexpMatches(s, r)</td><td>r.search(s)</td></tr>
<tr><td>assertNotRegexpMatches(s, r)</td><td>not r.search(s)</td></tr>
<tr><td>assertDictContainsSubset(a, b)</td><td>all the key/value pairs in a exist in b</td></tr>
</tbody>
</table>

### Doctest

個人的に大好きな機能。  
この機能はメソッドコメント上にコンソール上での実行記述を行うと、それをテスト操作 + 結果とみなしてテスト実行します。

```python
class Example:
    def add_and_twice_value(self, num1, num2):
        '''引数同士を足して、2倍する
        >>> k = Example()
        >>> k.add_and_twice_value(10, 10)
        20

        '''
        return (num1 + num2) * 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

わざと落ちるテストですが、実行してみると

```bash
$ python doctest_example.py 
**********************************************************************
File "doctest_example.py", line 5, in __main__.Example.add_and_twice_value
Failed example:
    k.add_and_twice_value(10, 10)
Expected:
    30
Got:
    40
**********************************************************************
1 items had failures:
   1 of   2 in __main__.Example.add_and_twice_value
***Test Failed*** 1 failures.
```


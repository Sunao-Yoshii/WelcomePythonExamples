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

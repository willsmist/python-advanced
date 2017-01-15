#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person(object):

    address = 'Earth'

    def __init__(self, name):

        self.name = name

p1 = Person('Apple')

p2 = Person('Bob')

print Person.address
print p1.address
print p2.address
print '---------------------'
p1.address = '11111'
print Person.address
print p1.address
print p2.address
print '---------------------'
Person.address = 'O0000'
print Person.address
print p1.address
print p2.address
print '---------------------'

# 可见，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。
# 而 Java 正与此相反，不管是通过 类名.类属性 还是通过 实例.类属性修改类属性，所有的 实例.类属性都会做一致的改变


class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score > s.score:
            return 1
        elif self.score < s.score:
            return -1
        else:
            return cmp(self.name, s.name)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)

def fib(n):
    L = []
    def f(k):

        if k == 0:
            L.append(0)
            return 0, 0
        if k == 1:
            f(0)
            L.append(1)
            return 0, 1
        preResult = f(k-1)
        result = (preResult[1], sum(preResult))
        L.append(result[1])
        return result
    f(n-1)
    return L
print fib(10)


class Fib(object):

    def __init__(self, num):
        a, b, L = 0, 1, []
        for i in range(num):
            L.append(a)
            a, b = b, a + b
        self.nums = L

    def __str__(self):
        return str(self.nums)

    __repr__ = __str__

    def __len__(self):
        return len(self.nums)

f = Fib(10)
print f
print len(f)

print '----------------------------------'

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

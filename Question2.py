import abc
import collections
from abc import ABC

print('#####################################Q1')


def composeStr(l1, l2):
    return "".join(list(map(lambda index: "".join({x[1]: x[0] for x in zip(l1, l2)}[index]), range(1, len(l1) + 1))))


l1 = ['a', 'h', 'f', 'e', 'y', 'u']
l2 = [1, 5, 3, 6, 2, 4]
print(composeStr(l1, l2))

print('#####################################Q2')


def composeLst(L):
    return list(map(lambda index: int("".join(str(dict(L)[index]) if index in dict(L).keys() else str(-1000))),
                    range(0, max(L)[0] + 1)))


L = [(4, 9), (0, 2), (1, 4), (3, 21)]
d = composeLst(L)
print(d)

print('#####################################Q3')


def newLst(L):
    return list(map(lambda index: int("".join(str(min(L)[1]))), range(0, max(L)[0] + 1)))


L = [(4, 9), (0, 2), (1, 4), (3, 21)]
print(newLst(L))
print('#####################################Q4')

Li = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]


def condition1(value, index):
    if value % 2 == 0 and index % 2 == 0:
        return True
    return False


def condition2(value, index):
    if value % 2 == 1 and index % 2 == 0 or value % 2 == 0 and index % 2 == 1:
        return True
    return False


def condition3(value, index):
    if value % 2 == 1 and index % 2 == 1:
        return True
    return False


L = [1, 0, 2, 3, 4, 5, 6, 0, 8, -555, 12345]


def crtList(L):
    return [(L[x] // 2 if condition1(L[x], x) else 0) or (L[x] if condition2(L[x], x) else 0) or (
        [L[x]] * 2 if condition3(L[x], x) else 0) for x in range(len(L))]


newList = list(filter(lambda x: not (isinstance(x, list)), crtList(L)))
print(newList)


print('#####################################Q5')
def testSharon(n):
    l = []
    for i in range(n):
        j = 0
        while j < i:
            if j % 2 == 0:
                l.append(j + 5)
            elif j % 3 == 0:
                l.append(j // 2)
            elif j % 5 == 2:
                l.append(j)
            j += 1
    return l

n = 12
l = list(filter(lambda i: i is not None ,sum(list(
    map(lambda i: list(map(lambda k: k + 5 if (k % 2 == 0) else k // 2 if (k % 3 == 0) else k if (k % 5 == 2) else None,
                           filter(lambda y: y % 2 == 0 or y % 3 == 0 or y % 5 == 2, range(i)))), range(0, n))), [])))
print("Original Function: ")
print(testSharon(n))
print("One Line Function: ")
print(l)

print('#####################################Q6')


def get_num(l):
    for i in range(0, len(l)):
        if div_helper(l[i]):
            yield l[i]
    return


def div_helper(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div = sum_div + i
    return sum_div >= num


##Q6 Class
class gen:
    def __init__(self, l):
        self.list = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if div_helper(self.list[self.index]):
            self.index += 1
            return self.list[self.index - 1]
        else:
            # Iterators must raise when done, else considered broken
            self.index += 1
            raise StopIteration


##Q6
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30, 40]
# Q6 a
newla = []
for g in get_num(l):
    newla.append(g)
print("Gen Function :")
print(newla)
# Q6 b
iter_expr = (l[i] for i in range(0, len(l)) if div_helper(l[i]))
newlb = []

for g in iter_expr:
    newlb.append(g)
print("Gen with list comprehension Function :")
print(newlb)

# Q6 c
iter_class = gen(l)
newlc = []
for i in range(0, len(l)):
    try:
        x = iter_class.__next__()
        newlc.append(x)
    except StopIteration as e:
        pass
print("Gen Class:")
print(newlc)
print('#####################################Q7')


def replace_at_index(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix + 1:]


def calc_jump(start, jump):
    if start[2] + jump[2] >= 60:
        start = replace_at_index(start, 2, (start[2] + jump[2]) % 60)
        start = replace_at_index(start, 1, start[1] + 1)

    else:
        start = replace_at_index(start, 2, start[2] + jump[2])
    if start[1] + jump[1] >= 60:
        start = replace_at_index(start, 1, (start[1] + jump[1]) % 60)
        start = replace_at_index(start, 0, start[0] + 1)

    else:
        start = replace_at_index(start, 1, start[1] + jump[1])
    if start[0] + jump[0] >= 24:
        start = replace_at_index(start, 0, (start[0] + jump[0]) % 24)

    else:
        start = replace_at_index(start, 0, start[0] + jump[0])
    return start


def check_end(start, end):
    if start[0] == end[0]:
        if start[1] == end[1]:
            if start[2] > end[2]:
                return True
        elif start[1] > end[1]:
            return True
    elif start[0] > end[0]:
        return True
    return False


def func_clock(start, end, jump):
    while not check_end(start, end):
        start = calc_jump(start, jump)
        yield start
    return


def func_clock_send(start, end, jump):
    count = 0
    while not check_end(start, end):

        check = yield start
        if count == 0:
            yield start
            count = count + 1
        if check is not None:
            end = check
        start = calc_jump(start, jump)
    yield start


##Q7 Class
class gen_clock:
    def __init__(self, start, end, jump):
        self.start = start
        self.end = end
        self.jump = jump

    def __iter__(self):
        return self

    def __next__(self):
        if not check_end(self.start, self.end):
            self.start = calc_jump(self.start, self.jump)
            return self.start
        else:
            raise StopIteration


start = (10, 30, 30)
end = (10, 40, 0)
jump = (0, 1, 1)
# Q7 a
print(list(func_clock(start, end, jump)))
# Q7 b

l_gen_clock = []
clock = gen_clock(start, end, jump)
while True:
    try:
        x = clock.__next__()
        l_gen_clock.append(x)
    except StopIteration as e:
        break
print(l_gen_clock)
# Q7 c
l_gen_clock_send = func_clock_send(start, end, jump)
next(l_gen_clock_send)
l_gen_clock_send.send((10, 50, 0))
print(list(l_gen_clock_send))

# Q7 d
l_gen_class_clock_send = []
clock = gen_clock(start, end, jump)
clock.end = (10, 50, 0)
while True:
    try:
        x = clock.__next__()
        l_gen_class_clock_send.append(x)
    except StopIteration as e:
        break
print(l_gen_class_clock_send)

print('#####################################Q8')


def funcA(m, n):
    if m < n:
        return lambda: funcA(m + 1, n - 1)
    elif m == n:
        return lambda: print("m==n")
    else:
        return lambda: lambda: print(m + n)


funcA(3, 10)()()()()()()
funcA(3, 7)()()()
funcA(4, 4)()
funcA(10, 5)()()
funcA(9, 5)()()

print('#####################################Q9')


def funcB(n):
    if n == 0:
        print("the end")
    else:
        return lambda: funcB(n - 1)


funcB(5)()()()()()
funcB(3)()()()
funcB(8)()()()()()()()()


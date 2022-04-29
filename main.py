from functools import reduce


def composeStr(l1, l2):
    return list(map(lambda index: "".join({x[1]: x[0] for x in zip(l1, l2)}[index]), range(1, len(l1) + 1)))


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


Li = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
l = [Li[i] // 2 for i in range(0, len(Li)) if condition1(Li[i], i)] + [Li[i] for i in range(0, len(Li)) if
                                                                       condition2(Li[i], i)] + \
    [[Li[i], Li[i]] for i in range(0, len(Li)) if condition3(Li[i], i)]

print(list(filter(lambda x: not (isinstance(x, list)), l)) +
      filter(lambda x: isinstance(x, list), l)))

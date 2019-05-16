'''d1 = {'nums':
          {'num1': 12,
           'num2': 12.1234523,
           'num3': 12.123451},
      'names':
          {'name1': 'Bob',
           'name2': 'Jack'}
      }

d2 = {'nums':
          {'num1': 12,
           'num2': 12.123452,
           'num3': 12.123451},
      'names':
          {'name1': 'Bob',
           'name2': 'Jack'}
      }
'''

d1 = {'nums': {'num': 12.1234523}}
d2 = {'nums': {'num': 12.1234331}}


d3 = [1, 2, 3, 'test']
d4 = [1, 2, 3, 'test']


def compare_floats(num1, num2):
    eps = 10**-5
    if abs(num1 - num2) < eps:
        print(num1, 'and', num2, 'are equal')
        return True
    else:
        print(num1, 'and', num2, 'are NOT equal')
        return False


def compare_dicts(d1, d2):
    for k in d1.keys():
        if k not in d2.keys():
            return False
        else:
            if type(d1[k]) is dict:
                return compare_dicts(d1[k], d2[k])
            if type(d1[k]) is list:
                return compare_lists(d1[k], d2[k])
            if type(d1[k]) is float and type(d2[k]) is float:
                return compare_floats(d1[k], d2[k])
            return d1[k] == d2[k]


def compare_lists(l1, l2):
    i = 0
    if len(l1) != len(l2):
        return False
    else:
        while i < len(l1):
            if type(l1[i]) is list and type(l2[i]) is list:
                return compare_lists(l1[i], l2[i])
            if type(l1[i]) is dict and type(l2[i]) is dict:
                return compare_dicts(l1[i], l2[i])
            return l1[i] == l2[i]
        i += 1


print(compare_dicts(d1, d2))
print(compare_lists(d3, d4))

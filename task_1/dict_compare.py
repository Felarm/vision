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
d2 = {'nums': {'num': 12.1234521}}


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
    prog = {'True': 0, 'False': 0}
    for k in d1.keys():
        if k not in d2.keys():
            print('aint equal')
            return False
        else:
            if type(d1[k]) is dict:
                print('its dict, lets go recursive lets compare', d1[k], 'and', d2[k])
                if compare_dicts(d1[k], d2[k]):
                    prog['True'] += 1
                    print('these dicts are equal')
                else:
                    print('these dicts are NOT equal')
                    prog['False'] += 1
            if type(d1[k]) is list:
                print('its a list, go other func. lets compare', d1[k], 'and', d2[k])
                if compare_lists(d1[k], d2[k]):
                    prog['True'] += 1
                else:
                    prog['False'] += 1
            if type(d1[k]) is float and type(d2[k]) is float:
                if compare_floats(d1[k], d2[k]):
                    prog['True'] += 1
                else:
                    prog['False'] += 1
            if d1[k] == d2[k]:
                print('this values are equal:', d1[k], 'and', d2[k])
                prog['True'] += 1
    print(prog)
    if prog['False'] == 0:
        return True
    else:
        return False


def compare_lists(l1, l2):  # or tuple
    prog = {'True': 0, 'False': 0}
    if len(l1) != len(l2):
        return False
    else:
        for i1 in l1:
            for i2 in l2:
                if type(i1) is list and type(i2) is list:
                    if compare_lists(i1, i2):
                        prog['True'] += 1
                    else:
                        prog['False'] += 1
                elif type(i1) is dict and type(i2) is dict:
                    if compare_dicts(i1, i2):
                        prog['True'] += 1
                    else:
                        prog['False'] += 1
                elif i1 == i2:
                    prog['True'] += 1
                elif i1 != i2:
                    print(i1, i2)
                    prog['False'] += 1


    if prog['False'] == 0:
        return True
    else:
        return False

print(compare_dicts(d1, d2))
print(compare_lists(d3, d4))
import json

json1 = json.loads('{"num": {"values":{"1":123.53242123, "2":41.5123552}, "params": 12}, "name": "Bob"}')
json2 = json.loads('{"num": {"values":{"1":123.53242321, "2":41.5123451}, "params": 13}, "name": "Bob"}')


def compare_float(num_1, num_2):
    print('lets compare', num_1, 'and', num_2)
    eps = 10**-5
    if abs(num_1 - num_2) < eps:
        return True
    else:
        return False


def compare_dicts(d1, d2):
    compare_state = {True: 0, False: 0}
    for key in d1.keys():
        print(compare_state)
        if key not in d2:
            print('no key')
            return False
        else:
            if type(d1[key]) is dict:
                print('its dict!')
                compare_dicts(d1[key], d2[key])
                print('we are out of recursion')
            else:
                if type(d1[key]) == float and type(d2[key]) == float:
                    print('ok, here are floaties coming')
                    if compare_float(d1[key], d2[key]):
                        compare_state[True] += 1
                elif d1[key] == d2[key]:
                    print('ok this values are equal: ', d1[key], d2[key])
                    compare_state[True] += 1
                else:
                    print('dicts are not equal')
                    return False
            if compare_state[False] == 0:
                return True
            else:
                print('dicts are not equal')
                return False

compare_dicts(json1, json2)





import json


TOL = 10**-5  # параметр для настройки точности сравнения float


def compare_floats(num1, num2):
    '''
    Функция сравнения двух чисел с плавающей точкой. Точность сравнения зависит от параметра TOL
    :param num1: первое число
    :param num2: второе число
    :return: возвращает True, если числа равны и, соответственно, False, если нет
    '''
    if abs(num1 - num2) < TOL:
        return True
    else:
        return False


def compare_dicts(d1, d2):
    '''
    Поэлементно сравниевает два словаря.
    Если в процессе итерации по элементам обнаруживается словарь, то возникает рекурсивный случай
    Если обнаруживается список, то вызывается функция прохода по списку
    Если обнаруживается число с плавающей точкой, то вызывается функция сравнения этих чисел
    :param d1: первый словарь
    :param d2: второй словарь
    :return: возвращает результаты исполнения функций (булевы) при выполнении условий, либо результат
    сравнения двух элементов, если типы этих элементов не dict, list и float
    '''
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
    '''
    Поэлементно сравниевает два списка.
    Если в процессе итерации по элементам обнаруживается список, то возникает рекурсивный случай
    Если обнаруживается словарь, то вызывается функция прохода по словарю
    Если обнаруживается число с плавающей точкой, то вызывается функция сравнения этих чисел
    :param l1: первый список
    :param l2: второй список
    :return: возвращает результаты исполнения функций (булевы) при выполнении условий, либо результат
    сравнения двух элементов, если типы этих элементов не dict, list и float
    '''
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


def compare_json(obj1, obj2):
    '''
    Функция сравнения двух json объектов после их декодирования. В случае, если это не валидные объекты и
    декодировать их не получилось - функция возвращает False.
    Если типы получившихся после декодирования объектов совпадают, то дальше идет сравнения элементов этих объектов.
    В зависимости от их типа используются разные методики сравнения
    :param obj1: первый JSON-объект
    :param obj2: второй JSON-объект
    :return: Возвращает True или False в зависимости от результата
    '''
    try:
        json1 = json.loads(obj1)
        json2 = json.loads(obj2)
    except json.JSONDecodeError:
        return False
    if type(json1) == type(json2):
        if type(json1) is dict:
            return compare_dicts(json1, json2)
        if type(json1) is list:
            return compare_lists(json1, json2)
        if type(json1) is float:
            return compare_floats(json1, json2)
        else:
            return json1 == json2
    else:
        return False


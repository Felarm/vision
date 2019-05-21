import unittest, json
from task_1 import task_1_1, task_1_2

data_test_json = ['[{"params": {"para1": 123.123456, "para2": 72.9876513, "para3": 72.9851243}}]',
                    '[{"params": {"para1": 123.1234572, "para2": 72.9876512, "para3": 72.9851213}}]']

data_test_dicts = [{"params": {"para1": 123.123456, "para2": 72.9876513, "para3": 72.98512}},
                   {"params": {"para1": 123.1234572, "para2": 72.9876512, "para3": 72.98513}}]

data_test_floats = [123.123456, 123.123458]

data_test_lists = [[123.123456, 123.123458], [123.123452, 123.1234531]]


class TestFunc1(unittest.TestCase):
    ''' Тестирование модуля task_1_1.py '''
    def setUp(self):
        self.compare_floats = task_1_1.compare_floats
        self.compare_dicts = task_1_1.compare_dicts
        self.compare_lists = task_1_1.compare_lists
        self.compare_jsons = task_1_1.compare_json
        self.d1 = data_test_dicts[0]
        self.d2 = data_test_dicts[1]
        self.n1 = data_test_floats[0]
        self.n2 = data_test_floats[1]
        self.l1 = data_test_lists[0]
        self.l2 = data_test_lists[1]
        self.j1 = data_test_json[0]
        self.j2 = data_test_json[1]

    def test_true_result(self):
        self.assertTrue(self.compare_floats(self.n1, self.n2), msg='{} and {} are not same'.format(self.n1, self.n2))
        self.assertTrue(self.compare_dicts(self.d1, self.d2), msg='{} and {} are not same'.format(self.d1, self.d2))
        self.assertTrue(self.compare_lists(self.l1, self.l2), msg='{} and {} are not same'.format(self.l1, self.l2))
        self.assertTrue(self.compare_jsons(self.j1, self.j2), msg='{} and {} are not same'.format(self.j1, self.j2))


class TestFunc2(unittest.TestCase):
    ''' Тестирование модуля task_1_2.py '''
    def setUp(self):
        self.find_fifth = task_1_2.find_fifth
        self.compare_jsons = task_1_2.compare_json
        self.j1 = data_test_json[0]
        self.j2 = data_test_json[1]

    def test_true_result(self):
        self.assertTrue(self.compare_jsons(self.j1, self.j2), msg='passed')
        self.assertEqual(self.find_fifth('1.12345621'), self.find_fifth('1.12345678'),
                         msg='{} and {} are not same'.format(self.find_fifth('1.12345621'), self.find_fifth('1.12345678')))
        self.assertNotEqual(self.find_fifth('123.12344'), self.find_fifth('123.12345'),
                            msg='{} and {} are same'.format(self.find_fifth('123.12344'), self.find_fifth('123.12345')))


if __name__ == '__main__':
    unittest.main()

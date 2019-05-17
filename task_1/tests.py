import unittest
from task_1 import task_1_1, task_1_2


class TestFunc1(unittest.TestCase):
    ''' Тестирование модуля task_1_1.py '''
    def setUp(self):
        self.compare_floats = task_1_1.compare_floats
        self.compare_dicts = task_1_1.compare_dicts
        self.compare_lists = task_1_1.compare_lists
        self.compare_jsons = task_1_1.compare_json

    def test_true_result(self):
        self.assertTrue(self.compare_floats(n1, n2), msg='passed')
        self.assertTrue(self.compare_dicts(d1, d2), msg='passed')
        self.assertTrue(self.compare_lists(l1, l2), msg='passed')
        self.assertTrue(self.compare_jsons(j1, j2), msg='passed')

    def test_false_result(self):
        self.assertFalse(self.compare_floats(n1, n2), msg='passed')
        self.assertFalse(self.compare_dicts(d1, d2), msg='passed')
        self.assertFalse(self.compare_lists(l1, l2), msg='passed')
        self.assertFalse(self.compare_jsons(j1, j2), msg='passed')


class TestFunc2(unittest.TestCase):
    ''' Тестирование модуля task_1_2.py '''
    def setUp(self):
        self.find_fifth = task_1_2.find_fifth
        self.compare_jsons = task_1_2.compare_json

    def test_true_result(self):
        self.assertTrue(self.compare_jsons(j1, j2), msg='passed')

    def test_false_result(self):
        self.assertTrue(self.compare_jsons(j1, j2), msg='passed')


if __name__ == '__main__':
    unittest.main()

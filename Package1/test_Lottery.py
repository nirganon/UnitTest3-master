from unittest import TestCase, mock
from Lottery import Lottery
from unittest.mock import patch
import requests
class TestLottery(TestCase):
    def setUp(self):
        self.my_loto = Lottery()

    def test_rand_numbers1(self):
        my_loto=Lottery()
        self.assertTrue(my_loto.valid_numbers)
    def test_rand_numbers2(self):
        my_loto=Lottery()
        self.assertTrue((len(my_loto.rand_numbers()) == 6))
    def test_valid_range(self):
        my_loto=Lottery
        self.assertTrue(1 <= max(my_loto.rand_numbers(self)) <= 45)
        self.assertTrue(1 <= min(my_loto.rand_numbers(self)) <= 45)

    @mock.patch('Lottery.Lottery.rand_numbers', return_value=[2,44,26,31,26,25])
    def test_valid_numbers_false(self, mock_rand_numbers):
        my_loto = Lottery
        self.assertFalse(self.my_loto.valid_numbers())
        print(self.my_loto)

    @mock.patch('Lottery.Lottery.rand_numbers', return_value=[2, 44, 26, 31, 27, 25])
    def test_valid_numbers_false(self, mock_rand_numbers):
        my_loto = Lottery
        self.assertTrue(self.my_loto.valid_numbers())
        print(self.my_loto)

    def test_valid_range_out_of_range(self):
        with patch('Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value=[0,1,45,34,2,7]
            print('out of range values', mock_rand_num.return_value)
            self.assertFalse(self.my_loto.valid_range())

            mock_rand_num.return_value = [46, 1, 45, 34, 2, 7]
            print('out of range values', mock_rand_num.return_value)
            self.assertFalse(self.my_loto.valid_range())

            mock_rand_num.return_value = [1, 1, 45, 34, 2, 7]
            print('out of range values', mock_rand_num.return_value)
            self.assertFalse(self.my_loto.valid_numbers())

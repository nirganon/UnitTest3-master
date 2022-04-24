from unittest import TestCase, mock
from unittest.mock import patch
from student1 import Student1

class TestStudent1(TestCase):

    def setUp(self) -> None:
        self.student = Student1(1234, "nir", 21)

    def test__init__valid(self):
        self.assertEqual(1234,self.student.id)
        self.assertEqual("nir", self.student.name)
        self.assertEqual(21, self.student.age)

    def test__init__invalid_arguments(self):
       with self.assertRaises(TypeError):
           st = Student1([1,5,9,2],"nir",21)
       with self.assertRaises(TypeError):
           st = Student1(123455, 69, 21)
       with self.assertRaises(TypeError):
           st = Student1(125245, "nir", "ggggg")
       with self.assertRaises(TypeError):
           st = Student1(125245, "nir", -1)
       with self.assertRaises(TypeError):
           st = Student1(125245, "nir", 121)

    def test_add_grade_valid(self):
        self.student.AddGrade("math", 90)
        self.assertEqual(self.student.grades_sheet["math"], 90)

    def test_add_bigger_grade(self):
        self.student.AddGrade("math", 101)
        self.assertEqual(self.student.grades_sheet["math"], 100)

    def test_add_smaller_grade(self):
        self.student.AddGrade("math", -1)
        self.assertEqual(self.student.grades_sheet["math"], 0)

    def test_add_invalid_grade(self):
        with self.assertRaises(TypeError):
            self.student.AddGrade(456,69)
        with self.assertRaises(TypeError):
            self.student.AddGrade("biology", "whhh")
        with self.assertRaises(TypeError):
            self.student.AddGrade(456, "daf")

    def test_calc_valid_factor(self):
        self.student.grades_sheet = {"math": 90, "chemistry": 99, "biology": 30}
        self.student.calc_factor("math", -10)
        self.assertEqual(self.student.grades_sheet["math"], 81)
        self.student.calc_factor("biology", 20)
        self.assertEqual(self.student.grades_sheet["biology"], 36)
        self.student.calc_factor("chemistry", 10)
        self.assertEqual(self.student.grades_sheet["chemistry"], 100)

    def test_calc_invalid_factor(self):
        with self.assertRaises(TypeError):
            self.student.calc_factor("math", -101)
        with self.assertRaises(TypeError):
            self.student.calc_factor("math", "many")
        with self.assertRaises(TypeError):
            self.student.calc_factor("math", [34, 67])
        with self.assertRaises(TypeError):
            self.student.calc_factor(78, 69)

    def test_average(self):
        self.student.grades_sheet = {"math": 90, "chemistry": 99, "biology": 30}
        self.assertEqual(73, self.student.Average())

    def test__eq__(self):
        st1 = Student1(123, "marom", 22)
        st2 = Student1(122, "marom", 22)
        st3 = Student1(123, "lion", 69)
        st4 = Student1(123, "marom", 22)
        self.assertEqual(st1, st3)
        self.assertFalse(st1 == st2)
        self.assertEqual(st1, st4)

    def test__gt__(self):
        st1 = Student1(121, "marom", 22)
        st2 = Student1(122, "marom", 23)
        st3 = Student1(100, "lion", 69)
        st4 = Student1(120, "marom", 22)
        self.assertTrue(st2 > st1)
        self.assertFalse(st1 > st4)
        self.assertTrue(st1 < st3)
        self.assertFalse(st1 > st3)



















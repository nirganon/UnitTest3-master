from unittest import TestCase
from course1 import Course1
from student1 import Student1

class TestCourse1(TestCase):
     def setUp(self) -> None:
         self.course = Course1(11, "science", 30)

     def test_init_valid(self):
         self.assertEqual(11, self.course.c_num)
         self.assertEqual("science", self.course.c_name)
         self.assertEqual(30, self.course.capacity)



